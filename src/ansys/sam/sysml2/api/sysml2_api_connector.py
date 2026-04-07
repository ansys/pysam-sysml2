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

"""Top-level interface module for SysML2 API."""


class SysML2APIConnector:
    """Provides the SysML2 API Connector interface."""

    def get_projects(self) -> list:
        """Get all projects of the connected user."""

    def get_project_by_id(self, project_id: str) -> dict:
        """Get project information for the given ID."""

    def create_project(
        self,
        project_name: str,
        project_description: str = "Project description",
    ) -> dict:
        """
        Create a project with the associated name and description.

        Parameters
        ----------
        project_name : str
            Name of the project.
        project_description : str, default: ``"Project description"``
            Description of the project.

        Returns
        -------
        dict
            Project record.
        """

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

    def update_project(
        self,
        project_id: str,
        project_name: str = None,
        project_description: str = None,
    ) -> dict:
        """
        Update the project with the given ID.

        Parameters
        ----------
        project_id : str
            ID of the project to update.
        project_name : str, optional
            New name for the project.
        project_description : str, optional
            New description for the project.

        Returns
        -------
        dict
            Updated project record.
        """

    def get_all_elements(self, project_id: str) -> list:
        """Get all elements of the given project."""

    def get_element_by_id(self, project_id: str, element_id: str) -> dict:
        """
        Get an element by ID and return its information.

        Parameters
        ----------
        project_id : str
            ID of the project where the element is located.
        element_id : str
            ID of the wanted element.

        Returns
        -------
        dict
            Information of the element.
        """

    def get_root_elements(self, project_id: str) -> list:
        """Get all root elements of the project."""

    def execute_query(self, project_id: str, query: str) -> dict:
        """
        Send a query to the standard API using the connector.

        Parameters
        ----------
        project_id : str
            Project ID.
        query : str
            Query in JSON format.

        Returns
        -------
        dict
            Result of the query.
        """
        pass

    def create_commit(self, project_id: str, commit: str) -> dict:
        """
        Send a commit, provided as a JSON string, to the standard API.

        Parameters
        ----------
        project_id : str
            Project ID.
        commit : str
            Commit, in JSON format.

        Returns
        -------
        dict
            Result of the commit.
        """
