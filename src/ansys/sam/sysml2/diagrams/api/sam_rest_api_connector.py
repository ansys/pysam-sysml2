# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
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
"""SAM API connector implementation."""

import json
from typing import Callable, Union

import requests

from ansys.sam.sysml2.classes.http_request import HttpRequest
from ansys.sam.sysml2.diagrams.api import SamApiConnector
from ansys.sam.sysml2.exception.connector_exception import (
    ConnectorConnectionException,
    DiagramConnectorException,
    InvalidElementJsonFoundException,
)


class SamRestApiConnector(SamApiConnector):
    """SAM REST API Connector implementation."""

    _server_url: str

    def __init__(self, server_url: str, token: str, use_ssl: bool = True):
        """Initialize the connector with server URL and authentication token."""
        if server_url.endswith("/"):
            server_url = server_url[:-1]
        self._server_url = server_url
        self._token = token
        self._use_ssl = use_ssl

    def get_project_data(self, model_id: str) -> dict:
        """Retrieve project data from the SAM API using the project identifier."""
        http_request = self._build_rest_http_request(endpoint=f"/projects/{model_id}/json")
        return self._send_request(http_request=http_request, call=requests.get)

    def get_diagrams_info(self, project_id: str) -> dict:
        """Fetch metadata and information for all diagrams within a specific project."""
        http_request = self._build_image_http_request(endpoint=f"/projects/{project_id}/diagrams")
        return self._send_request(http_request=http_request, call=requests.get)

    def get_single_diagram_info(self, project_id: str, diagram_id: str) -> dict:
        """Retrieve detailed information for a single diagram within a project."""
        http_request = self._build_image_http_request(
            endpoint=f"/projects/{project_id}/diagrams/{diagram_id}"
        )
        return self._send_request(http_request=http_request, call=requests.get)

    def get_diagram_image_as_svg(self, project_id: str, diagram_id: str) -> bytes:
        """Download a diagram rendered as SVG format."""
        http_request = self._build_image_http_request(
            endpoint=f"/projects/{project_id}/diagrams/{diagram_id}/svg"
        )
        return self._send_request_binary(http_request=http_request, call=requests.get)

    def get_diagram_image_as_png(self, project_id: str, diagram_id: str) -> bytes:
        """Download a diagram rendered as PNG format."""
        http_request = self._build_image_http_request(
            endpoint=f"/projects/{project_id}/diagrams/{diagram_id}/png"
        )
        return self._send_request_binary(http_request=http_request, call=requests.get)

    def get_diagram_image_as_jpeg(self, project_id: str, diagram_id: str) -> bytes:
        """Download a diagram rendered as JPEG format."""
        http_request = self._build_image_http_request(
            endpoint=f"/projects/{project_id}/diagrams/{diagram_id}/jpeg"
        )
        return self._send_request_binary(http_request=http_request, call=requests.get)

    def get_all_diagram_image_from_project(self, project_id: str, file_format: str) -> bytes:
        """Download all diagrams from a project as a compressed ZIP archive."""
        http_request = self._build_image_http_request(
            endpoint=f"/projects/{project_id}/diagrams/all/{file_format}"
        )
        return self._send_request_binary(http_request=http_request, call=requests.get, stream=True)

    def _send_request(self, http_request: HttpRequest, call: Callable) -> object:
        """Send HTTP request and parse JSON response with error handling."""
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

    def _send_request_binary(
        self, http_request: HttpRequest, call: Callable, stream: bool = False
    ) -> Union[bytes, requests.Response]:
        """Send HTTP request and return binary content or response object for file downloads."""
        try:
            response = call(**http_request.explode(), verify=self._use_ssl, stream=stream)
            response.raise_for_status()
            return response.content if not stream else response
        except Exception as e:
            raise ConnectorConnectionException(e)

    def _handle_http_error(self, response: requests.Response) -> None:
        """Handle HTTP error responses and raise appropriate custom exceptions."""
        match response.status_code:
            case 500:
                raise ConnectorConnectionException("Internal Server Error")
            case _:
                raise DiagramConnectorException(response.content)

    def _build_rest_http_request(self, endpoint: str) -> HttpRequest:
        """Build HTTP request for REST API endpoints."""
        url = self._build_rest_endpoint(endpoint)
        http_request = HttpRequest(url=url)
        return self._add_authentication_field(http_request=http_request)

    def _build_image_http_request(self, endpoint: str) -> HttpRequest:
        """Build HTTP request for Image API endpoints."""
        url = self._build_image_endpoint(endpoint)
        http_request = HttpRequest(url=url)
        return self._add_authentication_field(http_request=http_request)

    def _build_rest_endpoint(self, endpoint: str) -> str:
        """Build the complete URL for REST API endpoints."""
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
        return f"{self._server_url}/api/rest/latest{endpoint}"

    def _build_image_endpoint(self, endpoint: str) -> str:
        """Build the complete URL for Image API endpoints."""
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
        return f"{self._server_url}/api{endpoint}"

    def _add_authentication_field(self, http_request: HttpRequest) -> HttpRequest:
        """Add authentication headers to the HTTP request."""
        http_request.headers["Authorization"] = f"Bearer {self._token}"
        return http_request
