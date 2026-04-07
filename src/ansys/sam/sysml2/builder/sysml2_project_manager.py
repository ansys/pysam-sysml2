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

from typing import Dict, List

from ansys.sam.sysml2.api.sysml2_api_connector import SysML2APIConnector
from ansys.sam.sysml2.builder.sysml2_project_builder import SysML2ProjectBuilder
from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.classes.scripting_project import ScriptingProject


class SysML2ProjectManager:
    """Provides the director class for loading and managing projects."""

    _connector: SysML2APIConnector
    _constructed_project: Dict[(str, ScriptingProject)]

    def __init__(self, connector: SysML2APIConnector):
        """Construct a new instance with a specified SysML2 API Connector."""
        self._connector = connector
        self._constructed_project = dict()

    def get_projects(self) -> List[dict]:
        """
        Get all projects of the connected user.

        Returns
        -------
        list of dict
            List of all project records.
        """
        return self._connector.get_projects()

    def get_sysml_project(self, project_id: str) -> Project:
        """Get a SysML project with its ID from the API and map it in a Python object."""
        project = self._constructed_project.get(project_id, None)
        if project is None:
            project = SysML2ProjectBuilder(self._connector).build_sysml_project(project_id)
            self._constructed_project[project_id] = project
        return project

    def get_scripting_project(self, project_id: str) -> ScriptingProject:
        """Get a scripting project with its ID from the API and map it in a Python object."""
        project = self._constructed_project.get(project_id, None)
        if project is None:
            project = SysML2ProjectBuilder(self._connector).build_scripting_project(project_id)
            self._constructed_project[project_id] = project
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
        self._constructed_project[project_id] = project
        return project

    def create_scripting_project(
        self,
        name: str,
        description: str = "Project description",
    ) -> ScriptingProject:
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
        ScriptingProject
            The newly created project, fully built from the API.
        """
        project_data = self._connector.create_project(name, description)
        project_id = project_data["@id"]
        project = SysML2ProjectBuilder(self._connector).build_scripting_project(project_id)
        self._constructed_project[project_id] = project
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
            Deleted project record.
        """
        result = self._connector.delete_project(project_id)
        self._constructed_project.pop(project_id, None)
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
        self._constructed_project.pop(project_id, None)
        return result
