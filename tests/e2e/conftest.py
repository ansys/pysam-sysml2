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

"""E2E test configuration: requires a real SAM product instance."""

import base64
import os
from pathlib import Path
from uuid import uuid4

import pytest
import requests as http_requests

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.diagrams.api.sam_rest_api_connector import SamRestApiConnector


@pytest.fixture(scope="session", autouse=True)
def _skip_without_env():
    if not os.environ.get("SAM_SERVER_URL"):
        pytest.skip("SAM_SERVER_URL not set -- skipping e2e tests")


@pytest.fixture(scope="session")
def connector():
    """Provide a real AnsysSysML2APIConnector from environment variables."""
    return AnsysSysML2APIConnector(
        server_url=os.environ["SAM_SERVER_URL"],
        organization_id=os.environ["SAM_ORGANIZATION_ID"],
        token=os.environ["SAM_TOKEN"],
        use_ssl=os.environ.get("SAM_USE_SSL", "true").lower() == "true",
    )


@pytest.fixture(scope="session")
def project_manager(connector):
    """Provide a SysML2ProjectManager bound to the session connector."""
    return SysML2ProjectManager(connector)


@pytest.fixture(scope="session")
def sam_connector():
    """Provide a SamRestApiConnector for diagram operations."""
    return SamRestApiConnector(
        server_url=os.environ["SAM_SERVER_URL"],
        token=os.environ["SAM_TOKEN"],
        use_ssl=os.environ.get("SAM_USE_SSL", "true").lower() == "true",
    )


def _get_models_dir():
    """Resolve the models directory from E2E_MODELS_DIR (default: modeltestset)."""
    return Path(os.environ.get("E2E_MODELS_DIR", "modeltestset"))


def _import_project(connector, project_name, binary_path):
    """Import a .bin file as a new project via POST /organizations/{orgId}/projects/import."""
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


def _create_project(connector, model_name):
    """Create a new project from a .bin file.

    Parameters
    ----------
    connector : AnsysSysML2APIConnector
        Live connector to the SAM server.
    model_name : str
        Name of the model (e.g. "bike"). Resolves to ``{models_dir}/{name}/{name}.bin``.

    Returns
    -------
    Project ID
        The ID of the created project.
    """
    models_dir = _get_models_dir()
    binary_path = models_dir / model_name / f"{model_name}.bin"
    if not binary_path.exists():
        pytest.skip(f"Model binary not found: {binary_path}")

    project_name = f"{model_name}-{uuid4().hex[:8]}"
    project_data = _import_project(connector, project_name, binary_path)
    project_id = project_data["projectId"]
    return project_id


def load_scripting_project(connector, project_manager, model_name):
    """Import a .bin model file and return a ScriptingProject.

    Parameters
    ----------
    connector : AnsysSysML2APIConnector
        Live connector to the SAM server.
    project_manager : SysML2ProjectManager
        Project manager instance.
    model_name : str
        Name of the model (e.g. "bike"). Resolves to ``{models_dir}/{name}/{name}.bin``.

    Returns
    -------
    ScriptingProject
        The loaded scripting project.
    """
    project_id = _create_project(connector, model_name)
    return project_manager.get_scripting_project(project_id)


def load_sysml_project(connector, project_manager, model_name):
    """Import a .bin model file and return a SysML Project.

    Parameters
    ----------
    connector : AnsysSysML2APIConnector
        Live connector to the SAM server.
    project_manager : SysML2ProjectManager
        Project manager instance.
    model_name : str
        Name of the model (e.g. "bike"). Resolves to ``{models_dir}/{name}/{name}.bin``.

    Returns
    -------
    Project
        The loaded SysML project.
    """
    project_id = _create_project(connector, model_name)
    return project_manager.get_sysml_project(project_id)
