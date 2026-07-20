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

"""E2E tests for diagram operations using the bike model."""

import os
from pathlib import Path

import pytest

from ansys.sam.sysml2.diagrams.tools.sam_diagram_downloader import SamDiagramDownloader
from ansys.sam.sysml2.exception.connector_exception import DiagramConnectorException
from ansys.sam.sysml2.tools.ansys_scripting_project import AnsysScriptingProject


@pytest.mark.e2e
class TestDiagrams:

    def test_diagrams_available(self, project_factory):
        project = project_factory(model="bike", kind="scripting")

        ansys_project = AnsysScriptingProject(
            server_url=os.environ["SAM_SERVER_URL"],
            organization_id=os.environ["SAM_ORGANIZATION_ID"],
            token=os.environ["SAM_TOKEN"],
            use_ssl=os.environ.get("SAM_USE_SSL", "true").lower() == "true",
            project_id=project.get_id(),
        )

        assert ansys_project.is_diagrams_available()


@pytest.mark.e2e
class TestSamApiConnector:

    def test_get_diagrams_info(self, sam_connector, project_factory):
        project = project_factory(model="bike", kind="scripting")

        diagrams_info = sam_connector.get_diagrams_info(project.get_id())

        assert len(diagrams_info) == 4
        assert diagrams_info[0]["name"] == "Bike"

    def test_get_single_diagram_info(self, sam_connector, project_factory):
        project = project_factory(model="bike", kind="scripting")

        diagrams_info = sam_connector.get_diagrams_info(project.get_id())
        bike_entry = next(d for d in diagrams_info if d["name"] == "Bike")
        diagram_id = bike_entry["diagramId"]
        info = sam_connector.get_single_diagram_info(project.get_id(), diagram_id)

        assert isinstance(info, dict)
        assert info["name"] == "Bike"
        assert info["diagramId"] == diagram_id

    def test_get_single_diagram_info_unknown(self, sam_connector, project_factory):
        project = project_factory(model="bike", kind="scripting")

        with pytest.raises(DiagramConnectorException):
            sam_connector.get_single_diagram_info(project.get_id(), "unknown")


@pytest.mark.e2e
class TestSamDiagramDownloader:

    @pytest.mark.parametrize(
        "file_format,suffix",
        [("svg", ".svg"), ("png", ".png"), ("jpeg", ".jpeg")],
    )
    def test_download_diagram_per_format(
        self, sam_connector, project_factory, tmp_path, file_format, suffix
    ):
        project = project_factory(model="bike", kind="scripting")

        diagram_id = sam_connector.get_diagrams_info(project.get_id())[0]["diagramId"]
        downloader = SamDiagramDownloader(
            connector=sam_connector, project_id=project.get_id()
        )
        result = downloader.download_diagram(
            diagram_id=diagram_id, path=str(tmp_path), file_format=file_format
        )
        result_path = Path(result)

        assert result_path.exists()
        assert result.endswith(suffix)
        assert result_path.stat().st_size > 0

    @pytest.mark.parametrize("file_format", ["svg", "png", "jpeg"])
    def test_download_all_diagrams_per_format(
        self, sam_connector, project_factory, tmp_path, file_format
    ):
        project = project_factory(model="bike", kind="scripting")

        downloader = SamDiagramDownloader(
            connector=sam_connector, project_id=project.get_id()
        )
        result = downloader.download_all_diagrams(
            path=str(tmp_path), file_format=file_format
        )
        result_path = Path(result)

        assert result_path.exists()
        assert result.endswith(".zip")
        assert result_path.stat().st_size > 0

    def test_download_wrong_format(self, sam_connector, project_factory, tmp_path):
        project = project_factory(model="bike", kind="scripting")

        diagram_id = sam_connector.get_diagrams_info(project.get_id())[0]["diagramId"]
        downloader = SamDiagramDownloader(
            connector=sam_connector, project_id=project.get_id()
        )

        with pytest.raises(DiagramConnectorException):
            downloader.download_diagram(
                diagram_id=diagram_id,
                file_format="WRONG_FORMAT",
                path=str(tmp_path),
            )

    def test_download_invalid_path(self, sam_connector, project_factory):
        project = project_factory(model="bike", kind="scripting")

        diagram_id = sam_connector.get_diagrams_info(project.get_id())[0]["diagramId"]
        downloader = SamDiagramDownloader(
            connector=sam_connector, project_id=project.get_id()
        )

        with pytest.raises(DiagramConnectorException):
            downloader.download_diagram(
                diagram_id=diagram_id,
                file_format="png",
                path="",
                filename="test",
            )
