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
"""Specific Module for Ansys Sysml2 API connector."""


import requests

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector


class AnsysRestApiConnector(AnsysSysML2APIConnector):
    """Specific connector class for Ansys SysML 2 Connector."""

    def __init__(self, connector: AnsysSysML2APIConnector):
        """
        Construct Method for new instance.

        Parameters
        ----------
        connector : AnsysSysML2APIConnector
            The connector
        """
        super().__init__(
            server_url=connector._server_url,
            organization_id=connector._organization_id,
            token=connector._token,
            use_ssl=connector._use_ssl,
        )

    def get_project_data(self, model_id: str) -> dict:
        """
        Load projects data from SAM api.

        Parameters
        ----------
        model_id : str
            project Id.

        Returns
        -------
        dict
            Data
        """
        http_request = self._build_http_request(endpoint=f"/projects/{model_id}/json")
        return self._send_request(http_request=http_request, call=requests.get)

    def _build_endpoint(self, endpoint):
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
        return f"{self._server_url}/api/rest/latest{endpoint}"
