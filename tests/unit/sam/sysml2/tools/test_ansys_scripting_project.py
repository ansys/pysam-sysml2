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

"""Unit tests for AnsysScriptingProject using mocker to inject MockedConnectors."""

import pytest

from ansys.sam.sysml2.exception.connector_exception import DiagramNotAvailableException
from ansys.sam.sysml2.tools.ansys_scripting_project import AnsysScriptingProject
from tests.unit.const import (
    PROJECT_ID_2,
    PROJECT_ID_5,
    VALID_ORGANIZATION,
    VALID_TOKEN,
)
from tests.unit.mocked_connector import MockedSysML2APIConnector
from tests.unit.mocked_sam_connector import MockedSamApiConnector


@pytest.fixture
def _patch_connectors(mocker):
    """Patch AnsysSysML2APIConnector and SamRestApiConnector to use mocked versions."""
    mocker.patch(
        "ansys.sam.sysml2.tools.ansys_project.AnsysSysML2APIConnector",
        return_value=MockedSysML2APIConnector(),
    )
    mocker.patch(
        "ansys.sam.sysml2.tools.ansys_project.SamRestApiConnector",
        return_value=MockedSamApiConnector(),
    )


@pytest.mark.usefixtures("_patch_connectors")
class TestAnsysScriptingProject:

    def test_project_loads_and_has_root(self):
        project = AnsysScriptingProject(
            server_url="http://fake",
            organization_id=VALID_ORGANIZATION,
            token=VALID_TOKEN,
            use_ssl=False,
            project_id=PROJECT_ID_5,
        )
        root = project.get_root_package()
        assert root is not None
        assert root._name == "bikeSample"

    def test_is_diagrams_available(self):
        project = AnsysScriptingProject(
            server_url="http://fake",
            organization_id=VALID_ORGANIZATION,
            token=VALID_TOKEN,
            use_ssl=False,
            project_id=PROJECT_ID_5,
        )
        assert project.is_diagrams_available() is True

    def test_no_diagrams_available(self):
        project = AnsysScriptingProject(
            server_url="http://fake",
            organization_id=VALID_ORGANIZATION,
            token=VALID_TOKEN,
            use_ssl=False,
            project_id=PROJECT_ID_2,
        )
        assert project.is_diagrams_available() is False
        with pytest.raises(DiagramNotAvailableException):
            project.download_all_diagrams(path=".")
        with pytest.raises(DiagramNotAvailableException):
            project.download_diagram(path=".", diagram_id="unknown")
        with pytest.raises(DiagramNotAvailableException):
            project.get_project_diagrams_info()
        with pytest.raises(DiagramNotAvailableException):
            project.get_single_diagram_info(diagram_id="unknown")

    def test_get_diagrams_info(self):
        project = AnsysScriptingProject(
            server_url="http://fake",
            organization_id=VALID_ORGANIZATION,
            token=VALID_TOKEN,
            use_ssl=False,
            project_id=PROJECT_ID_5,
        )
        info = project.get_project_diagrams_info()
        assert len(info) == 4
        expected = [
            {"name": "Bike", "numberOfElements": 22, "kind": "SimpleDiagram"},
            {"name": "myBikeInheritance", "numberOfElements": 3, "kind": "SimpleDiagram"},
            {"name": "myBikeRedef", "numberOfElements": 5, "kind": "SimpleDiagram"},
            {"name": "Redef & inheritance", "numberOfElements": 12, "kind": "SimpleDiagram"},
        ]
        for i, exp in enumerate(expected):
            assert info[i]["name"] == exp["name"]
            assert info[i]["numberOfElements"] == exp["numberOfElements"]
            assert info[i]["kind"] == exp["kind"]

    def test_get_single_diagram_info(self):
        project = AnsysScriptingProject(
            server_url="http://fake",
            organization_id=VALID_ORGANIZATION,
            token=VALID_TOKEN,
            use_ssl=False,
            project_id=PROJECT_ID_5,
        )
        diagram_id = "85f84746-3bbc-4b65-8b9c-503d736655eb"
        info = project.get_single_diagram_info(diagram_id)
        assert isinstance(info, dict)
        assert info["name"] == "Bike"
        assert info["diagramId"] == diagram_id
        assert info["numberOfElements"] == 0
