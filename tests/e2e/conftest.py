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
from ansys.sam.sysml2.diagrams.sam_diagram_manager import SAMDiagramManager
from ansys.sam.sysml2.exception.connector_exception import ProjectNotFoundException


REQUIRED_ENV_VARS = ("SAM_SERVER_URL", "SAM_ORGANIZATION_ID", "SAM_TOKEN")


@pytest.fixture(scope="session", autouse=True)
def _skip_without_env():
    """Skip every e2e test unless the connector fixtures can be built."""
    missing = [name for name in REQUIRED_ENV_VARS if not os.environ.get(name)]
    if missing:
        pytest.skip(f"e2e env vars not set: {', '.join(missing)}")


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


@pytest.fixture
def project_factory(connector, project_manager):
    """Factory fixture: create SAM projects on demand and auto-delete them after the test.

    Usage::

        def test_something(project_factory):
            project = project_factory(model="bike", kind="scripting")
            ...

    Multiple projects may be created in one test; all are cleaned up.
    Tests that delete the project themselves are tolerated via
    ``ProjectNotFoundException`` handling.
    """
    created_ids: list[str] = []

    def _load(model: str = "bike", kind: str = "scripting"):
        project_id = _create_project(connector, model)
        created_ids.append(project_id)
        if kind == "scripting":
            return project_manager.get_scripting_project(project_id)
        if kind == "sysml":
            return project_manager.get_sysml_project(project_id)
        raise ValueError(f"Unknown project kind: {kind!r}")

    yield _load

    for project_id in created_ids:
        try:
            connector.delete_project(project_id)
        except ProjectNotFoundException:
            pass


@pytest.fixture
def project_with_diagrams_factory(project_factory, sam_connector):
    """Factory fixture: create a project (scripting or sysml) with diagrams loaded.

    Usage::

        def test_something(project_with_diagrams_factory):
            project = project_with_diagrams_factory(model="bike", kind="scripting")
            ...
    """

    def _load(model: str = "bike", kind: str = "scripting"):
        project = project_factory(model=model, kind=kind)
        with SAMDiagramManager(connector=sam_connector) as diagrams:
            diagrams.load_diagrams(model=project)
        return project

    return _load
