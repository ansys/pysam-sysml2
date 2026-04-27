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

"""Mocked SAM API connector returning canned JSON from modeltestset/project_5/."""

import json
from pathlib import Path

from ansys.sam.sysml2.diagrams.api.sam_api_connector import SamApiConnector
from ansys.sam.sysml2.exception.connector_exception import ConnectorConnectionException

MODELTESTSET = Path(__file__).resolve().parent / "modeltestset"


class _FakeStreamResponse:
    """Mimics requests.Response for streaming downloads."""

    def __init__(self, content: bytes):
        self._content = content

    def iter_content(self, chunk_size=8192):
        for i in range(0, len(self._content), chunk_size):
            yield self._content[i : i + chunk_size]


class MockedSamApiConnector(SamApiConnector):
    """Returns canned diagram-related JSON from modeltestset/ fixtures."""

    def get_project_data(self, model_id: str) -> dict:
        """Get project REST data."""
        api_rest_file = MODELTESTSET / f"project_{model_id}" / "api_rest.json"
        if not api_rest_file.exists():
            raise ConnectorConnectionException(
                f"No REST data for project {model_id}"
            )
        return json.loads(api_rest_file.read_text(encoding="utf-8"))

    def get_diagrams_info(self, project_id: str) -> dict:
        """Get diagrams info."""
        diagrams_file = MODELTESTSET / f"project_{project_id}" / "diagrams.json"
        if not diagrams_file.exists():
            raise ConnectorConnectionException(
                f"No diagrams data for project {project_id}"
            )
        return json.loads(diagrams_file.read_text(encoding="utf-8"))

    def get_single_diagram_info(self, project_id: str, diagram_id: str) -> dict:
        """Get single diagram info."""
        info_file = (
            MODELTESTSET
            / f"project_{project_id}"
            / f"{diagram_id}_diagram_info.json"
        )
        if not info_file.exists():
            raise ConnectorConnectionException(
                f"Diagram {diagram_id} not found in project {project_id}"
            )
        return json.loads(info_file.read_text(encoding="utf-8"))

    def get_diagram_image_as_svg(self, project_id: str, diagram_id: str) -> bytes:
        """Return stub SVG bytes."""
        return b"<svg>stub</svg>"

    def get_diagram_image_as_png(self, project_id: str, diagram_id: str) -> bytes:
        """Return stub PNG bytes."""
        return b"\x89PNG\r\n\x1a\nstub"

    def get_diagram_image_as_jpeg(self, project_id: str, diagram_id: str) -> bytes:
        """Return stub JPEG bytes."""
        return b"\xff\xd8\xff\xe0stub"

    def get_all_diagram_image_from_project(
        self, project_id: str, file_format: str
    ):
        """Return a stream-like response wrapping stub ZIP bytes."""
        nb_file = MODELTESTSET / f"project_{project_id}" / "number_of_diagrams.txt"
        if not nb_file.exists():
            raise ConnectorConnectionException(
                f"No diagram data for project {project_id}"
            )
        nb = int(nb_file.read_text(encoding="utf-8").strip())
        summary = json.dumps({
            "success": 200,
            "project_id": project_id,
            "number_diagrams": nb,
            "file_format": file_format,
        })
        return _FakeStreamResponse(summary.encode("utf-8"))
