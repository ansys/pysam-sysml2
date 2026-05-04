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

from ansys.sam.sysml2.diagrams.sam_diagram_manager import SAMDiagramManager
from ansys.sam.sysml2.diagrams.tools.sam_diagram_downloader import SamDiagramDownloader
from ansys.sam.sysml2.exception.connector_exception import (
    ConnectorConnectionException,
    DiagramConnectorException,
)
from ansys.sam.sysml2.tools.ansys_scripting_project import AnsysScriptingProject

from .conftest import load_scripting_project


def _get_diagrams(element):
    return getattr(element, "__diagram")


def _bike_with_loaded_diagrams(connector, project_manager, sam_connector):
    project = load_scripting_project(connector, project_manager, "bike")
    with SAMDiagramManager(connector=sam_connector) as diagrams:
        diagrams.load_diagrams(model=project)
    return project


@pytest.mark.e2e
class TestDiagrams:

    def test_diagrams_available(self, connector, project_manager):
        project = load_scripting_project(connector, project_manager, "bike")
        project_id = project._id

        ansys_project = AnsysScriptingProject(
            server_url=os.environ["SAM_SERVER_URL"],
            organization_id=os.environ["SAM_ORGANIZATION_ID"],
            token=os.environ["SAM_TOKEN"],
            use_ssl=os.environ.get("SAM_USE_SSL", "true").lower() == "true",
            project_id=project_id,
        )

        assert ansys_project.is_diagrams_available()

        connector.delete_project(project_id)

    def test_diagrams_info(self, connector, project_manager, sam_connector):
        project = _bike_with_loaded_diagrams(connector, project_manager, sam_connector)

        root_diagrams = _get_diagrams(project.get_root_package())
        assert isinstance(root_diagrams, list)
        assert len(root_diagrams) == 1

        connector.delete_project(project._id)

    def test_diagram_navigation(self, connector, project_manager, sam_connector):
        project = _bike_with_loaded_diagrams(connector, project_manager, sam_connector)

        first_diagram = _get_diagrams(project.get_root_package())[0]
        assert first_diagram._plane._model_element._name is not None

        connector.delete_project(project._id)


@pytest.mark.e2e
class TestSAMDiagramManager:

    def test_load_diagrams(self, connector, project_manager, sam_connector):
        project = _bike_with_loaded_diagrams(connector, project_manager, sam_connector)

        package = project.get_root_package()
        bike = package.Bike
        assert len(_get_diagrams(package)) == 1
        assert len(_get_diagrams(bike)) == 1

        diagram = _get_diagrams(package)[0]
        diagram_bike = _get_diagrams(bike)[0]
        assert hasattr(diagram, "_name")
        assert hasattr(diagram_bike, "_name")
        assert diagram._name == "general diagram"
        assert diagram_bike._name == "general diagram"

        connector.delete_project(project._id)

    def test_navigation_through_diagrams(self, connector, project_manager, sam_connector):
        project = _bike_with_loaded_diagrams(connector, project_manager, sam_connector)

        package = project.get_root_package()
        diagram = _get_diagrams(package)[0]
        owned = diagram._plane._owned_diagram_elements
        assert len(owned) == 10

        simple_nodes = [x for x in owned if x.__class__.__name__ == "SimpleNode"]
        assert len(simple_nodes) == 5
        for node in simple_nodes:
            assert hasattr(node, "_model_element")

        connector.delete_project(project._id)

    def test_points_correctly_typed(self, connector, project_manager, sam_connector):
        project = _bike_with_loaded_diagrams(connector, project_manager, sam_connector)

        package = project.get_root_package()
        diagram = _get_diagrams(package)[0]
        owned = diagram._plane._owned_diagram_elements

        path_elements = [x for x in owned if x.__class__.__name__ == "Path"]
        assert len(path_elements) > 0

        point_elements = []
        for path in path_elements:
            if hasattr(path, "_points") and path._points:
                point_elements.extend(path._points)
        assert len(point_elements) > 0
        actual_points = [p for p in point_elements if p.__class__.__name__ == "Point"]
        assert len(actual_points) > 0

        connector.delete_project(project._id)


@pytest.mark.e2e
class TestSamRestApiConnector:

    def test_get_project_data(self, connector, project_manager, sam_connector):
        project = load_scripting_project(connector, project_manager, "bike")

        data = sam_connector.get_project_data(project._id)
        assert len(data) > 0
        assert "eClass" in data

        connector.delete_project(project._id)

    def test_get_diagrams_info(self, connector, project_manager, sam_connector):
        project = load_scripting_project(connector, project_manager, "bike")

        diagrams_info = sam_connector.get_diagrams_info(project._id)
        assert len(diagrams_info) == 4
        assert diagrams_info[0]["name"] == "Bike"

        connector.delete_project(project._id)

    def test_get_single_diagram_info(self, connector, project_manager, sam_connector):
        project = load_scripting_project(connector, project_manager, "bike")

        diagrams_info = sam_connector.get_diagrams_info(project._id)
        bike_entry = next(d for d in diagrams_info if d["name"] == "Bike")
        diagram_id = bike_entry["diagramId"]

        info = sam_connector.get_single_diagram_info(project._id, diagram_id)
        assert isinstance(info, dict)
        assert info["name"] == "Bike"
        assert info["diagramId"] == diagram_id

        connector.delete_project(project._id)

    def test_get_single_diagram_info_unknown(
        self, connector, project_manager, sam_connector
    ):
        project = load_scripting_project(connector, project_manager, "bike")

        with pytest.raises(ConnectorConnectionException):
            sam_connector.get_single_diagram_info(project._id, "unknown")

        connector.delete_project(project._id)


@pytest.mark.e2e
class TestSamDiagramDownloader:

    @pytest.mark.parametrize(
        "file_format,suffix",
        [("svg", ".svg"), ("png", ".png"), ("jpeg", ".jpeg")],
    )
    def test_download_diagram_per_format(
        self, connector, project_manager, sam_connector, tmp_path, file_format, suffix
    ):
        project = _bike_with_loaded_diagrams(connector, project_manager, sam_connector)

        diagram = _get_diagrams(project.get_root_package())[0]
        downloader = SamDiagramDownloader(
            connector=sam_connector, project_id=project._id
        )
        result = downloader.download_diagram(
            diagram_id=diagram._id, path=str(tmp_path), file_format=file_format
        )
        result_path = Path(result)
        assert result_path.exists()
        assert result.endswith(suffix)
        assert result_path.stat().st_size > 0

        connector.delete_project(project._id)

    @pytest.mark.parametrize("file_format", ["svg", "png", "jpeg"])
    def test_download_all_diagrams_per_format(
        self, connector, project_manager, sam_connector, tmp_path, file_format
    ):
        project = load_scripting_project(connector, project_manager, "bike")

        downloader = SamDiagramDownloader(
            connector=sam_connector, project_id=project._id
        )
        result = downloader.download_all_diagrams(
            path=str(tmp_path), file_format=file_format
        )
        result_path = Path(result)
        assert result_path.exists()
        assert result.endswith(".zip")
        assert result_path.stat().st_size > 0

        connector.delete_project(project._id)

    def test_download_wrong_format(
        self, connector, project_manager, sam_connector, tmp_path
    ):
        project = _bike_with_loaded_diagrams(connector, project_manager, sam_connector)

        diagram = _get_diagrams(project.get_root_package())[0]
        downloader = SamDiagramDownloader(
            connector=sam_connector, project_id=project._id
        )
        with pytest.raises(DiagramConnectorException):
            downloader.download_diagram(
                diagram_id=diagram._id,
                file_format="WRONG_FORMAT",
                path=str(tmp_path),
            )

        connector.delete_project(project._id)

    def test_download_invalid_path(
        self, connector, project_manager, sam_connector
    ):
        project = _bike_with_loaded_diagrams(connector, project_manager, sam_connector)

        diagram = _get_diagrams(project.get_root_package())[0]
        downloader = SamDiagramDownloader(
            connector=sam_connector, project_id=project._id
        )
        with pytest.raises(DiagramConnectorException):
            downloader.download_diagram(
                diagram_id=diagram._id,
                file_format="png",
                path="",
                filename="test",
            )

        connector.delete_project(project._id)
