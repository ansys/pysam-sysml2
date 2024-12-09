# Copyright (C) 2024 ANSYS, Inc. and/or its affiliates.
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

"""File created on Tue Dec 03 2024."""

from overrides import override

from ansys.sam.sysml2.auth.connector_auth import ConnectorAuth
from ansys.sam.sysml2.routes.route_dispatcher import RouteDispatcher

from .model_connector import ModelConnector


class SysMLConnector(ModelConnector):
    """Unique class for all SysML V2 Standard API connection."""

    _route_dispatcher: RouteDispatcher = None

    def __init__(self, route_dispatcher: RouteDispatcher, authenticator: ConnectorAuth) -> None:
        super().__init__(authenticator)

    @override
    def get_project_data(self, project_id: str) -> object:
        """
        get_project_data collect information of the project and project elements.

        Parameters
        ----------
        project_id : str
            The Id of the project

        Returns
        -------
        object
            All information collected, for JSON data, the type is Dict
        """

    def get_projects(self) -> list:
        """
        get_projects return all Project of the connected User.

        Returns
        -------
        list
            The list of all projects
        """

    def get_project(self, project_id: str) -> dict:
        """
        get_project return information for the given project.

        Parameters
        ----------
        project_id : str
            Id of the project

        Returns
        -------
        dict
            Information of the project
        """

    def get_elements(self, project_id: str) -> list:
        """
        get_elements return all elements of the given project.

        Parameters
        ----------
        project_id : str
            Project Id

        Returns
        -------
        list
            The list of all elements
        """

    def get_element(self, project_id: str, element_id: str) -> dict:
        """
        get_element return information of the given element.

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

    def query(self, query: str) -> dict:
        """
        Query send a query to the Standard API, using the connector.

        Parameters
        ----------
        query : str
            The query, in JSON format

        Returns
        -------
        dict
            Result of the query
        """

    def commit(self, commit: str) -> dict:
        """
        Commit send a commit to the Standard API using the connector.

        Parameters
        ----------
        commit : str
            The commit with all changes, in JSON formats

        Returns
        -------
        dict
            Result of the Commit
        """
