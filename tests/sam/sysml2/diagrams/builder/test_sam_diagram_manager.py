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

import json
from pathlib import Path

import pytest

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.diagrams.api.sam_api_connector import SamApiConnector
from ansys.sam.sysml2.diagrams.api.sam_rest_api_connector import SamRestApiConnector
from ansys.sam.sysml2.diagrams.sam_diagram_manager import SAMDiagramManager
from ansys.sam.sysml2.diagrams.tools.sam_diagram_downloader import SamDiagramDownloader
from ansys.sam.sysml2.exception.connector_exception import DiagramConnectorException
from conftest import tmp_dir
from mocked_server.mocked_server import MockedServer
from mocked_server.routes.const import PROJECT_ID_5, VALID_ORGANIZATION, VALID_TOKEN


def get_diagrams(element):
    return element.__diagram


dl_path = tmp_dir / "images"


class TestSAMDiagramManager:

    @pytest.fixture
    def valid__sysml2_source(self) -> AnsysSysML2APIConnector:
        return AnsysSysML2APIConnector(
            server_url=MockedServer.get_url(),
            organization_id=VALID_ORGANIZATION,
            token=VALID_TOKEN,
        )

    @pytest.fixture
    def valid_sam_api_source(self) -> SamRestApiConnector:
        return SamRestApiConnector(
            server_url=MockedServer.get_url(),
            token=VALID_TOKEN,
        )

    @pytest.fixture
    def project_nb_5(self, valid__sysml2_source: AnsysSysML2APIConnector) -> Project:
        manager = SysML2ProjectManager(valid__sysml2_source)
        project = manager.get_project(PROJECT_ID_5)
        return project

    def test_load_diagrams(self, valid_sam_api_source: SamApiConnector, project_nb_5: Project):
        with SAMDiagramManager(valid_sam_api_source) as diagrams:
            diagrams.load_diagrams(project_nb_5)

        package = project_nb_5.get_root_package()
        bike = package.Bike

        assert len(get_diagrams(package)) == 1
        assert len(get_diagrams(bike)) == 1

        diagram = get_diagrams(package)[0]
        diagram_bike = get_diagrams(bike)[0]

        assert hasattr(diagram, "_name")
        assert hasattr(diagram_bike, "_name")

        assert diagram._name == "general diagram"
        assert diagram_bike._name == "general diagram"

    def test_navigation_through_diagrams(
        self, valid_sam_api_source: SamApiConnector, project_nb_5: Project
    ):
        with SAMDiagramManager(valid_sam_api_source) as diagrams:
            diagrams.load_diagrams(project_nb_5)

        package = project_nb_5.get_root_package()

        diagram = get_diagrams(package)[0]

        diagram_owned_elements = diagram._plane._owned_diagram_elements
        assert len(diagram_owned_elements) == 10

        simple = [x for x in diagram_owned_elements if x.__class__.__name__ == "SimpleNode"]
        for node in simple:
            assert hasattr(node, "_model_element")
        assert len(simple) == 5

    def test_points_are_correctly_typed(
        self, valid_sam_api_source: SamApiConnector, project_nb_5: Project
    ):
        with SAMDiagramManager(valid_sam_api_source) as diagrams:
            diagrams.load_diagrams(project_nb_5)

        package = project_nb_5.get_root_package()
        diagram = get_diagrams(package)[0]
        diagram_owned_elements = diagram._plane._owned_diagram_elements

        path_elements = [x for x in diagram_owned_elements if x.__class__.__name__ == "Path"]
        assert len(path_elements) > 0, "No Path elements found"

        point_elements = []
        for path in path_elements:
            if hasattr(path, "_points") and path._points:
                point_elements.extend(path._points)

        assert len(point_elements) > 0

        actual_points = [p for p in point_elements if p.__class__.__name__ == "Point"]

        assert len(actual_points) > 0

    def test_download_all_diagrams_without_args(
        self, valid_sam_api_source: SamApiConnector, project_nb_5: Project
    ):
        expected_file_format = "svg"
        expected_filename = f"{project_nb_5._id}_{expected_file_format}_diagrams.zip"
        expected_file_path = dl_path / expected_filename

        with SAMDiagramManager(valid_sam_api_source) as diagrams:
            diagrams.load_diagrams(project_nb_5)

        downloader = SamDiagramDownloader(valid_sam_api_source, project_nb_5._id)
        response = downloader.download_all_diagrams(path=dl_path)

        response_path = Path(response)

        assert response_path == expected_file_path
        assert expected_file_path.exists()
        assert response_path.name == expected_filename

        with open(expected_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        expected_data = {
            "success": 200,
            "project_id": PROJECT_ID_5,
            "number_diagrams": 2,
            "file_format": expected_file_format,
        }

        assert data == expected_data

    def test_download_all_diagrams_with_format_only(
        self, valid_sam_api_source: SamApiConnector, project_nb_5: Project
    ):
        expected_file_format = "png"
        expected_filename = f"{project_nb_5._id}_{expected_file_format}_diagrams.zip"
        expected_file_path = dl_path / expected_filename

        with SAMDiagramManager(valid_sam_api_source) as diagrams:
            diagrams.load_diagrams(project_nb_5)

        downloader = SamDiagramDownloader(valid_sam_api_source, project_nb_5._id)
        response = downloader.download_all_diagrams(path=dl_path, file_format=expected_file_format)

        response_path = Path(response)

        assert response_path == expected_file_path
        assert expected_file_path.exists()
        assert response_path.name == expected_filename

        with open(expected_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        expected_data = {
            "success": 200,
            "project_id": PROJECT_ID_5,
            "number_diagrams": 2,
            "file_format": expected_file_format,
        }

        assert data == expected_data

    def test_download_all_diagrams_with_wrong_file_format(
        self, valid_sam_api_source: SamApiConnector, project_nb_5: Project
    ):
        expected_file_format = "WRONG_FILE_FORMAT"
        expected_filename = f"{project_nb_5._id}_{expected_file_format}_diagrams.zip"
        expected_file_path = dl_path / expected_filename

        with SAMDiagramManager(valid_sam_api_source) as diagrams:
            diagrams.load_diagrams(project_nb_5)

        downloader = SamDiagramDownloader(valid_sam_api_source, project_nb_5._id)
        with pytest.raises(DiagramConnectorException):
            downloader.download_all_diagrams(path=dl_path, file_format=expected_file_format)

        assert expected_file_path.exists() == False

    def test_download_all_diagrams_with_filename(
        self, valid_sam_api_source: SamApiConnector, project_nb_5: Project
    ):
        expected_file_format = "svg"
        expected_filename = "download_all_diagrams_with_filename.zip"
        expected_file_path = dl_path / expected_filename

        with SAMDiagramManager(valid_sam_api_source) as diagrams:
            diagrams.load_diagrams(project_nb_5)

        downloader = SamDiagramDownloader(valid_sam_api_source, project_nb_5._id)
        response = downloader.download_all_diagrams(path=dl_path, filename=expected_filename)

        response_path = Path(response)

        assert response_path == expected_file_path
        assert expected_file_path.exists()
        assert response_path.name == expected_filename

        with open(expected_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        expected_data = {
            "success": 200,
            "project_id": PROJECT_ID_5,
            "number_diagrams": 2,
            "file_format": expected_file_format,
        }

        assert data == expected_data

    def test_download_all_diagrams_with_args(
        self, valid_sam_api_source: SamApiConnector, project_nb_5: Project
    ):
        expected_file_format = "png"
        expected_filename = "download_all_diagrams_with_args.zip"
        expected_file_path = dl_path / expected_filename

        with SAMDiagramManager(valid_sam_api_source) as diagrams:
            diagrams.load_diagrams(project_nb_5)

        downloader = SamDiagramDownloader(valid_sam_api_source, project_nb_5._id)
        response = downloader.download_all_diagrams(
            path=dl_path, file_format=expected_file_format, filename=expected_filename
        )

        response_path = Path(response)

        assert response_path == expected_file_path
        assert expected_file_path.exists()
        assert response_path.name == expected_filename

        with open(expected_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        expected_data = {
            "success": 200,
            "project_id": PROJECT_ID_5,
            "number_diagrams": 2,
            "file_format": expected_file_format,
        }
        assert data == expected_data
