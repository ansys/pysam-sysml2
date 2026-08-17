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

"""Director class for project building."""

from typing import NamedTuple

from ansys.sam.sysml2.api.sysml2_api_connector import SysML2APIConnector
from ansys.sam.sysml2.builder.sysml2_project_builder import SysML2ProjectBuilder
from ansys.sam.sysml2.classes.project import Project


class _ProjectCacheKey(NamedTuple):
    """Cache key for a loaded project variant."""

    project_id: str
    resolve_libraries: bool
    includes_derived: bool
    includes_inherited: bool


class SysML2ProjectManager:
    """Provides the director class for loading and managing projects."""

    _connector: SysML2APIConnector
    _sysml_projects: dict[_ProjectCacheKey, Project]
    _scripting_projects: dict[_ProjectCacheKey, Project]

    def __init__(self, connector: SysML2APIConnector):
        """Construct a new instance with a specified SysML2 API Connector."""
        self._connector = connector
        self._sysml_projects = {}
        self._scripting_projects = {}

    def get_projects(self) -> list[dict]:
        """
        Get all projects of the connected user.

        Returns
        -------
        list of dict
            List of all project records.
        """
        return self._connector.get_projects()

    def get_sysml_project(
        self,
        project_id: str,
        resolve_libraries: bool = False,
        includes_derived: bool = True,
        includes_inherited: bool = True,
    ) -> Project:
        """
        Get a SysML project with its ID from the API and map it in a Python object.

        Parameters
        ----------
        project_id : str
            ID of the project to load.
        resolve_libraries : bool, default: False
            When ``True``, library element contents are resolved and mapped so they can be
            navigated. Only applied on first load; a cached project is returned as-is.
        includes_derived : bool, default: True
            When ``True``, include derived properties from the API ``/elements`` response.
        includes_inherited : bool, default: True
            When ``True``, include inherited memberships and features from the API response.

        Returns
        -------
        Project
            The requested project, built from the API or returned from cache.
        """
        cache_key = self._project_cache_key(
            project_id, resolve_libraries, includes_derived, includes_inherited
        )
        project = self._sysml_projects.get(cache_key)
        if project is None:
            project = SysML2ProjectBuilder(self._connector).build_sysml_project(
                project_id,
                resolve_libraries,
                includes_derived,
                includes_inherited,
            )
            self._sysml_projects[cache_key] = project
        return project

    def get_scripting_project(
        self,
        project_id: str,
        resolve_libraries: bool = False,
        includes_derived: bool = True,
        includes_inherited: bool = True,
    ) -> Project:
        """
        Get a scripting project with its ID from the API and map it in a Python object.

        Parameters
        ----------
        project_id : str
            ID of the project to load.
        resolve_libraries : bool, default: False
            When ``True``, library element contents are resolved and mapped so they can be
            navigated. Only applied on first load; a cached project is returned as-is.
        includes_derived : bool, default: True
            When ``True``, include derived properties from the API ``/elements`` response.
        includes_inherited : bool, default: True
            When ``True``, include inherited memberships and features from the API response.

        Returns
        -------
        Project
            The requested project, built from the API or returned from cache.
        """
        cache_key = self._project_cache_key(
            project_id, resolve_libraries, includes_derived, includes_inherited
        )
        project = self._scripting_projects.get(cache_key)
        if project is None:
            project = SysML2ProjectBuilder(self._connector).build_scripting_project(
                project_id,
                resolve_libraries,
                includes_derived,
                includes_inherited,
            )
            self._scripting_projects[cache_key] = project
        return project

    def create_sysml_project(
        self,
        name: str,
        description: str = "Project description",
    ) -> Project:
        """
        Create a new project on the server and return it as a SysML Project.

        Parameters
        ----------
        name : str
            Name of the project.
        description : str, default: ``"Project description"``
            Description of the project.

        Returns
        -------
        Project
            The newly created project, fully built from the API.
        """
        project_data = self._connector.create_project(name, description)
        project_id = project_data["@id"]
        project = SysML2ProjectBuilder(self._connector).build_sysml_project(project_id)
        cache_key = _ProjectCacheKey(
            project_id=project_id,
            resolve_libraries=False,
            includes_derived=True,
            includes_inherited=True,
        )
        self._sysml_projects[cache_key] = project
        return project

    def create_scripting_project(
        self,
        name: str,
        description: str = "Project description",
    ) -> Project:
        """
        Create a new project on the server and return it as a Scripting Project.

        Parameters
        ----------
        name : str
            Name of the project.
        description : str, default: ``"Project description"``
            Description of the project.

        Returns
        -------
        Project
            The newly created project, fully built from the API.
        """
        project_data = self._connector.create_project(name, description)
        project_id = project_data["@id"]
        project = SysML2ProjectBuilder(self._connector).build_scripting_project(project_id)
        cache_key = _ProjectCacheKey(
            project_id=project_id,
            resolve_libraries=False,
            includes_derived=True,
            includes_inherited=True,
        )
        self._scripting_projects[cache_key] = project
        return project

    def delete_project(self, project_id: str) -> dict:
        """
        Delete the project with the given ID.

        Parameters
        ----------
        project_id : str
            ID of the project to delete.

        Returns
        -------
        dict
            Confirmation containing ``@type`` and ``@id`` of the deleted project.
        """
        result = self._connector.delete_project(project_id)
        self._evict_project_caches(project_id)
        return result

    def update_project(
        self,
        project_id: str,
        name: str = None,
        description: str = None,
    ) -> dict:
        """
        Update the project with the given ID.

        Parameters
        ----------
        project_id : str
            ID of the project to update.
        name : str, optional
            New name for the project.
        description : str, optional
            New description for the project.

        Returns
        -------
        dict
            Updated project record.
        """
        result = self._connector.update_project(project_id, name, description)
        self._evict_project_caches(project_id)
        return result

    @staticmethod
    def _project_cache_key(
        project_id: str,
        resolve_libraries: bool,
        includes_derived: bool,
        includes_inherited: bool,
    ) -> _ProjectCacheKey:
        """
        Build the cache key for a project load variant.

        Parameters
        ----------
        project_id : str
            ID of the project.
        resolve_libraries : bool
            Whether library contents are resolved.
        includes_derived : bool
            Whether derived properties were requested from the API.
        includes_inherited : bool
            Whether inherited memberships and features were requested from the API.

        Returns
        -------
        _ProjectCacheKey
            Named cache key for this load variant.
        """
        return _ProjectCacheKey(
            project_id=project_id,
            resolve_libraries=resolve_libraries,
            includes_derived=includes_derived,
            includes_inherited=includes_inherited,
        )

    def _evict_project_caches(self, project_id: str) -> None:
        """
        Remove all cached variants of a project.

        Parameters
        ----------
        project_id : str
            ID of the project to evict.
        """
        self._scripting_projects = {
            key: project
            for key, project in self._scripting_projects.items()
            if key.project_id != project_id
        }
        self._sysml_projects = {
            key: project
            for key, project in self._sysml_projects.items()
            if key.project_id != project_id
        }
