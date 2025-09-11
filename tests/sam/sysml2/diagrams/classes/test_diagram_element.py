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


class TestDiagramElement:

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

    def test_working_dowload_diagram_in_svg(
        self, valid_sam_api_source: SamApiConnector, project_nb_5: Project
    ):
        package = project_nb_5.get_root_package()

        expected_file_format = "svg"
        expected_filename = f"ae11d5ed-0f61-44a1-b4a7-f727d5bddccd.{expected_file_format}"
        expected_file_path = dl_path / expected_filename

        with SAMDiagramManager(valid_sam_api_source) as diagrams:
            diagrams.load_diagrams(project_nb_5)

        downloader = SamDiagramDownloader(valid_sam_api_source, project_nb_5._id)
        diagram = get_diagrams(package)[0]
        response = downloader.download_diagram(
            diagram_id=diagram._id, file_format=expected_file_format, path=dl_path
        )

        response_path = Path(response)

        assert response_path == expected_file_path
        assert expected_file_path.exists()
        assert response_path.name == expected_filename

    def test_working_dowload_diagram_in_png(
        self, valid_sam_api_source: SamApiConnector, project_nb_5: Project
    ):
        package = project_nb_5.get_root_package()

        expected_file_format = "png"
        expected_filename = f"ae11d5ed-0f61-44a1-b4a7-f727d5bddccd.{expected_file_format}"
        expected_file_path = dl_path / expected_filename

        with SAMDiagramManager(valid_sam_api_source) as diagrams:
            diagrams.load_diagrams(project_nb_5)

        downloader = SamDiagramDownloader(valid_sam_api_source, project_nb_5._id)
        diagram = get_diagrams(package)[0]
        response = downloader.download_diagram(
            diagram_id=diagram._id, file_format=expected_file_format, path=dl_path
        )

        response_path = Path(response)

        assert response_path == expected_file_path
        assert expected_file_path.exists()
        assert response_path.name == expected_filename

    def test_working_dowload_diagram_in_jpeg(
        self, valid_sam_api_source: SamApiConnector, project_nb_5: Project
    ):
        package = project_nb_5.get_root_package()

        expected_file_format = "jpeg"
        expected_filename = f"ae11d5ed-0f61-44a1-b4a7-f727d5bddccd.{expected_file_format}"
        expected_file_path = dl_path / expected_filename

        with SAMDiagramManager(valid_sam_api_source) as diagrams:
            diagrams.load_diagrams(project_nb_5)

        downloader = SamDiagramDownloader(valid_sam_api_source, project_nb_5._id)
        diagram = get_diagrams(package)[0]
        response = downloader.download_diagram(
            diagram_id=diagram._id, file_format=expected_file_format, path=dl_path
        )

        response_path = Path(response)

        assert response_path == expected_file_path
        assert expected_file_path.exists()
        assert response_path.name == expected_filename

    def test_dowload_diagram_with_wrong_argument(
        self, valid_sam_api_source: SamApiConnector, project_nb_5: Project
    ):
        package = project_nb_5.get_root_package()

        expected_file_format = "WRONG_FILE_FORMAT"
        expected_filename = f"ae11d5ed-0f61-44a1-b4a7-f727d5bddccd.{expected_file_format}"
        expected_file_path = dl_path / expected_filename

        with SAMDiagramManager(valid_sam_api_source) as diagrams:
            diagrams.load_diagrams(project_nb_5)

        downloader = SamDiagramDownloader(valid_sam_api_source, project_nb_5._id)
        diagram = get_diagrams(package)[0]
        with pytest.raises(DiagramConnectorException):
            downloader.download_diagram(
                diagram_id=diagram._id, file_format=expected_file_format, path=dl_path
            )

        assert expected_file_path.exists() == False

    def test_working_dowload_diagram_with_path_is_a_file(
        self, valid_sam_api_source: SamApiConnector, project_nb_5: Project
    ):
        package = project_nb_5.get_root_package()

        expected_file_format = "png"
        expected_name = "CUSTOM_FILENAME"
        expected_filename = f"{expected_name}.{expected_file_format}"
        expected_file_path = dl_path / expected_filename
        path_is_a_file = dl_path / expected_filename

        with SAMDiagramManager(valid_sam_api_source) as diagrams:
            diagrams.load_diagrams(project_nb_5)

        downloader = SamDiagramDownloader(valid_sam_api_source, project_nb_5._id)
        diagram = get_diagrams(package)[0]
        response = downloader.download_diagram(
            diagram_id=diagram._id,
            file_format=expected_file_format,
            path=path_is_a_file,
            filename=expected_name,
        )

        response_path = Path(response)

        assert response_path == expected_file_path
        assert expected_file_path.exists()
        assert response_path.name == expected_filename

    def test_working_dowload_diagram_with_invalid_path(
        self, valid_sam_api_source: SamApiConnector, project_nb_5: Project
    ):
        package = project_nb_5.get_root_package()

        expected_file_format = "png"
        expected_name = "CUSTOM_FILENAME"
        invalid_path = ""

        with SAMDiagramManager(valid_sam_api_source) as diagrams:
            diagrams.load_diagrams(project_nb_5)

        downloader = SamDiagramDownloader(valid_sam_api_source, project_nb_5._id)
        diagram = get_diagrams(package)[0]

        with pytest.raises(DiagramConnectorException, match=r"Cannot resolve path:"):
            downloader.download_diagram(
                diagram_id=diagram._id,
                file_format=expected_file_format,
                path=invalid_path,
                filename=expected_name,
            )
