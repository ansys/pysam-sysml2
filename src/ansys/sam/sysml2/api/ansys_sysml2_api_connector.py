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

"""Module for Ansys SysML2 API connector."""

import requests

from ansys.sam.sysml2.api.template_sysml2_api_connector import (
    TemplateSysML2APIConnector,
)
from ansys.sam.sysml2.classes.http_request import HttpRequest
from ansys.sam.sysml2.exception.connector_exception import ConnectorException

accepted_versions = ["27"]


class AnsysSysML2APIConnector(TemplateSysML2APIConnector):
    """Provides the Ansys SysML2 connector."""

    _server_url: str
    _organization_id: str
    _token: str

    def __init__(
        self,
        server_url: str,
        token: str,
        organization_id: str,
        use_ssl: bool = True,
        check_version: bool = True,
    ):
        """
        Construct a new instance.

        Parameters
        ----------
        server_url : str
            Server URL.
        token : str
            Authentication token.
        organization_id : str
            Project organization ID.
        use_ssl : bool, default: True
            Whether the server URL uses SSL (valid HTTPS).
        check_version : bool, default: True
            Whether to check the version of the API.
        """
        super().__init__(use_ssl)
        if server_url.endswith("/"):
            server_url = server_url[:-1]
        self._server_url = server_url
        self._organization_id = organization_id
        self._token = token
        if check_version:
            self._check_version()

    def _build_endpoint(self, endpoint: str) -> str:
        """Build the full URL from the API endpoint."""
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
        return f"{self._server_url}/api/spaces/{self._organization_id}/sysml2{endpoint}"

    def _check_version(self):
        """Check the version of the API."""
        http_request = http_request = HttpRequest(f"{self._server_url}/api/status/info")
        response = self._send_request(http_request, requests.get)
        version = response["build"]["version"].split(".")[0]
        if version not in accepted_versions:
            error_text = f"Unsupported SAM server version: {
                response['build']['version']
            }. Accepted versions: {', '.join(f'{v}.*' for v in accepted_versions)}"
            raise ConnectorException(error_text)

    def _add_authentication_field(self, http_request: HttpRequest) -> HttpRequest:
        """
        Update the HTTP request with the correct authentication field.

        Parameters
        ----------
        http_request : HttpRequest
            Request to authenticate.

        Returns
        -------
        HttpRequest
            Authenticated request.
        """
        http_request.headers["Authorization"] = "Bearer " + self._token
        return http_request
