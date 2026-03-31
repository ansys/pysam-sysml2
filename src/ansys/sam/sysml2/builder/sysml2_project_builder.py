# Copyright (C) 2024 - 2026 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Project builder."""

from typing import Dict, List, Set

from ansys.sam.sysml2.api.sysml2_api_connector import SysML2APIConnector
from ansys.sam.sysml2.builder.classes.project_impl import ProjectImpl
from ansys.sam.sysml2.builder.classes.scripting_project_impl import ScriptingProjectImpl
from ansys.sam.sysml2.builder.classes.sysml_util import SysMLUtil
from ansys.sam.sysml2.builder.mapper.mapper import Mapper
from ansys.sam.sysml2.builder.mapper.scripting_mapper import ScriptingMapper
from ansys.sam.sysml2.builder.mapper.sysml_mapper import SysMLMapper
from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.classes.scripting_project import ScriptingProject
from ansys.sam.sysml2.classes.sysml_element import SysMLElement
from ansys.sam.sysml2.dto.query.constraints_classes import (
    CompositeConstraint,
    PrimitiveConstraint,
)
from ansys.sam.sysml2.dto.query.query_class import Query
from ansys.sam.sysml2.dto.query.query_enum import JoinOperator
from ansys.sam.sysml2.exception.mapper_exception import MapperException
from ansys.sam.sysml2.meta_model.e_object import EObject
from ansys.sam.sysml2.meta_model.element import Element
from ansys.sam.sysml2.observer.observer import ModificationObserver

_SCRIPTING_KEEP = {"get_value", "parse_and_set_value", "set_value", "delete"}


class SysML2ProjectBuilder:
    """Provides the SysML2 project builder."""

    _connector: SysML2APIConnector
    _mappers: Dict[str, Mapper] = {
        "Scripting": ScriptingMapper(),
        "SysML": SysMLMapper(),
    }

    def __init__(self, connector: SysML2APIConnector):
        """
        Construct a new instance.

        Parameters
        ----------
        connector : SysML2APIConnector
            SysML2 API connector for server communication.
        """
        self._connector = connector

    def build_sysml_project(self, project_id: str) -> Project:
        """Call the API with the specified project ID and build the SysML project from JSON."""
        project_info = self._connector.get_project_by_id(project_id)
        project = ProjectImpl(project_id, project_info["name"])
        self.__build_project(project)
        return project

    def build_scripting_project(self, project_id: str) -> ScriptingProject:
        """Call the API with the specified project ID and build the scripting project from JSON."""
        project_info = self._connector.get_project_by_id(project_id)
        project = ScriptingProjectImpl(project_id, project_info["name"])
        self.__build_project(project)
        return project

    def __build_project(self, project: Project | ScriptingProject):
        """Build the project from JSON."""
        self._build_project_element(project)
        self._resolve_inherited_link(project)
        self._add_write_access(project)
        self._index_libraries(project)

    def _build_project_element(self, project: Project | ScriptingProject):
        """Build all project elements in the project."""
        elements = self._connector.get_all_elements(project_id=project._id)
        self._map_element_in_project(project, elements)
        missing_elements = self._resolve_fields(project)
        seen = missing_elements.copy()
        while missing_elements:
            new_element = self._get_missing(project, missing_elements)
            self._map_element_in_project(project, new_element)
            missing_elements = self._resolve_fields(project)
            missing_elements.difference_update(seen)
            seen.update(missing_elements)
        self.extract_root_and_check_names(project)

    def extract_root_and_check_names(self, project: Project | ScriptingProject):
        """Extract root elements and resolve inherited names in a single pass.

        Both operations are combined into one iteration over the project
        environment to avoid looping twice. Use ``check_names`` or
        ``extract_root`` individually when only one operation is needed.
        """
        roots = []
        if isinstance(project, Project):
            for element in project._env.values():
                setattr(element, "name", SysMLUtil.check_sysml_inherited_name(element))
                if element.owner is None:
                    roots.append(element)
        elif isinstance(project, ScriptingProject):
            for element in project._env.values():
                setattr(element, "_name", SysMLUtil.check_inherited_name(element))
                if not hasattr(element, "_owner"):
                    roots.append(element)
        else:
            raise TypeError(
                f"Unsupported project type: {type(project).__name__}. "
                "Expected Project or ScriptingProject."
            )
        project._root = roots

    def check_names(self, project: Project | ScriptingProject):
        """Resolve inherited names for all elements."""
        if isinstance(project, Project):
            for element in project._env.values():
                setattr(element, "name", SysMLUtil.check_sysml_inherited_name(element))
        elif isinstance(project, ScriptingProject):
            for element in project._env.values():
                setattr(element, "_name", SysMLUtil.check_inherited_name(element))
        else:
            raise TypeError(
                f"Unsupported project type: {type(project).__name__}. "
                "Expected Project or ScriptingProject."
            )

    def extract_root(self, project: Project | ScriptingProject):
        """Extract root elements from the project."""
        roots = []
        if isinstance(project, Project):
            for element in project._env.values():
                if element.owner is None:
                    roots.append(element)
        elif isinstance(project, ScriptingProject):
            for element in project._env.values():
                if not hasattr(element, "_owner"):
                    roots.append(element)
        else:
            raise TypeError(
                f"Unsupported project type: {type(project).__name__}. "
                "Expected Project or ScriptingProject."
            )
        project._root = roots

    def _get_mapper(self, project: Project | ScriptingProject) -> Mapper:
        """
        Get the correct mapper.

        Parameters
        ----------
        project : Project | ScriptingProject
            Context project.

        Returns
        -------
        Mapper
            Correct mapper.

        Raises
        ------
        MapperException
            If no mapper is found for the project type.
        """
        if isinstance(project, Project):
            return self._mappers.get("SysML")
        elif isinstance(project, ScriptingProject):
            return self._mappers.get("Scripting")
        else:
            raise MapperException(f"No mapper found for project type: {type(project).__name__}")

    def _map_element_in_project(self, project: Project | ScriptingProject, elements: list):
        """
        Map all elements and add them to the context project.

        Parameters
        ----------
        project : Project | ScriptingProject
            Context project.
        elements : list[dict]
            All elements to map.
        """
        unresolved_fields = []
        mapper = self._get_mapper(project)
        for element in elements:
            existing_element = project.find_element_by_id(element["@id"])
            mapped_element = mapper.map(project.get_name(), element, existing_element)
            project.add_element(mapped_element.get_element())
            unresolved_fields.extend(mapped_element.get_unresolved_fields())
        project.update_unresolved_fields(unresolved_fields)

    def _resolve_fields(self, project: Project | ScriptingProject) -> Set[str]:
        """
        Resolve all fields and return missing IDs.

        Parameters
        ----------
        project : Project | ScriptingProject
            Context project.

        Returns
        -------
        Set[str]
            All missing IDs.
        """
        missing = set()
        unresolved_fields = project._unresolved_fields.copy()
        for unresolved_field in unresolved_fields:
            element_id = unresolved_field.get_id()
            element = project._env.get(element_id, None)
            if element is not None:
                unresolved_field.resolve(element)
                project._unresolved_fields.remove(unresolved_field)
            else:
                missing.add(element_id)
        return {x for x in missing if "/?" not in x}

    def _get_missing(
        self, project: Project | ScriptingProject, missing_elements: Set[str]
    ) -> List[dict]:
        """
        Get all missing elements from the API.

        Parameters
        ----------
        project : Project | ScriptingProject
            Current context.
        missing_elements : Set[str]
            All missing element IDs.

        Returns
        -------
        List[dict]
            New element.
        """
        query = Query(None)
        cp = None
        if len(missing_elements) > 1:
            cp = CompositeConstraint(operator=JoinOperator.OR)
            cp.constraint = [
                PrimitiveConstraint(property_name="@id", value=eid) for eid in missing_elements
            ]
        else:
            cp = PrimitiveConstraint(property_name="@id", value=next(iter(missing_elements)))
        query.where = cp
        return self._connector.execute_query(project._id, query.to_json())

    def _resolve_inherited_link(self, project: Project | ScriptingProject):
        """Resolve all inherited elements and add them as members."""
        if isinstance(project, ScriptingProject):
            self._resolve_scripting_inherited_link(project)
        else:
            self._resolve_sysml_inherited_link(project)
        self._resolve_fields(project)

    def _resolve_scripting_inherited_link(self, project: ScriptingProject):
        """Resolve inherited elements for scripting projects."""
        for element in project._env.copy().values():
            for x in dir(element):
                if not x.startswith("_") and x not in _SCRIPTING_KEEP:
                    delattr(element, x)
            all_element = self.__get_all_element(element)
            for x in all_element:
                if hasattr(x, "_name") and getattr(x, "_name") is not None:
                    setattr(element, getattr(x, "_name"), x)
            self._resolve_inherited_elements(project, element)

    def _resolve_sysml_inherited_link(self, project: Project):
        """Resolve inherited elements for SysML projects."""
        for element in project._env.copy().values():
            element._element_hash_map = self.__get_all_sysml_element(element)
            self._resolve_inherited_elements(project, element)

    def _resolve_inherited_elements(
        self,
        project: ScriptingProject | Project,
        element: SysMLElement | Element,
        use_owned_element: bool = False,
    ):
        """
        Resolve all inherited elements into mirrors.

        Parameters
        ----------
        project : ScriptingProject | Project
            Container project.
        element : SysMLElement | Element
            Element to resolve.
        use_owned_element : bool
            Whether to include owned elements alongside inherited ones.
        """
        if isinstance(project, ScriptingProject):
            self._resolve_scripting_inherited_elements(project, element, use_owned_element)
        else:
            self._resolve_sysml_inherited_elements(project, element, use_owned_element)

    def _resolve_scripting_inherited_elements(
        self,
        project: ScriptingProject,
        element: SysMLElement,
        use_owned_element: bool,
    ):
        """Resolve inherited elements for a scripting project element."""
        inherited = getattr(element, "_inheritedFeature", []).copy()
        if use_owned_element:
            inherited.extend(getattr(element, "_ownedElement", []))
        base_id = "/?" + element._id if not element._id.startswith("/?") else element._id

        result = {}
        for inherited_element in inherited:
            if isinstance(inherited_element, str):
                id_ = base_id + inherited_element
            else:
                id_ = base_id + "/?" + inherited_element._id
            mirror_element = SysMLElement(id_)
            project.add_element(mirror_element)
            if not isinstance(inherited_element, str):
                name = self._copy_scripting_data(inherited_element, mirror_element)
                result[name] = mirror_element
            self._resolve_scripting_inherited_elements(
                project, mirror_element, use_owned_element=True
            )
        self._update_scripting_element(element, result)

    def _resolve_sysml_inherited_elements(
        self,
        project: Project,
        element: Element,
        use_owned_element: bool,
    ):
        """Resolve inherited elements for a SysML project element."""
        inherited = getattr(element, "_owned_inherited_feature", []).copy()
        if use_owned_element:
            inherited.extend(getattr(element, "_owned_element", []))
        base_id = "/?" + element.id if not element.id.startswith("/?") else element.id

        result = {}
        for inherited_element in inherited:
            if isinstance(inherited_element, str):
                id_ = base_id + inherited_element
                constructor = Element
            else:
                id_ = base_id + "/?" + inherited_element.id
                constructor = SysMLUtil.get_sysml_constructor(inherited_element.__class__.__name__)
            mirror_element = constructor(id_)
            project.add_element(mirror_element)
            if not isinstance(inherited_element, str):
                name = self._copy_sysml_data(inherited_element, mirror_element)
                result[name] = mirror_element
            self._resolve_sysml_inherited_elements(project, mirror_element, use_owned_element=True)
        self._update_sysml_element(element, result)

    def _copy_sysml_data(self, source: Element, target: Element) -> str:
        """
        Copy function for SysML elements.

        Parameters
        ----------
        source : Element
            Source element.
        target : Element
            Target element.

        Returns
        -------
        str
            Element name.
        """
        eobject_attrs = frozenset(dir(EObject))
        for x in dir(source):
            if x not in eobject_attrs:
                setattr(target, "_" + x, getattr(source, x))
        target._identifier = target._id
        return source.name

    def _copy_scripting_data(self, source: SysMLElement, target: SysMLElement) -> str:
        """
        Copy function for scripting elements.

        Parameters
        ----------
        source : SysMLElement
            Source element.
        target : SysMLElement
            Target element.

        Returns
        -------
        str
            Element name.
        """
        sysml_element_attrs = frozenset(dir(SysMLElement))
        for x in dir(source):
            if x not in sysml_element_attrs and x != "_id":
                setattr(target, x, getattr(source, x))
        target._identifier = target._id
        return source._name

    def _update_sysml_element(self, element: Element, inherited_elements: Dict[str, Element]):
        """
        Update function to add inherited elements.

        Parameters
        ----------
        element : Element
            Base element.
        inherited_elements : Dict[str, Element]
            Contained inherited elements.
        """
        element._element_hash_map.update(inherited_elements)

    def _update_scripting_element(
        self, element: SysMLElement, inherited_elements: Dict[str, SysMLElement]
    ):
        """
        Update function to add inherited elements.

        Parameters
        ----------
        element : SysMLElement
            Base element.
        inherited_elements : Dict[str, SysMLElement]
            Contained inherited elements.
        """
        for name, inherited_element in inherited_elements.items():
            if name is not None:
                setattr(element, name, inherited_element)

    def __get_all_element(self, element: SysMLElement) -> list:
        """Parse all definitions from the element and return its owned elements."""
        all_element = getattr(element, "_ownedElement", []).copy()
        all_element.extend(getattr(element, "_inheritedFeature", []))
        return all_element

    def __get_all_sysml_element(self, element: Element) -> dict:
        """Parse all definitions and collect owned elements."""
        all_element = element.owned_element

        return {x.name: x for x in all_element if isinstance(x, Element)}

    def _add_write_access(self, project: Project | ScriptingProject):
        """Add write rules access on the project."""
        project_modification_observer = ModificationObserver(project, self._connector)
        for element in project._env.values():
            element._observer = project_modification_observer

    def _index_sysml_libraries(self, libraries_elements, element, project):
        """Index libraries of the SysML project for future reload."""
        if not getattr(element, "qualifiedName", "").startswith(project._name):
            libraries_elements.add(element.id)

    def _index_scripting_libraries(self, libraries_elements, element, project):
        """Index libraries of the scripting project for future reload."""
        if not getattr(element, "_qualifiedName", "").startswith(project._name):
            libraries_elements.add(element._id)

    def _index_libraries(self, project: Project | ScriptingProject):
        """Index libraries of the project for future reload."""
        libraries_elements = set()
        call = None
        if isinstance(project, Project):
            call = self._index_sysml_libraries
        elif isinstance(project, ScriptingProject):
            call = self._index_scripting_libraries
        else:
            raise TypeError(f"Unsupported project type: {type(project).__name__}. ")
        for element in project._env.values():
            call(libraries_elements, element, project)
        project._libraries_ids = libraries_elements

    def reload_project(
        self, modification_observer: ModificationObserver, project: Project | ScriptingProject
    ):
        """
        Reload the project and update all its elements.

        Parameters
        ----------
        modification_observer : ModificationObserver
            Observer instance.
        project : Project | ScriptingProject
            Project instance to reload.
        """
        modification_observer.stop()
        self._build_project_element(project)
        self._resolve_inherited_link(project)
        self._add_write_access(project)
        self._index_libraries(project)
        modification_observer.start()
