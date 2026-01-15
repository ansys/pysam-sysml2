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
"""API connector interface utilities for SAM API operations."""

from abc import ABC, abstractmethod


class SamApiConnector(ABC):
    """Provides the SAM API connector interface."""

    @abstractmethod
    def get_project_data(self, model_id: str) -> dict:
        """Get project data from the SAM API using the project ID."""

    @abstractmethod
    def get_diagrams_info(self, project_id: str) -> dict:
        """Get metadata and information for all diagrams within a specific project."""

    @abstractmethod
    def get_single_diagram_info(self, project_id: str, diagram_id: str) -> dict:
        """
        Get detailed information for a single diagram within a project.

        Parameters
        ----------
        project_id: str
            Project ID of the project containing the diagram.
        diagram_id: str
            Diagram ID of the diagram to get information on.
        """

    @abstractmethod
    def get_diagram_image_as_svg(self, project_id: str, diagram_id: str) -> bytes:
        """
        Download a diagram rendered as SVG format.

        Parameters
        ----------
        project_id: str
            Project ID of the project containing the diagram.
        diagram_id: str
            Diagram ID of the diagram to download.
        """

    @abstractmethod
    def get_diagram_image_as_png(self, project_id: str, diagram_id: str) -> bytes:
        """
        Download a diagram rendered as PNG format.

        Parameters
        ----------
        project_id: str
            Project ID of the project containing the diagram.
        diagram_id: str
            Diagram ID of the diagram to download.
        """

    @abstractmethod
    def get_diagram_image_as_jpeg(self, project_id: str, diagram_id: str) -> bytes:
        """
        Download a diagram rendered as JPEG format.

        Parameters
        ----------
        project_id: str
            Project ID of the project containing the diagram.
        diagram_id: str
            Diagram ID of the diagram to download.
        """

    @abstractmethod
    def get_all_diagram_image_from_project(self, project_id: str, file_format: str) -> bytes:
        """
        Download all diagrams from a project as a compressed ZIP archive.

        Parameters
        ----------
        project_id: str
            Project ID of the project containing the diagram.
        file_format: str
            File format of the diagram images contained in the ZIP archive.
        """
