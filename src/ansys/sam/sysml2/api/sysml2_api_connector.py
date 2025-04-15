# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
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

"""Top level interface module for SysML2 api."""


class SysML2APIConnector:
    """API Connector Interface."""

    def get_projects(self) -> list:
        """
        Get_projects return all Project of the connected User.

        Returns
        -------
        list
            The list of all projects
        """

    def get_project_by_id(self, project_id: str) -> dict:
        """
        Get_project_by_id return information for the given project.

        Parameters
        ----------
        project_id : str
            Id of the project

        Returns
        -------
        dict
            Information of the project
        """

    def create_project(
        self,
        project_name: str,
        project_description: str = "Project description",
    ) -> dict:
        """
        Create_project creates a project with the associated name and description.

        Parameters
        ----------
        project_name : str
            name of the project
        project_description (optional) : str
            description of the project

        Returns
        -------
        dict
            Project record
        """

    def get_all_elements(self, project_id: str) -> list:
        """
        Get_all_elements return all elements of the given project.

        Parameters
        ----------
        project_id : str
            Project Id

        Returns
        -------
        list
            The list of all elements
        """

    def get_element_by_id(self, project_id: str, element_id: str) -> dict:
        """
        Get_element_by_id return information of the given element.

        Parameters
        ----------
        project_id : str
            Id of the project where the element is
        element_id : str
            Id of the wanted element
        Returns
        -------
        dict
            Information of the element
        """

    def get_root_elements(self, project_id: str) -> list:
        """
        Get_root_elements return all root element of the project.

        Parameters
        ----------
        project_id : str
            Project id

        Returns
        -------
        list
            All root elements
        """

    def execute_query(self, project_id: str, query: str) -> dict:
        """
        Query send a query to the Standard API, using the connector.

        Parameters
        ----------
        project_id : str
            Project id
        query : str
            The query, in JSON format

        Returns
        -------
        dict
            Result of the query
        """

    def create_commit(self, project_id: str, commit: str) -> dict:
        """
        Create a commit and send to the Standard API.

        Parameters
        ----------
        project_id : str
            Project Id
        commit : str
            Commit, in JSON format

        Returns
        -------
        dict
            Result of the commit
        """
