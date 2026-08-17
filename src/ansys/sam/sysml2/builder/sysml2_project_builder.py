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
from ansys.sam.sysml2.builder.classes.sysml_util import SysMLUtil
from ansys.sam.sysml2.builder.derived_collections import fill_derived_collections
from ansys.sam.sysml2.builder.mapper.mapper import Mapper
from ansys.sam.sysml2.builder.mapper.scripting_mapper import ScriptingMapper
from ansys.sam.sysml2.builder.mapper.sysml_mapper import SysMLMapper
from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.dto.query.constraints_classes import (
    CompositeConstraint,
    PrimitiveConstraint,
)
from ansys.sam.sysml2.dto.query.query_class import Query
from ansys.sam.sysml2.dto.query.query_enum import JoinOperator
from ansys.sam.sysml2.exception.mapper_exception import MapperException
from ansys.sam.sysml2.meta_model.element import Element
from ansys.sam.sysml2.observer.observer import ModificationObserver

_SYSML_KEEP = {"get", "get_value", "set_value", "delete"}


def _resolve_includes_derived(
    connector: SysML2APIConnector,
    includes_derived: bool | None,
) -> bool:
    """Resolve ``includes_derived`` using connector defaults when omitted."""
    if includes_derived is not None:
        return includes_derived
    return connector.default_includes_derived()


class SysML2ProjectBuilder:
    """Provides the SysML2 project builder."""

    _connector: SysML2APIConnector
    _mappers: dict[str, Mapper] = {
        "SysML": SysMLMapper(),
        "Scripting": ScriptingMapper(),
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

    def build_sysml_project(
        self,
        project_id: str,
        resolve_libraries: bool = False,
        includes_derived: bool | None = None,
        includes_inherited: bool = True,
    ) -> Project:
        """
        Call the API with the specified project ID and build the SysML project from JSON.

        Parameters
        ----------
        project_id : str
            ID of the project to build.
        resolve_libraries : bool, default: False
            When ``True``, keep library elements' references so their contents are resolved
            and mapped during the build.
        includes_derived : bool | None, default: None
            When ``True``, include derived properties from the API ``/elements`` response.
            When ``None``, use ``connector.default_includes_derived()`` (``False`` on SST).
        includes_inherited : bool, default: True
            When ``True``, include inherited memberships and features from the API response.

        Returns
        -------
        Project
            The fully built SysML project.
        """
        includes_derived = _resolve_includes_derived(self._connector, includes_derived)
        project_info = self._connector.get_project_by_id(project_id)
        project = ProjectImpl(project_id, project_info["name"])
        project._resolve_libraries = resolve_libraries
        project._includes_derived = includes_derived
        project._includes_inherited = includes_inherited
        self.__build_project(project)
        return project

    def build_scripting_project(
        self,
        project_id: str,
        resolve_libraries: bool = False,
        includes_derived: bool | None = None,
        includes_inherited: bool = True,
    ) -> Project:
        """
        Call the API with the specified project ID and build the scripting project from JSON.

        Parameters
        ----------
        project_id : str
            ID of the project to build.
        resolve_libraries : bool, default: False
            When ``True``, keep library elements' references so their contents are resolved
            and mapped during the build.
        includes_derived : bool | None, default: None
            When ``True``, include derived properties from the API ``/elements`` response.
            When ``None``, use ``connector.default_includes_derived()`` (``False`` on SST).
        includes_inherited : bool, default: True
            When ``True``, include inherited memberships and features from the API response.

        Returns
        -------
        Project
            The fully built dynamic project.
        """
        includes_derived = _resolve_includes_derived(self._connector, includes_derived)
        project_info = self._connector.get_project_by_id(project_id)
        project = ProjectImpl(project_id, project_info["name"])
        project._scripting = True
        project._resolve_libraries = resolve_libraries
        project._includes_derived = includes_derived
        project._includes_inherited = includes_inherited
        self.__build_project(project)
        return project

    def __build_project(self, project: Project):
        """Build the project from JSON."""
        # TODO(agrzecho): re-introduce library element tracking once the API exposes
        # library elements (bulk in get_all_elements, or per-UUID fetch).
        # https://github.com/ansys/pysam-sysml2/issues/183
        self._build_project_element(project)
        fill_derived_collections(project)
        self._resolve_inherited_link(project)
        self._add_write_access(project)

    def _build_project_element(self, project: Project) -> None:
        """Build all project elements in the project."""
        roots_json = self._connector.get_root_elements(project_id=project._id)
        root_ids = {root["@id"] for root in roots_json}

        elements_json = self._connector.get_all_elements(
            project_id=project._id,
            includes_derived=project._includes_derived,
            includes_inherited=project._includes_inherited,
        )
        known_ids = {element["@id"] for element in elements_json}
        # The API omits the root Namespace from /elements; mapping an element twice would
        # stack a second UnresolvedField and duplicate it in list fields on resolve.
        elements_json.extend(root for root in roots_json if root["@id"] not in known_ids)

        self._map_element_in_project(project, elements_json)
        missing_elements = self._resolve_fields(project)
        seen = missing_elements.copy()
        while missing_elements:
            new_element = self._get_missing(project, missing_elements)
            self._map_element_in_project(project, new_element)
            missing_elements = self._resolve_fields(project)
            missing_elements.difference_update(seen)
            seen.update(missing_elements)
        self.extract_root_and_check_names(project, root_ids)

    def extract_root_and_check_names(self, project: Project, root_ids: set[str]):
        """Extract root elements and resolve inherited names in a single pass."""
        roots = []
        if isinstance(project, Project):
            dot_safe = getattr(project, "_scripting", False)
            for element in project._env.values():
                element.declared_name = SysMLUtil.check_sysml_inherited_name(
                    element, dot_safe=dot_safe
                )
                if element.id in root_ids:
                    roots.append(element)
        else:
            raise TypeError(
                f"Unsupported project type: {type(project).__name__}. Expected Project."
            )
        project._root = roots

    def _get_mapper(self, project: Project) -> Mapper:
        """
        Get the correct mapper.

        Parameters
        ----------
        project : Project
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
            if getattr(project, "_scripting", False):
                return self._mappers.get("Scripting")
            return self._mappers.get("SysML")
        else:
            raise MapperException(f"No mapper found for project type: {type(project).__name__}")

    def _map_element_in_project(self, project: Project, elements: list):
        """
        Map all elements and add them to the context project.

        Parameters
        ----------
        project : Project
            Context project.
        elements : list[dict]
            All elements to map.
        """
        unresolved_fields = []
        mapper = self._get_mapper(project)
        resolve_libraries = getattr(project, "_resolve_libraries", False)
        for element in elements:
            existing_element = project.find_element_by_id(element["@id"])
            mapped_element = mapper.map(element, existing_element, resolve_libraries)
            project.add_element(mapped_element.get_element())
            unresolved_fields.extend(mapped_element.get_unresolved_fields())
        project.update_unresolved_fields(unresolved_fields)

    def _resolve_fields(self, project: Project) -> set[str]:
        """
        Resolve all fields and return missing IDs.

        Parameters
        ----------
        project : Project
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
        return missing

    def _get_missing(self, project: Project, missing_elements: set[str]) -> list[dict]:
        """
        Get all missing elements from the API.

        Parameters
        ----------
        project : Project
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
        return self._connector.execute_query(
            project._id,
            query.to_json(),
            includes_derived=project._includes_derived,
            includes_inherited=project._includes_inherited,
        )

    def _resolve_inherited_link(self, project: Project):
        """Refresh per-element hash map and owned-name set; proxies are created lazily on access."""
        for element in project._env.copy().values():
            self._clear_element(element, _SYSML_KEEP)
            element._element_hash_map = self.__get_all_sysml_element(element)
            element._owned_names = self.__get_sysml_owned_names(element)

    def _clear_element(self, element, keep: set[str]) -> None:
        """Drop stale pre-wrapped proxies from a previous build before refilling."""
        for x in list(element.__dict__.keys()):
            if not x.startswith("_") and x not in keep:
                delattr(element, x)

    def __get_all_sysml_element(self, element: Element) -> dict:
        """Return owned + inherited children of a metamodel element keyed by ``declared_name``."""
        all_element = element.owned_element.copy()
        all_element.extend(getattr(element, "inherited_feature", []).copy())
        return {x.declared_name: x for x in all_element if isinstance(x, Element)}

    def __get_sysml_owned_names(self, element: Element) -> set[str]:
        """Return the declared names of owned (non-inherited) children of a metamodel element."""
        return {
            x.declared_name
            for x in element.owned_element
            if isinstance(x, Element) and x.declared_name
        }

    def _add_write_access(self, project: Project):
        """Add write rules access on the project."""
        project_modification_observer = ModificationObserver(project, self._connector)
        for element in project._env.values():
            element._observer = project_modification_observer

    def reload_project(
        self,
        modification_observer: ModificationObserver,
        project: Project,
    ):
        """
        Reload the project and update all its elements.

        Parameters
        ----------
        modification_observer : ModificationObserver
            Observer instance.
        project : Project
            Project instance to reload.
        """
        modification_observer.stop()
        project._resolve_libraries = False  # libraries are static; never re-resolve on reload
        self._build_project_element(project)
        fill_derived_collections(project)
        self._resolve_inherited_link(project)
        self._add_write_access(project)
        modification_observer.start()
