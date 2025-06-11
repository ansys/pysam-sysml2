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

"""Template for implementation of endpoint."""

import json
from typing import Callable

import requests

from ansys.sam.sysml2.api.sysml2_api_connector import SysML2APIConnector
from ansys.sam.sysml2.classes.http_request import HttpRequest
from ansys.sam.sysml2.exception.connector_exception import (
    BadRequestConnectionException,
    ConnectorConnectionException,
    ElementNotFoundException,
    HTTPResponseException,
    InvalidElementJsonFoundException,
    InvalidProjectNameException,
    ModelAsNotChangedException,
    ProjectNotFoundException,
    UnauthorizedConnectionException,
)


class TemplateSysML2APIConnector(SysML2APIConnector):
    """Abstract class with SysML methods."""

    _use_ssl: bool

    def __init__(self, use_ssl: bool = True):
        """
        Abstract Construct Method for new instance.

        Parameters
        ----------
        use_ssl : bool, optional
            If the server use SSL (valid HTTPS), by default True
        """
        super().__init__()
        self._use_ssl = use_ssl

    def get_projects(self) -> list:
        """
        Get_projects return all Project of the connected User.

        Returns
        -------
        list
            The list of all projects
        """
        http_request = self._build_http_request(endpoint="/projects")
        return self._send_request(http_request, requests.get)

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
        http_request = self._build_http_request(endpoint=f"/projects/{project_id}")
        return self._send_request(
            http_request=http_request,
            call=requests.get,
        )

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
        if project_name == "":
            raise InvalidProjectNameException(
                "When creating a project, its name has to be non empty."
            )
        http_request = self._build_http_request(endpoint="/projects")
        http_request.json = {
            "name": project_name,
            "description": project_description,
        }
        return self._send_request(http_request=http_request, call=requests.post)

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
        http_request = self._build_http_request(
            endpoint=f"/projects/{project_id}/commits/head/elements"
        )
        return self._send_request(
            http_request=http_request,
            call=requests.get,
        )

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
        http_request = self._build_http_request(
            endpoint=f"/projects/{project_id}/commits/head/elements/{element_id}"
        )
        return self._send_request(
            http_request=http_request,
            call=requests.get,
        )

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
        http_request = self._build_http_request(
            endpoint=f"/projects/{project_id}/commits/head/roots"
        )
        return self._send_request(http_request=http_request, call=requests.get)

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
        http_request = self._build_http_request(endpoint=f"/projects/{project_id}/query-results")
        http_request.json = json.loads(query)
        return self._send_request(http_request=http_request, call=requests.post)

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
        http_request = self._build_http_request(endpoint=f"/projects/{project_id}/commit")
        http_request.json = json.loads(commit)
        return self._send_request(http_request=http_request, call=requests.post)

    def _build_http_request(self, endpoint: str) -> HttpRequest:
        """
        Build a full HTTP Request to be sended, from API Endpoint.

        Parameters
        ----------
        endpoint : str
            API Endpoint

        Returns
        -------
        HttpRequest
            Full configured HTTP Request.
        """
        url = self._build_endpoint(endpoint)
        http_request = HttpRequest(url=url)
        return self._add_authentication_field(http_request=http_request)

    def _send_request(self, http_request: HttpRequest, call: Callable) -> object:
        """
        Send_request send the http request throws the call function.

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
            response = call(**http_request.explode(), verify=self._use_ssl)
        except Exception as e:
            raise ConnectorConnectionException(e)

        if response.status_code == 200:
            try:
                return json.loads(response.content)
            except Exception as e:
                raise InvalidElementJsonFoundException(f"Invalid JSON received : {e}")
        else:
            self._handle_http_error(response)

    def _handle_http_error(self, response: requests.Response) -> None:
        """
        Handle HTTP errors and raise appropriate exceptions based on the response status code.

        Parameters
        ----------
        response : Response
            The HTTP response object received from the server.

        Raises
        ------
        ConnectorConnectionException
            If the server returns a 500 status code (Internal Server Error) or
            a 403 status code (Forbidden).
        UnauthorizedConnectionException
            If the server returns a 401 status code (Unauthorized).
        HTTPResponseException
            If the server returns any other unhandled status code.
        """
        match response.status_code:
            case 500:
                raise ConnectorConnectionException("Internal Server Error")
            case 404:
                self._handle_404_response(response)
            case 403:
                raise ConnectorConnectionException(response.json()["message"])
            case 401:
                raise UnauthorizedConnectionException("Authentication failed")
            case 400:
                message = response.json()["message"]
                if message == "Model has not changed":
                    raise ModelAsNotChangedException(f"Bad Request : {message}")
                else:
                    raise BadRequestConnectionException(f"Bad Request : {message}")
            case _:
                raise HTTPResponseException(response.content)

    def _handle_404_response(self, response: requests.Response) -> None:
        """
        Handle 404 (Not Found) HTTP responses and raise appropriate exceptions.

        This method parses the response content and raises specific exceptions
        based on the error description provided in the response.

        Parameters
        ----------
        response : Response
            The HTTP response object with a 404 status code.

        Raises
        ------
        ConnectorConnectionException
            If the error is related to an organization not being found.
        ElementNotFoundException
            If the error is related to an element not being found.
        ProjectNotFoundException
            If the error is related to a project not being found.
        HTTPResponseException
            If the error description doesn't match any of the above cases.
        """
        content = response.json()
        if "Organization" in content["message"]:
            raise ConnectorConnectionException(content["message"])
        elif "Element" in content["message"]:
            raise ElementNotFoundException(content["message"])
        elif "Project" in content["message"]:
            raise ProjectNotFoundException(content["message"])
        else:
            raise HTTPResponseException(response.content)

    def _build_endpoint(self, endpoint: str) -> str:
        """
        Build the full URL from the API Endpoint.

        Parameters
        ----------
        endpoint : str
            The API Endpoint

        Returns
        -------
        str
            The full API URL
        """

    def _add_authentication_field(self, http_request: HttpRequest) -> HttpRequest:
        """
        Update the HTTP Request with de correct auth field.

        Parameters
        ----------
        http_request : HttpRequest
            The request to be auth

        Returns
        -------
        HttpRequest
            Authenticated request
        """
