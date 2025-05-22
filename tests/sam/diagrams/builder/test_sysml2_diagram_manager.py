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

import json

import pytest

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.diagrams.SysML2DiagramManager import SysML2DiagramManager
from conftest import tmp_dir
from mocked_server.mocked_server import MockedServer
from mocked_server.routes.const import PROJECT_ID_3, VALID_ORGANIZATION, VALID_TOKEN


def get_diagrams(element):
    return element.__diagram


dl_path = tmp_dir / "images"


class TestSysML2DiagramManager:

    @pytest.fixture
    def valid_source(self) -> AnsysSysML2APIConnector:
        return AnsysSysML2APIConnector(
            server_url=MockedServer.get_url(),
            organization_id=VALID_ORGANIZATION,
            token=VALID_TOKEN,
        )

    @pytest.fixture
    def project_nb_3(self, valid_source: AnsysSysML2APIConnector) -> Project:
        manager = SysML2ProjectManager(valid_source)
        project = manager.get_project(PROJECT_ID_3)
        return project

    def test_load_diagrams(self, valid_source: AnsysSysML2APIConnector, project_nb_3: Project):
        with SysML2DiagramManager(valid_source) as diagrams:
            diagrams.load_diagrams(project_nb_3)

        package = project_nb_3.get_root_package()
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
        self, valid_source: AnsysSysML2APIConnector, project_nb_3: Project
    ):
        with SysML2DiagramManager(valid_source) as diagrams:
            diagrams.load_diagrams(project_nb_3)

        package = project_nb_3.get_root_package()

        diagram = get_diagrams(package)[0]

        diagram_owned_elements = diagram._plane._owned_diagram_elements
        assert len(diagram_owned_elements) == 10

        simple = [x for x in diagram_owned_elements if x.__class__.__name__ == "SimpleNode"]
        for node in simple:
            assert hasattr(node, "_model_element")
        assert len(simple) == 5

    def test_download_all_diagrams_without_args(
        self, valid_source: AnsysSysML2APIConnector, project_nb_3: Project
    ):
        package = project_nb_3.get_root_package()
        expected_file_format = "svg"
        expected_filename = f"{package._name}_{expected_file_format}_diagrams.zip"
        expected_file_path = dl_path / expected_filename

        with SysML2DiagramManager(valid_source) as diagrams:
            diagrams.load_diagrams(project_nb_3)
            response = diagrams.download_all_diagrams(project=project_nb_3, path=dl_path)

        assert response["status"] == "success"
        assert response["message"].startswith("File saved to ")
        assert response["message"].endswith(expected_filename)

        assert expected_file_path.exists()
        assert expected_file_path.name == expected_filename

        with open(expected_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        expected_data = {
            "success": 200,
            "project_id": PROJECT_ID_3,
            "number_diagrams": 2,
            "file_format": expected_file_format,
        }

        assert data == expected_data

    def test_download_all_diagrams_with_format_only(
        self, valid_source: AnsysSysML2APIConnector, project_nb_3: Project
    ):
        package = project_nb_3.get_root_package()

        expected_file_format = "png"
        expected_filename = f"{package._name}_{expected_file_format}_diagrams.zip"
        expected_file_path = dl_path / expected_filename

        with SysML2DiagramManager(valid_source) as diagrams:
            diagrams.load_diagrams(project_nb_3)
            response = diagrams.download_all_diagrams(
                project=project_nb_3, path=dl_path, file_format=expected_file_format
            )

        assert response["status"] == "success"
        assert response["message"].startswith("File saved to ")
        assert response["message"].endswith(expected_filename)

        assert expected_file_path.exists()
        assert expected_file_path.name == expected_filename

        with open(expected_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        expected_data = {
            "success": 200,
            "project_id": PROJECT_ID_3,
            "number_diagrams": 2,
            "file_format": expected_file_format,
        }

        assert data == expected_data

    def test_download_all_diagrams_with_wrong_file_format(
        self, valid_source: AnsysSysML2APIConnector, project_nb_3: Project
    ):
        package = project_nb_3.get_root_package()

        expected_file_format = "WRONG_FILE_FORMAT"
        expected_filename = f"{package._name}_{expected_file_format}_diagrams.zip"
        expected_file_path = dl_path / expected_filename

        with SysML2DiagramManager(valid_source) as diagrams:
            diagrams.load_diagrams(project_nb_3)
            response = diagrams.download_all_diagrams(
                project=project_nb_3, path=dl_path, file_format=expected_file_format
            )

        assert response["status"] == "error"
        assert response["message"] == 'Download failed: 404 - "File format not supported"\n'

        assert expected_file_path.exists() == False

    def test_download_all_diagrams_with_jpeg_format_gives_jpg(
        self, valid_source: AnsysSysML2APIConnector, project_nb_3: Project
    ):
        package = project_nb_3.get_root_package()

        file_format = "jpeg"
        expected_file_format = "jpg"
        expected_filename = f"{package._name}_{file_format}_diagrams.zip"
        expected_file_path = dl_path / expected_filename

        with SysML2DiagramManager(valid_source) as diagrams:
            diagrams.load_diagrams(project_nb_3)
            response = diagrams.download_all_diagrams(
                project=project_nb_3, path=dl_path, file_format=file_format
            )

        assert response["status"] == "success"
        assert response["message"].startswith("File saved to ")
        assert response["message"].endswith(expected_filename)

        assert expected_file_path.exists()
        assert expected_file_path.name == expected_filename

        with open(expected_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        expected_data = {
            "success": 200,
            "project_id": PROJECT_ID_3,
            "number_diagrams": 2,
            "file_format": expected_file_format,
        }

        assert data == expected_data

    def test_download_all_diagrams_with_filename(
        self, valid_source: AnsysSysML2APIConnector, project_nb_3: Project
    ):
        expected_file_format = "svg"
        expected_filename = "download_all_diagrams_with_filename.zip"
        expected_file_path = dl_path / expected_filename

        with SysML2DiagramManager(valid_source) as diagrams:
            diagrams.load_diagrams(project_nb_3)
            response = diagrams.download_all_diagrams(
                project=project_nb_3, path=dl_path, filename=expected_filename
            )

        assert response["status"] == "success"
        assert response["message"].startswith("File saved to ")
        assert response["message"].endswith(expected_filename)

        assert expected_file_path.exists()
        assert expected_file_path.name == expected_filename

        with open(expected_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        expected_data = {
            "success": 200,
            "project_id": PROJECT_ID_3,
            "number_diagrams": 2,
            "file_format": expected_file_format,
        }

        assert data == expected_data

    def test_download_all_diagrams_with_args(
        self, valid_source: AnsysSysML2APIConnector, project_nb_3: Project
    ):
        expected_file_format = "png"
        expected_filename = "download_all_diagrams_with_args.zip"
        expected_file_path = dl_path / expected_filename

        with SysML2DiagramManager(valid_source) as diagrams:
            diagrams.load_diagrams(project_nb_3)
            response = diagrams.download_all_diagrams(
                project=project_nb_3,
                path=dl_path,
                file_format=expected_file_format,
                filename=expected_filename,
            )

        assert response["status"] == "success"
        assert response["message"].startswith("File saved to ")
        assert response["message"].endswith(expected_filename)

        assert expected_file_path.exists()
        assert expected_file_path.name == expected_filename

        with open(expected_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        expected_data = {
            "success": 200,
            "project_id": PROJECT_ID_3,
            "number_diagrams": 2,
            "file_format": expected_file_format,
        }
        assert data == expected_data
