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

"""Unit tests for diagram element download using MockedSamApiConnector."""

from pathlib import Path

import pytest

from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.classes.scripting_project import ScriptingProject
from ansys.sam.sysml2.diagrams.sam_diagram_manager import SAMDiagramManager
from ansys.sam.sysml2.diagrams.tools.sam_diagram_downloader import SamDiagramDownloader
from ansys.sam.sysml2.exception.connector_exception import DiagramConnectorException
from tests.unit.const import PROJECT_ID_5


def get_diagrams(element):
    return element.__diagram


class TestDiagramElement:

    @pytest.fixture
    def project_5(self, connector) -> ScriptingProject:
        manager = SysML2ProjectManager(connector)
        return manager.get_scripting_project(PROJECT_ID_5)

    @pytest.fixture
    def loaded_project(self, sam_connector, project_5):
        with SAMDiagramManager(sam_connector) as diagrams:
            diagrams.load_diagrams(project_5)
        return project_5

    def test_download_diagram_svg(self, sam_connector, loaded_project, tmp_path):
        package = loaded_project.get_root_package()
        diagram = get_diagrams(package)[0]
        downloader = SamDiagramDownloader(sam_connector, loaded_project._id)
        result = downloader.download_diagram(
            diagram_id=diagram._id, file_format="svg", path=tmp_path
        )
        assert Path(result).exists()
        assert result.endswith(".svg")

    def test_download_diagram_png(self, sam_connector, loaded_project, tmp_path):
        package = loaded_project.get_root_package()
        diagram = get_diagrams(package)[0]
        downloader = SamDiagramDownloader(sam_connector, loaded_project._id)
        result = downloader.download_diagram(
            diagram_id=diagram._id, file_format="png", path=tmp_path
        )
        assert Path(result).exists()
        assert result.endswith(".png")

    def test_download_diagram_jpeg(self, sam_connector, loaded_project, tmp_path):
        package = loaded_project.get_root_package()
        diagram = get_diagrams(package)[0]
        downloader = SamDiagramDownloader(sam_connector, loaded_project._id)
        result = downloader.download_diagram(
            diagram_id=diagram._id, file_format="jpeg", path=tmp_path
        )
        assert Path(result).exists()
        assert result.endswith(".jpeg")

    def test_download_wrong_format(self, sam_connector, loaded_project, tmp_path):
        package = loaded_project.get_root_package()
        diagram = get_diagrams(package)[0]
        downloader = SamDiagramDownloader(sam_connector, loaded_project._id)
        with pytest.raises(DiagramConnectorException):
            downloader.download_diagram(
                diagram_id=diagram._id,
                file_format="WRONG_FORMAT",
                path=tmp_path,
            )

    def test_download_invalid_path(self, sam_connector, loaded_project):
        package = loaded_project.get_root_package()
        diagram = get_diagrams(package)[0]
        downloader = SamDiagramDownloader(sam_connector, loaded_project._id)
        with pytest.raises(DiagramConnectorException):
            downloader.download_diagram(
                diagram_id=diagram._id,
                file_format="png",
                path="",
                filename="test",
            )

    def test_download_all_diagrams(self, sam_connector, loaded_project, tmp_path):
        downloader = SamDiagramDownloader(sam_connector, loaded_project._id)
        result = downloader.download_all_diagrams(path=tmp_path)
        assert Path(result).exists()
        assert result.endswith(".zip")
