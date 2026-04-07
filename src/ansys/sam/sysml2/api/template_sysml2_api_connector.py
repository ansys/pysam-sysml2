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
    ProjectNotFoundException,
    UnauthorizedConnectionException,
)


class TemplateSysML2APIConnector(SysML2APIConnector):
    """Provides the abstract class with SysML methods."""

    _use_ssl: bool

    def __init__(self, use_ssl: bool = True):
        """
        Abstract construct method for a new instance.

        Parameters
        ----------
        use_ssl : bool, default: True
            Whether the server use SSL (valid HTTPS).
        """
        super().__init__()
        self._use_ssl = use_ssl

    def get_projects(self) -> list:
        """
        Get all projects of the connected user.

        Returns
        -------
        list
            List of all projects of the connected user.
        """
        http_request = self._build_http_request(endpoint="/projects")
        return self._send_request(http_request, requests.get)

    def get_project_by_id(self, project_id: str) -> dict:
        """
        Get information for a given project.

        Parameters
        ----------
        project_id : str
            ID of the project.

        Returns
        -------
        dict
            Information for the project.
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
        Create a project with a given name and description.

        Parameters
        ----------
        project_name : str
            Name of the project.
        project_description (optional) : str
            Description of the project.

        Returns
        -------
        dict
            Project record.
        """
        if project_name == "":
            raise InvalidProjectNameException(
                "When creating a project, its name must be non-empty."
            )
        http_request = self._build_http_request(endpoint="/projects")
        http_request.json_body = {
            "name": project_name,
            "description": project_description,
        }
        return self._send_request(http_request=http_request, call=requests.post)

    def get_all_elements(self, project_id: str) -> list:
        """
        Get all elements of a given project.

        Parameters
        ----------
        project_id : str
            ID of the project.

        Returns
        -------
        list
            List of all elements.
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
        Get information of a given element.

        Parameters
        ----------
        project_id : str
            ID of the project where the element is located.
        element_id : str
            ID of the given element.

        Returns
        -------
        dict
            Information of the element.
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
        Get all root elements of the project.

        Parameters
        ----------
        project_id : str
            ID of the project.

        Returns
        -------
        list
            All root elements.
        """
        http_request = self._build_http_request(
            endpoint=f"/projects/{project_id}/commits/head/roots"
        )
        return self._send_request(http_request=http_request, call=requests.get)

    def execute_query(self, project_id: str, query: str) -> dict:
        """
        Send a query to the standard API using the connector.

        Parameters
        ----------
        project_id : str
            ID of the project.
        query : str
            Query in JSON format.

        Returns
        -------
        dict
            Result of the query.
        """
        http_request = self._build_http_request(endpoint=f"/projects/{project_id}/query-results")
        http_request.json_body = json.loads(query)
        return self._send_request(http_request=http_request, call=requests.post)

    def create_commit(self, project_id: str, commit: str) -> dict:
        """Send a commit, provided as a JSON string, to the standard API."""
        http_request = self._build_http_request(endpoint=f"/projects/{project_id}/commit")
        http_request.json_body = json.loads(commit)
        return self._send_request(http_request=http_request, call=requests.post)

    def _build_http_request(self, endpoint: str) -> HttpRequest:
        """
        Build a full HTTP request to send from the API endpoint.

        Parameters
        ----------
        endpoint : str
            API endpoint.

        Returns
        -------
        HttpRequest
            Full configured HTTP request.
        """
        url = self._build_endpoint(endpoint)
        http_request = HttpRequest(url=url)
        return self._add_authentication_field(http_request=http_request)

    def _send_request(self, http_request: HttpRequest, call: Callable) -> object:
        """
        Send the HTTP request using the provided call function.

        Parameters
        ----------
        http_request : HttpRequest
            Request to send.
        call : Callable
            Call function for sending the request.

        Returns
        -------
        object
            JSON object (as a dictionary or list).

        Raises
        ------
        ConnectorConnectionException
            If the connection fails.
        ConnectorConnectionException
            If provided information is false.
        InvalidElementJsonFoundException
            If the server returns an invalid element.
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
            HTTP response object received from the server.

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
            HTTP response object with a 404 status code.

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
        """Build the full URL from the API endpoint."""

    def _add_authentication_field(self, http_request: HttpRequest) -> HttpRequest:
        """
        Update the HTTP request with the correct authentication field.

        Parameters
        ----------
        http_request : HttpRequest
            HTTP request to authenticate.

        Returns
        -------
        HttpRequest
            Authenticated request.
        """
