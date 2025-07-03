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

"""Specific Module for ANsy Sysml2 API connector."""

from ansys.sam.sysml2.api.template_sysml2_api_connector import TemplateSysML2APIConnector
from ansys.sam.sysml2.classes.http_request import HttpRequest


class AnsysSysML2APIConnector(TemplateSysML2APIConnector):
    """Specific connector class for Ansys SysML 2 Connector."""

    _server_url: str
    _organization_id: str
    _token: str

    def __init__(
        self,
        server_url: str,
        token: str,
        organization_id: str,
        use_ssl: bool = True,
    ):
        """
        Construct Method for new instance.

        Parameters
        ----------
        server_url : str
            The server URL
        token : str
            Authentication token
        organization_id : str
            Project organization id
        use_ssl : bool, optional
            if the server url SSL (valid HTTPS), by default True
        """
        super().__init__(use_ssl)
        if server_url.endswith("/"):
            server_url = server_url[:-1]
        self._server_url = server_url
        self._organization_id = organization_id
        self._token = token

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
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
        return f"{self._server_url}/api/spaces/{self._organization_id}/sysml2{endpoint}"

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
        http_request.headers["Authorization"] = "Bearer " + self._token
        return http_request
