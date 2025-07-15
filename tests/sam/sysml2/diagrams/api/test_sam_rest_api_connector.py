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

import pytest

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.diagrams.api.sam_api_connector import SamApiConnector
from ansys.sam.sysml2.diagrams.api.sam_rest_api_connector import SamRestApiConnector
from ansys.sam.sysml2.exception.connector_exception import ConnectorConnectionException
from mocked_server.mocked_server import MockedServer
from mocked_server.routes.const import PROJECT_ID_5, VALID_ORGANIZATION, VALID_TOKEN


class TestAnsysRestApiConnector:

    @pytest.fixture
    def valid__sysml2_source(self) -> AnsysSysML2APIConnector:
        return AnsysSysML2APIConnector(
            server_url=MockedServer.get_url(),
            organization_id=VALID_ORGANIZATION,
            token=VALID_TOKEN,
        )

    @pytest.fixture
    def connector(self) -> SamApiConnector:
        connector = SamRestApiConnector(
            server_url=MockedServer.get_url() + "/",
            token=VALID_TOKEN,
        )
        return connector

    @pytest.fixture
    def project_nb_5(self, valid__sysml2_source: AnsysSysML2APIConnector) -> Project:
        manager = SysML2ProjectManager(valid__sysml2_source)
        project = manager.get_project(PROJECT_ID_5)
        return project

    def test_get_project_data(self, connector: SamApiConnector):
        data = connector.get_project_data(PROJECT_ID_5)
        assert len(data) > 0
        assert "eClass" in data

    def test_build_rest_end_point(self, connector: SamApiConnector):
        url = connector._build_rest_endpoint(f"/projects/{PROJECT_ID_5}/json")
        assert url.endswith("/json")

    def test_build_image_end_point_without_slash(self, connector: SamApiConnector):
        url = connector._build_image_endpoint(f"/svg")
        assert url.endswith("/svg")

    def test_build_rest_end_point_without_slash(self, connector: SamApiConnector):
        url = connector._build_rest_endpoint(f"projects/{PROJECT_ID_5}/json")
        assert url.endswith("/json")

    def test_get_diagrams_info(self, connector: SamRestApiConnector, project_nb_5: Project):
        diagrams_info = connector.get_diagrams_info(project_nb_5._id)

        expected_diagrams = [
            {"name": "Bike", "numberOfElements": 22, "kind": "SimpleDiagram"},
            {"name": "myBikeInheritance", "numberOfElements": 3, "kind": "SimpleDiagram"},
            {"name": "myBikeRedef", "numberOfElements": 5, "kind": "SimpleDiagram"},
            {"name": "Redef & inheritance", "numberOfElements": 12, "kind": "SimpleDiagram"},
        ]

        assert len(diagrams_info) == len(expected_diagrams)

        for i, expected in enumerate(expected_diagrams):
            actual = diagrams_info[i]
            assert actual["name"] == expected["name"]
            assert actual["numberOfElements"] == expected["numberOfElements"]
            assert actual["kind"] == expected["kind"]

    def test_get_single_diagram_info(self, connector: SamRestApiConnector, project_nb_5: Project):
        diagram_id = "85f84746-3bbc-4b65-8b9c-503d736655eb"

        diagram_info = connector.get_single_diagram_info(project_nb_5._id, diagram_id)

        assert isinstance(diagram_info, dict), "Single diagram info should be a dictionary"

        expected_data = {
            "projectId": "dd2e4b9b-a290-4511-a892-aafd0ede597a",
            "diagramId": "85f84746-3bbc-4b65-8b9c-503d736655eb",
            "name": "Bike",
            "kind": "SimpleDiagram",
            "numberOfElements": 0,
        }

        assert diagram_info["projectId"] == expected_data["projectId"]
        assert diagram_info["diagramId"] == expected_data["diagramId"]
        assert diagram_info["name"] == expected_data["name"]
        assert diagram_info["kind"] == expected_data["kind"]
        assert diagram_info["numberOfElements"] == expected_data["numberOfElements"]

    def test_get_single_diagram_info_with_unknown_diagram_id(
        self, connector: SamApiConnector, project_nb_5: Project
    ):
        diagram_id = "unknown"
        with pytest.raises(ConnectorConnectionException):
            connector.get_single_diagram_info(project_nb_5._id, diagram_id)
