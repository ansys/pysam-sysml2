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
import json
from typing import Callable

from overrides import override
import requests
from requests import Response

from ansys.sam.sysml2.auth.sysml_auth import SysMLAuth
from ansys.sam.sysml2.core.http_request import HttpRequest
from ansys.sam.sysml2.exception.connector_exception import (
    ConnectorConnectionException,
    ElementNotFoundException,
    HTTPResponseException,
    InvalidElementJsonFoundException,
    ProjectNotFoundException,
)
from ansys.sam.sysml2.routes.route_dispatcher import RouteDispatcher

from .model_connector import ModelConnector


class SysMLConnector(ModelConnector):
    """Unique class for all SysML V2 Standard API connection."""

    _route_dispatcher: RouteDispatcher = None
    _authenticator: SysMLAuth = None
    _is_secure: bool = True

    def __init__(
        self, route_dispatcher: RouteDispatcher, authenticator: SysMLAuth, is_secure: bool = True
    ) -> None:
        super().__init__(authenticator)
        self._route_dispatcher = route_dispatcher
        self._is_secure = is_secure

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
        project_information = self.get_project(project_id=project_id)
        elements = self.get_elements(project_id=project_id)
        project_information["elements"] = elements
        return project_information

    def get_projects(self) -> list:
        """
        get_projects return all Project of the connected User.

        Returns
        -------
        list
            The list of all projects
        """
        url = self._route_dispatcher.build_endpoint("/projects")
        http_request = HttpRequest(url=url)
        http_request = self._authenticator.update_request(request=http_request)
        return self._send_request(http_request, requests.get)

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
        url = self._route_dispatcher.build_endpoint(f"/projects/{project_id}")
        http_request = HttpRequest(url=url)
        http_request = self._authenticator.update_request(request=http_request)
        return self._send_request(
            http_request=http_request,
            call=requests.get,
            exception_dict={404: ProjectNotFoundException},
        )

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
        url = self._route_dispatcher.build_endpoint(f"/projects/{project_id}/commits/head/elements")
        http_request = HttpRequest(url=url)
        http_request = self._authenticator.update_request(request=http_request)
        return self._send_request(
            http_request=http_request,
            call=requests.get,
            exception_dict={404: ProjectNotFoundException},
        )

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
        url = self._route_dispatcher.build_endpoint(
            f"/projects/{project_id}/commits/head/elements/{element_id}"
        )
        http_request = HttpRequest(url=url)
        http_request = self._authenticator.update_request(request=http_request)
        return self._send_request(
            http_request=http_request,
            call=requests.get,
            exception_dict={404: ElementNotFoundException},
        )

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

    def _send_request(
        self, http_request: HttpRequest, call: Callable, exception_dict: dict = None
    ) -> object:
        """
        _send_request send the http request throws the call function.

        Parameters
        ----------
        http_request : HttpRequest
            The request to send
        call : Callable
            THe call function to send the request
        exception_dict : dict
            Association of exception for http return code

        Returns
        -------
        object
            JSON object (as Dict or list)

        Raises
        ------
        ConnectorConnectionException
            When the connection fail
        ConnectorConnectionException
            When provided information are false
        InvalidElementJsonFoundException
            If the server return invalid element
        """
        response = None
        try:
            response = call(**http_request.explode(), verify=self._is_secure)
        except Exception as e:
            raise ConnectorConnectionException(e)

        if response.status_code == 200:
            try:
                return json.loads(response.content)
            except Exception as e:
                raise InvalidElementJsonFoundException(f"Invalid JSON received : {e}")
        else:
            self._check_status_code(response, exception_dict)

    def _check_status_code(self, response: Response, exception_dict: dict) -> None:
        content = response.json()
        if "Organization" in content["description"]:
            raise ConnectorConnectionException(content["description"])
        if response.status_code == 403:
            raise ConnectorConnectionException("Access Forbidden!")
        if exception_dict is not None and response.status_code in exception_dict:
            raise exception_dict[response.status_code](response.content)
        else:
            raise HTTPResponseException(response.content)
