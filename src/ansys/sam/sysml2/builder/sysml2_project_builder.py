# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
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

from typing import List, Set

from ansys.sam.sysml2.api.sysml2_api_connector import SysML2APIConnector
from ansys.sam.sysml2.builder.classes.project_impl import ProjectImpl
from ansys.sam.sysml2.builder.classes.sysml_util import SysMLUtil
from ansys.sam.sysml2.builder.json_mapper import JsonMapper
from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.classes.sysml_element import SysMLElement
from ansys.sam.sysml2.dto.query.constraints_classes import CompositeConstraint, PrimitiveConstraint
from ansys.sam.sysml2.dto.query.query_class import Query
from ansys.sam.sysml2.dto.query.query_enum import JoinOperator
from ansys.sam.sysml2.observer.observer import ModificationObserver


class SysML2ProjectBuilder:
    """Provides the SysML2 project builder."""

    _connector: SysML2APIConnector
    _mapper: JsonMapper = JsonMapper()

    def __init__(self, connector: SysML2APIConnector):
        """
        Construct a new instance.

        Parameters
        ----------
        connector : SysML2APIConnector
            SysML2 API connector.
        """
        self._connector = connector

    def build_project(self, project_id: str) -> Project:
        """
        Call the API and build the project from JSON.

        Parameters
        ----------
        project_id : str
            Project ID.

        Returns
        -------
        Project
            Built project.
        """
        project_info = self._connector.get_project_by_id(project_id)
        project = ProjectImpl(project_id, project_info["name"])
        self._build_project_element(project)
        self._resolve_inherited_link(project)
        self._add_write_access(project)
        self._index_libraries(project)
        return project

    def _build_project_element(self, project: ProjectImpl):
        """
        Build all project elements.

        Parameters
        ----------
        project : ProjectImpl
            Project to build.
        """
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

    def extract_root_and_check_names(self, project: ProjectImpl):
        """
        Extract the root element and update names.

        Parse all project elements and update names.
        Also check if it's a root element.

        Parameters
        ----------
        project : ProjectImpl
            Context project.
        """
        roots = list()
        for _, element in project._env.items():
            setattr(element, "_name", SysMLUtil.check_inherited_name(element))
            if "_owner" not in dir(element):
                roots.append(element)
        project._root = roots

    def _map_element_in_project(self, project: ProjectImpl, elements: list):
        """
        Map all elements and add it to the context project.

        Parameters
        ----------
        project : ProjectImpl
            Context project.
        elements : list
            All element to map.
        """
        unresolved_fields = list()
        for element in elements:
            existing_element = project.find_element_by_id(element["@id"])
            mapped_element = self._mapper.map(project.get_name(), element, existing_element)
            project.add_element(mapped_element.get_element())
            unresolved_fields.extend(mapped_element.get_unresolved_fields())
        project.update_unresolved_fields(unresolved_fields)

    def _resolve_fields(self, project: ProjectImpl) -> Set[str]:
        """
        Resolve all fields and return missing IDs.

        Parameters
        ----------
        project : ProjectImpl
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

    def _get_missing(self, project: ProjectImpl, missing_elements: Set[str]) -> List[dict]:
        """
        Get all missing elements from the API.

        Parameters
        ----------
        project : ProjectImpl
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

    def _resolve_inherited_link(self, project: ProjectImpl):
        """Resolve all inherited elements and add them as members."""
        for _, element in project._env.items():
            [
                delattr(element, x)
                for x in dir(element)
                if not x.startswith("_")
                and x not in ["get_value", "parse_and_set_value", "set_value"]
            ]
            all_element = self.__get_all_element(element)
            [setattr(element, getattr(x, "_name"), x) for x in all_element if hasattr(x, "_name")]

    def __get_all_element(self, element: SysMLElement) -> list:
        """
        Parse all definitions and collect owned elements.

        Parameters
        ----------
        element : SysMLElement
            Base element.

        Returns
        -------
        list
            All owned elements.
        """
        all_element = getattr(element, "_ownedElement", [])
        all_element.extend(getattr(element, "_inheritedFeature", []))
        return all_element

    def _add_write_access(self, project: ProjectImpl):
        """Add write rules access on the project."""
        project_modification_observer = ModificationObserver(project, self._connector)
        for _, element in project._env.items():
            element._observer = project_modification_observer

    def _index_libraries(self, project: ProjectImpl):
        """Index libraries for future reload."""
        libraries_elements = set()
        for _, element in project._env.items():
            if not getattr(element, "_qualifiedName", "").startswith(project._name):
                libraries_elements.add(element._id)
        project._libraries_ids = libraries_elements

    def reload_project(self, modification_observer: ModificationObserver, project: ProjectImpl):
        """Reload the project and update elements."""
        modification_observer.stop_observer()
        self._build_project_element(project)
        self._resolve_inherited_link(project)
        self._add_write_access(project)
        self._index_libraries(project)
        modification_observer.start_observer()
