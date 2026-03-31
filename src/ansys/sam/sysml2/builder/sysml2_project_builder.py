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

from typing import Dict, List, Set, Union

from ansys.sam.sysml2.api.sysml2_api_connector import SysML2APIConnector
from ansys.sam.sysml2.builder.classes.project_impl import ProjectImpl
from ansys.sam.sysml2.builder.classes.scripting_project_impl import ScriptingProjectImpl
from ansys.sam.sysml2.builder.classes.sysml_util import SysMLUtil
from ansys.sam.sysml2.builder.mapper.mapper import Mapper
from ansys.sam.sysml2.builder.mapper.scripting_mapper import ScriptingMapper
from ansys.sam.sysml2.builder.mapper.sysml_mapper import SysmlMapper
from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.classes.scripting_project import ScriptingProject
from ansys.sam.sysml2.classes.sysml_element import SysMLElement
from ansys.sam.sysml2.dto.query.constraints_classes import (
    CompositeConstraint,
    PrimitiveConstraint,
)
from ansys.sam.sysml2.dto.query.query_class import Query
from ansys.sam.sysml2.dto.query.query_enum import JoinOperator
from ansys.sam.sysml2.meta_model.e_object import EObject
from ansys.sam.sysml2.meta_model.element import Element
from ansys.sam.sysml2.observer.observer import ModificationObserver


class SysML2ProjectBuilder:
    """Provides the SysML2 project builder."""

    _connector: SysML2APIConnector
    _mappers: Dict[str, Mapper] = {
        "Scripting": ScriptingMapper(),
        "SysML": SysmlMapper(),
    }

    def __init__(self, connector: SysML2APIConnector):
        """Construct a new instance with a specified SysML2 API Connector."""
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

    def __build_project(self, project: Union[Project | ScriptingProject]):
        """Build the project from JSON."""
        self._build_project_element(project)
        self._resolve_inherited_link(project)
        self._add_write_access(project)
        self._index_libraries(project)

    def _build_project_element(self, project: Union[Project | ScriptingProject]):
        """Build all project elements in the project."""
        elements = self._connector.get_all_elements(project_id=project._id)
        self._map_element_in_project(project, elements)
        missing_elements = self._resolve_fields(project)
        seen = missing_elements.copy()
        while len(missing_elements) != 0:
            new_element = self._get_missing(project, missing_elements)
            self._map_element_in_project(project, new_element)
            missing_elements = self._resolve_fields(project)
            missing_elements.difference_update(seen)
            seen.update(missing_elements)
        self.extract_root_and_check_names(project)

    def extract_root_and_check_names(self, project: Union[Project | ScriptingProject]):
        """Parse all project elements, extract the root element, and update names."""
        roots = list()
        add_function = None
        if isinstance(project, Project):
            add_function = self.filter_and_add_sysml_element
        elif isinstance(project, ScriptingProject):
            add_function = self.filter_and_add_scripting_element
        else:
            raise TypeError(
                f"Unsupported project type: {type(project).name}. "
                "Expected Project or ScriptingProject."
            )
        for _, element in project._env.items():
            add_function(element, roots)
        project._root = roots

    def filter_and_add_sysml_element(self, element: Element, roots: List):
        """
        Filter and check root packages for SysML projects.

        Parameters
        ----------
        element : Element
            Element to check.
        roots : List
            List of root packages.
        """
        setattr(element, "name", SysMLUtil.check_sysml_inherited_name(element))
        if element.owner is None:
            roots.append(element)

    def filter_and_add_scripting_element(self, element: SysMLElement, roots: List):
        """
        Filter and check root packages for Scripting project.

        Parameters
        ----------
        element : SysMLElement
            Element to check.
        roots : List
            List of root packages.
        """
        setattr(element, "_name", SysMLUtil.check_inherited_name(element))
        if getattr(element, "_owner", None) is None:
            roots.append(element)

    def _get_mapper(self, project: Union[Project | ScriptingProject]) -> Mapper:
        """
        Get the correct mapper.

        Parameters
        ----------
        project : Union[Project | ScriptingProject]
            Context project.

        Returns
        -------
        Mapper
            Correct mapper.

        Raises
        ------
        Exception
            If no mapper is correct.
        """
        if isinstance(project, Project):
            return self._mappers.get("SysML")
        elif isinstance(project, ScriptingProject):
            return self._mappers.get("Scripting")
        else:
            raise Exception()

    def _map_element_in_project(self, project: Union[Project | ScriptingProject], elements: list):
        """
        Map all elements and add it to the context project.

        Parameters
        ----------
        project : Union[Project | ScriptingProject]
            Context project.
        elements : list
            All element to map.
        """
        unresolved_fields = list()
        mapper = self._get_mapper(project)
        for element in elements:
            existing_element = project.find_element_by_id(element["@id"])
            mapped_element = mapper.map(project.get_name(), element, existing_element)
            project.add_element(mapped_element.get_element())
            unresolved_fields.extend(mapped_element.get_unresolved_fields())
        project.update_unresolved_fields(unresolved_fields)

    def _resolve_fields(self, project: Union[Project | ScriptingProject]) -> Set[str]:
        """
        Resolve all fields and return missing IDs.

        Parameters
        ----------
        project : Union[Project | ScriptingProject]
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
        return set(x for x in missing if "/?" not in x)

    def _get_missing(
        self, project: Union[Project | ScriptingProject], missing_elements: Set[str]
    ) -> List[dict]:
        """
        Get all missing elements from the API.

        Parameters
        ----------
        project : Union[Project | ScriptingProject]
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
            missing_list = []
            for element_id in missing_elements:
                missing_list.append(
                    PrimitiveConstraint(
                        property="@id",
                        value=element_id,
                    )
                )
            cp.constraint = missing_list
        else:
            cp = PrimitiveConstraint(property="@id", value=list(missing_elements)[0])
        query.where = cp
        self.missing = set()
        return self._connector.execute_query(project._id, query.to_json())

    def _resolve_inherited_link(self, project: Union[Project | ScriptingProject]):
        """Resolve all inherited elements and add them as members."""
        if isinstance(project, ScriptingProject):
            for _, element in project._env.copy().items():
                [
                    delattr(element, x)
                    for x in dir(element)
                    if not x.startswith("_")
                    and x not in ["get_value", "parse_and_set_value", "set_value", "delete"]
                ]
                all_element = self.__get_all_element(element)
                [
                    setattr(element, getattr(x, "_name"), x)
                    for x in all_element
                    if hasattr(x, "_name") and getattr(x, "_name") is not None
                ]
                self._resolve_inherited_elements(project, element)
        else:
            for _, element in project._env.copy().items():
                element._element_hash_map = self.__get_all_sysml_element(element)
                self._resolve_inherited_elements(project, element)
        self._resolve_fields(project)

    def _resolve_inherited_elements(
        self,
        project: Union[ScriptingProject, Project],
        element: Union[SysMLElement | Element],
        use_owned_element: bool = False,
    ):
        """
        Resolve all inherited elements into mirrors.

        Parameters
        ----------
        project : Union[ScriptingProject, Project]
            Container project.
        element : Union[SysMLElement | Element]
            Element to resolve.
        """
        if isinstance(project, ScriptingProjectImpl):
            all_inherited_element = getattr(element, "_inheritedFeature", []).copy()
            if use_owned_element:
                all_inherited_element.extend(getattr(element, "_ownedElement", []))
            base_element = SysMLElement
            base_id = "/?" + element._id if not element._id.startswith("/?") else element._id
            copy_function = self._copy_scripting_data
            update_element = self._update_scripting_element
        else:
            all_inherited_element = getattr(element, "_owned_inherited_feature", []).copy()
            if use_owned_element:
                all_inherited_element.extend(getattr(element, "_owned_element", []))
            base_element = Element
            base_id = "/?" + element.id if not element.id.startswith("/?") else element.id
            copy_function = self._copy_sysml_data
            update_element = self._update_sysml_element
        result = {}
        for inherited_element in all_inherited_element:
            id_ = base_id
            if isinstance(inherited_element, str):
                id_ += inherited_element
            elif isinstance(inherited_element, Element):
                id_ += "/?" + inherited_element.id
            else:
                id_ += "/?" + inherited_element._id

            if base_element == Element and not isinstance(inherited_element, str):
                base_element = SysMLUtil.get_sysml_constructor(inherited_element.__class__.__name__)
            mirror_element = base_element(id_)
            project.add_element(mirror_element)
            if not isinstance(inherited_element, str):
                name = copy_function(inherited_element, mirror_element)
                result[name] = mirror_element

            self._resolve_inherited_elements(project, mirror_element, use_owned_element=True)
        update_element(element, result)

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
        for x in dir(source):
            if x not in dir(EObject):
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
        for x in dir(source):
            if x not in dir(SysMLElement) and x != "_id":
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
        all_element = getattr(element, "_ownedElement", [])
        all_element.extend(getattr(element, "_inheritedFeature", []))
        return all_element

    def __get_all_sysml_element(self, element: Element) -> dict:
        """Parse all definitions and collect owned elements."""
        all_element = element.owned_element

        return dict([(x.name, x) for x in all_element if isinstance(x, Element)])

    def _add_write_access(self, project: ScriptingProjectImpl):
        """Add write rules access on the project."""
        project_modification_observer = ModificationObserver(project, self._connector)
        for _, element in project._env.items():
            element._observer = project_modification_observer

    def _index_sysml_libraries(self, libraries_elements, element, project):
        """Index libraries of the SysML project for future reload."""
        if not getattr(element, "qualifiedName", "").startswith(project._name):
            libraries_elements.add(element.id)

    def _index_scripting_libraries(self, libraries_elements, element, project):
        """Index libraries of the scripting project for future reload."""
        if not getattr(element, "_qualifiedName", "").startswith(project._name):
            libraries_elements.add(element._id)

    def _index_libraries(self, project: ScriptingProjectImpl):
        """Index libraries of the project for future reload."""
        libraries_elements = set()
        call = None
        if isinstance(project, Project):
            call = self._index_sysml_libraries
        elif isinstance(project, ScriptingProject):
            call = self._index_scripting_libraries
        else:
            raise TypeError(f"Unsupported project type: {type(project).name}. ")
        for _, element in project._env.items():
            call(libraries_elements, element, project)
        project._libraries_ids = libraries_elements

    def reload_project(
        self, modification_observer: ModificationObserver, project: ScriptingProjectImpl
    ):
        """
        Reload the project and update all its elements.

        Parameters
        ----------
        modification_observer : ModificationObserver
            Observer instance.
        project : ScriptingProjectImpl
            Scripting project instance to reload.
        """
        modification_observer.stop_observer()
        self._build_project_element(project)
        self._resolve_inherited_link(project)
        self._add_write_access(project)
        self._index_libraries(project)
        modification_observer.start_observer()
