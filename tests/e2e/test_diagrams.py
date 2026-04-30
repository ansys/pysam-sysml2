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
from ansys.sam.sysml2.tools.ansys_scripting_project import AnsysScriptingProject

from .conftest import load_scripting_project


@pytest.mark.e2e
class TestDiagrams:

    def test_diagrams_available(self, connector, project_manager):
        """Load bike model via AnsysScriptingProject, verify diagrams are available."""
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
        """Load bike, load diagrams, verify diagram info is returned."""
        project = load_scripting_project(connector, project_manager, "bike")

        with SAMDiagramManager(connector=sam_connector) as diagrams:
            diagrams.load_diagrams(model=project)

        root_diagrams = getattr(project.get_root_package(), "__diagram")
        assert isinstance(root_diagrams, list)
        assert len(root_diagrams) > 0

        connector.delete_project(project._id)

    def test_download_diagram_svg(self, connector, project_manager, sam_connector, tmp_path):
        """Download a single diagram as SVG, verify file exists on disk."""
        project = load_scripting_project(connector, project_manager, "bike")

        with SAMDiagramManager(connector=sam_connector) as diagrams:
            diagrams.load_diagrams(model=project)

        first_diagram = getattr(project.get_root_package(), "__diagram")[0]
        downloader = SamDiagramDownloader(
            connector=sam_connector, project_id=project._id
        )

        result = downloader.download_diagram(
            diagram_id=first_diagram._id,
            path=str(tmp_path),
            file_format="svg",
        )
        assert Path(result).exists()

        connector.delete_project(project._id)

    def test_download_all_diagrams(self, connector, project_manager, sam_connector, tmp_path):
        """Download all diagrams as a ZIP, verify file exists."""
        project = load_scripting_project(connector, project_manager, "bike")

        downloader = SamDiagramDownloader(
            connector=sam_connector, project_id=project._id
        )
        result = downloader.download_all_diagrams(
            path=str(tmp_path), file_format="jpeg"
        )
        assert Path(result).exists()

        connector.delete_project(project._id)

    def test_diagram_navigation(self, connector, project_manager, sam_connector):
        """Navigate diagram structure, verify model_element names are populated."""
        project = load_scripting_project(connector, project_manager, "bike")

        with SAMDiagramManager(connector=sam_connector) as diagrams:
            diagrams.load_diagrams(model=project)

        root_diagrams = getattr(project.get_root_package(), "__diagram")
        first_diagram = root_diagrams[0]
        assert first_diagram._plane._model_element._name is not None

        connector.delete_project(project._id)
