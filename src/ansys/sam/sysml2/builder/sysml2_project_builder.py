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
from ansys.sam.sysml2.meta_model.element import Element
from ansys.sam.sysml2.observer.observer import ModificationObserver

_SCRIPTING_KEEP = {"get_value", "parse_and_set_value", "set_value", "delete"}
sysml_element_dir = dir(SysMLElement) + ["_id"]


class SysML2ProjectBuilder:
    """Provides the SysML2 project builder."""

    _connector: SysML2APIConnector
    _mappers: dict[str, Mapper] = {
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
        environment to avoid looping twice.
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
                if getattr(element, "_owner", None) is None:
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

    def _resolve_fields(self, project: Project | ScriptingProject) -> set[str]:
        """
        Resolve all fields and return missing IDs.

        Parameters
        ----------
        project : Project | ScriptingProject
            Context project.

        Returns
        -------
        set[str]
            All missing IDs.
        """
        missing = set()
        unresolved_fields = project._unresolved_fields.copy()
        resolved_fields = set()
        for unresolved_field in unresolved_fields:
            element_id = unresolved_field.get_id()
            element = project._env.get(element_id, None)
            if element is not None:
                unresolved_field.resolve(element)
                resolved_fields.add(unresolved_field)
            else:
                missing.add(element_id)
        project._unresolved_fields = [f for f in unresolved_fields if f not in resolved_fields]
        return {x for x in missing if "/?" not in x}

    def _get_missing(
        self, project: Project | ScriptingProject, missing_elements: set[str]
    ) -> list[dict]:
        """
        Get all missing elements from the API.

        Parameters
        ----------
        project : Project | ScriptingProject
            Current context.
        missing_elements : set[str]
            All missing element IDs.

        Returns
        -------
        list[dict]
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
            for element in project._env.copy().values():
                self.clear_element(_SCRIPTING_KEEP, element)
                self.update_element(element)

            self._resolve_dynamic_inherited_fields(project)

        else:
            for element in project._env.copy().values():
                element._element_hash_map = self.__get_all_sysml_element(element)
            self._resolve_sysml_inherited_fields(project)

    def _resolve_dynamic_inherited_fields(self, project: ScriptingProjectImpl):
        """Resolve all inherited fields and add them as members."""
        composed_ids = {
            x.get_id() for x in project._unresolved_fields if x.get_id().startswith("/?")
        }
        elements = {}
        for composed_id in composed_ids:
            elements_ids = composed_id.split("/?")
            element: SysMLElement = project._env.get(elements_ids[-1], None)
            if element is None:
                continue
            parents = self._get_all_parents(project, elements_ids)
            if not parents:
                continue
            elif len(parents) == 1:
                elements.update(self._resolve_single_level_inherited_dynamic(element, parents))
            else:
                elements.update(self._resolve_multi_level_inherited_dynamic(element, parents))
        project._env.update(elements)
        self._resolve_fields(project)

    def _resolve_sysml_inherited_fields(self, project: Project):
        """Resolve all inherited fields and add them as members."""
        composed_ids = {
            x.get_id() for x in project._unresolved_fields if x.get_id().startswith("/?")
        }
        elements = {}
        for composed_id in composed_ids:
            elements_ids = composed_id.split("/?")
            element: Element = project._env.get(elements_ids[-1], None)
            if element is None:
                continue
            parents = self._get_all_parents(project, elements_ids)
            if not parents:
                continue
            elif len(parents) == 1:
                elements.update(self._resolve_single_level_inherited(element, parents))
            else:
                elements.update(self._resolve_multi_level_inherited(element, parents))
        project._env.update(elements)
        self._resolve_fields(project)

    def _resolve_multi_level_inherited_dynamic(self, element, parents):
        """
        Resolve multi-level inherited element.

        Parameters
        ----------
        element :  SysMLElement
            The element to resolve.
        parents : list[Element]
            The list of parent elements.

        Returns
        -------
        dict
            A dictionary containing the resolved inherited element.
        """
        current = parents[0]
        for parent in parents[1:]:
            if parent._name is not None and parent._name in current._element_hash_map:
                current = getattr(current, parent._name, None)
            else:
                return {}
        if element._name is not None and element._name in current._element_hash_map:
            element_ = getattr(current, element._name, None)
        else:
            return {}
        if element_ is not None:
            return {element_._id: element_}
        return {}

    def _resolve_single_level_inherited_dynamic(self, element, parents):
        """
        Resolve single-level inherited element.

        Parameters
        ----------
        element : SysMLElement
            The element to resolve.
        parents : list[Element]
            The list of parent elements.

        Returns
        -------
        dict
            A dictionary containing the resolved inherited element.
        """
        if element._name is not None:
            e = getattr(parents[0], element._name, None)
            if e is not None:
                return {e._id: e}
            return {}
        else:
            from ansys.sam.sysml2.classes.sysml_inherited_element import (
                SysMLInheritedElement,
            )

            element_ = SysMLInheritedElement(
                parents[0],
                next(
                    (e for e in parents[0]._element_hash_map if e._id == element._id),
                    None,
                ),
            )
            if element_._element is not None:
                return {element_._id: element_}
        return {}

    def _resolve_multi_level_inherited(self, element, parents):
        """
        Resolve multi-level inherited element.

        Parameters
        ----------
        element : Element
            The element to resolve.
        parents : list[Element]
            The list of parent elements.

        Returns
        -------
        dict
            A dictionary containing the resolved inherited element.
        """
        current = parents[0]
        for parent in parents[1:]:
            if parent.name is not None and parent.name in current._element_hash_map:
                current = current.get(parent.name)
            else:
                return {}
        if element.name is not None and element.name in current._element_hash_map:
            element_ = current.get(element.name)
        else:
            return {}
        if element_ is not None:
            return {element_.id: element_}
        return {}

    def _resolve_single_level_inherited(self, element, parents):
        """
        Resolve single-level inherited element.

        Parameters
        ----------
        element : Element
            The element to resolve.
        parents : list[Element]
            The list of parent elements.

        Returns
        -------
        dict
            A dictionary containing the resolved inherited element.
        """
        if element.name is not None:
            e = parents[0].get(element.name)
            if e is not None:
                return {e.id: e}
            return {}
        else:
            from ansys.sam.sysml2.classes.sysml_inherited_element import (
                SysMLInheritedElement,
            )

            element_ = SysMLInheritedElement(
                parents[0],
                next(
                    (e for e in parents[0]._element_hash_map if e.id == element.id),
                    None,
                ),
            )
            if element_._element is not None:
                return {element_.id: element_}
        return {}

    def _get_all_parents(self, project, elements_ids):
        """
        Get all parent elements from the composed ID.

        Parameters
        ----------
        project : Project | ScriptingProject
            The project containing the elements.
        elements_ids : list[str]
            The list of element IDs.

        Returns
        -------
        list[Element]
            The list of parent elements.
        """
        parents: list[Element] = []
        for parent_id in elements_ids[1:-1]:
            parent_element = project._env.get(parent_id, None)
            if parent_element is None:
                break
            parents.append(parent_element)
        return parents

    def update_element(self, element):
        """
        Update the element with inherited elements.

        Parameters
        ----------
        element : SysMLElement
            The element to update.
        """
        all_element = self.__get_all_element(element)
        element._element_hash_map = all_element
        for name, e in all_element.items():
            if name is not None:
                setattr(element, f"#{name}", e)

    def clear_element(self, ignore_list, element):
        """
        Clear all inherited elements in the element.

        Parameters
        ----------
        ignore_list : list
            List of attributes to ignore when clearing.
        element : SysMLElement
            The element to clear.
        """
        [
            delattr(element, x)
            for x in list(element.__dict__.keys())
            if not x.startswith("_") and x not in ignore_list
        ]

    def __get_all_element(self, element: SysMLElement) -> dict:
        """Parse all definitions from the element and return its owned elements."""
        all_element = getattr(element, "_ownedElement", []).copy()
        all_element.extend(getattr(element, "_inheritedFeature", []))
        return {x._name: x for x in all_element if isinstance(x, SysMLElement)}

    def __get_all_sysml_element(self, element: Element) -> dict:
        """Parse all definitions and collect owned elements."""
        all_element = element.owned_element.copy()
        all_element.extend(getattr(element, "owned_inherited_feature", []).copy())
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
        self,
        modification_observer: ModificationObserver,
        project: Project | ScriptingProject,
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
