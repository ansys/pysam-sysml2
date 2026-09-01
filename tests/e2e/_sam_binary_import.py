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

"""Non-standard SAM binary import route, kept out of the standard connector."""

import base64
from pathlib import Path

import requests as http_requests


def import_project(connector, project_name: str, binary_path: Path) -> dict:
    """Upload a ``.bin`` model file as a new project on the SAM server.

    Parameters
    ----------
    connector : AnsysSysML2APIConnector
        Live connector to the SAM server. Private attributes are read.
    project_name : str
        Unique name to register the new project under.
    binary_path : Path
        Filesystem path to the ``.bin`` payload.

    Returns
    -------
    dict
        Parsed JSON response from the import endpoint (contains ``projectId``).
    """
    data = Path(binary_path).read_bytes()
    url = (
        f"{connector._server_url}/api/organizations/"
        f"{connector._organization_id}/projects/import"
    )
    headers = {
        "Authorization": f"Bearer {connector._token}",
        "Content-Type": "application/json",
    }
    body = {
        "name": project_name,
        "visibility": "PRIVATE",
        "importerType": "BINARY",
        "base64data": base64.b64encode(data).decode("ascii"),
    }
    response = http_requests.post(url, json=body, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()
