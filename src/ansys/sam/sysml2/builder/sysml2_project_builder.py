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
_SYSML_KEEP = {"get", "get_value", "parse_and_set_value", "set_value", "delete"}


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
        # TODO(agrzecho): re-introduce library element tracking once the API exposes
        # library elements (bulk in get_all_elements, or per-UUID fetch).
        # https://github.com/ansys/pysam-sysml2/issues/183
        self._build_project_element(project)
        self._resolve_inherited_link(project)
        self._add_write_access(project)

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
        """Extract root elements and resolve inherited names in a single pass."""
        roots = []
        if isinstance(project, Project):
            for element in project._env.values():
                element.declared_name = SysMLUtil.check_sysml_inherited_name(element)
                if self._is_logical_root(element, "owner"):
                    roots.append(element)
        elif isinstance(project, ScriptingProject):
            for element in project._env.values():
                resolved = SysMLUtil.check_inherited_name(element)
                element._name = resolved
                element._declaredName = resolved
                if self._is_logical_root(element, "_owner"):
                    roots.append(element)
        else:
            raise TypeError(
                f"Unsupported project type: {type(project).__name__}. "
                "Expected Project or ScriptingProject."
            )
        project._root = roots

    def _is_logical_root(self, element, owner_attr: str) -> bool:
        """Decide whether ``element`` is a user-facing root of the model."""
        owner = getattr(element, owner_attr, None)
        if owner is None:
            return element.__class__.__name__ != "Namespace"
        return owner.__class__.__name__ == "Namespace" and getattr(owner, owner_attr, None) is None

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
            mapped_element = mapper.map(element, existing_element)
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
        return missing

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
        """Refresh per-element hash map and owned-name set; proxies are created lazily on access."""
        if isinstance(project, ScriptingProject):
            for element in project._env.copy().values():
                self._clear_element(element, _SCRIPTING_KEEP)
                element._element_hash_map = self.__get_all_element(element)
                element._owned_names = self.__get_owned_names(element)
        else:
            for element in project._env.copy().values():
                self._clear_element(element, _SYSML_KEEP)
                element._element_hash_map = self.__get_all_sysml_element(element)
                element._owned_names = self.__get_sysml_owned_names(element)

    def _clear_element(self, element, keep: set[str]) -> None:
        """Drop stale pre-wrapped proxies from a previous build before refilling."""
        for x in list(element.__dict__.keys()):
            if not x.startswith("_") and x not in keep:
                delattr(element, x)

    def __get_all_element(self, element: SysMLElement) -> dict:
        """Return owned + inherited children of a scripting element keyed by ``_name``."""
        all_element = getattr(element, "_ownedElement", []).copy()
        all_element.extend(getattr(element, "_inheritedFeature", []))
        return {x._name: x for x in all_element if isinstance(x, SysMLElement)}

    def __get_owned_names(self, element: SysMLElement) -> set[str]:
        """Return the names of owned (non-inherited) children of a scripting element."""
        return {
            x._name
            for x in getattr(element, "_ownedElement", [])
            if isinstance(x, SysMLElement) and x._name is not None
        }

    def __get_all_sysml_element(self, element: Element) -> dict:
        """Return owned + inherited children of a metamodel element keyed by ``name``."""
        all_element = element.owned_element.copy()
        all_element.extend(getattr(element, "inherited_feature", []).copy())
        return {x.name: x for x in all_element if isinstance(x, Element)}

    def __get_sysml_owned_names(self, element: Element) -> set[str]:
        """Return the names of owned (non-inherited) children of a metamodel element."""
        return {
            x.name for x in element.owned_element if isinstance(x, Element) and x.name is not None
        }

    def _add_write_access(self, project: Project | ScriptingProject):
        """Add write rules access on the project."""
        project_modification_observer = ModificationObserver(project, self._connector)
        for element in project._env.values():
            element._observer = project_modification_observer

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
        modification_observer.start()
