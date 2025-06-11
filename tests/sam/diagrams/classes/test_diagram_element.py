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

from conftest import tmp_dir
from mocked_server.mocked_server import MockedServer
from mocked_server.routes.const import PROJECT_ID_3, VALID_ORGANIZATION, VALID_TOKEN
import pytest

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.diagrams.SysML2DiagramManager import SysML2DiagramManager


def get_diagrams(element):
    return element.__diagram


dl_path = tmp_dir / "images"


class TestDiagramElement:
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

    def test_working_dowload_diagram_in_svg(
        self, valid_source: AnsysSysML2APIConnector, project_nb_3: Project
    ):
        package = project_nb_3.get_root_package()

        expected_file_format = "svg"
        expected_filename = f"ae11d5ed-0f61-44a1-b4a7-f727d5bddccd.{expected_file_format}"
        expected_file_path = dl_path / expected_filename

        with SysML2DiagramManager(valid_source) as diagrams:
            diagrams.load_diagrams(project_nb_3)

        aaa = get_diagrams(package)[0]
        aaa.__dict__

        response = get_diagrams(package)[0].download_diagram(expected_file_format, dl_path)

        assert response["status"] == "success"
        assert response["message"].startswith("File saved to ")
        assert response["message"].endswith(expected_filename)

        assert expected_file_path.exists()
        assert expected_file_path.name == expected_filename

    def test_working_dowload_diagram_in_png(
        self, valid_source: AnsysSysML2APIConnector, project_nb_3: Project
    ):
        package = project_nb_3.get_root_package()

        expected_file_format = "png"
        expected_filename = f"ae11d5ed-0f61-44a1-b4a7-f727d5bddccd.{expected_file_format}"
        expected_file_path = dl_path / expected_filename

        with SysML2DiagramManager(valid_source) as diagrams:
            diagrams.load_diagrams(project_nb_3)

        response = get_diagrams(package)[0].download_diagram(expected_file_format, dl_path)

        assert response["status"] == "success"
        assert response["message"].startswith("File saved to ")
        assert response["message"].endswith(expected_filename)

        assert expected_file_path.exists()
        assert expected_file_path.name == expected_filename

    def test_working_dowload_diagram_in_jpeg(
        self, valid_source: AnsysSysML2APIConnector, project_nb_3: Project
    ):
        package = project_nb_3.get_root_package()

        expected_file_format = "jpeg"
        expected_filename = f"ae11d5ed-0f61-44a1-b4a7-f727d5bddccd.{expected_file_format}"
        expected_file_path = dl_path / expected_filename

        with SysML2DiagramManager(valid_source) as diagrams:
            diagrams.load_diagrams(project_nb_3)

        response = get_diagrams(package)[0].download_diagram(expected_file_format, dl_path)

        assert response["status"] == "success"
        assert response["message"].startswith("File saved to ")
        assert response["message"].endswith(expected_filename)

        assert expected_file_path.exists()
        assert expected_file_path.name == expected_filename

    def test_dowload_diagram_with_wrong_argument(
        self, valid_source: AnsysSysML2APIConnector, project_nb_3: Project
    ):
        package = project_nb_3.get_root_package()

        expected_file_format = "WRONG_FILE_FORMAT"
        expected_filename = f"ae11d5ed-0f61-44a1-b4a7-f727d5bddccd.{expected_file_format}"
        expected_file_path = dl_path / expected_filename

        with SysML2DiagramManager(valid_source) as diagrams:
            diagrams.load_diagrams(project_nb_3)

        response = get_diagrams(package)[0].download_diagram(expected_file_format, dl_path)

        assert response["status"] == "error"
        assert response["message"].startswith("404 Client Error: NOT FOUND for url:")

        assert expected_file_path.exists() == False
