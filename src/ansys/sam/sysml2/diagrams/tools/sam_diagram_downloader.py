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
"""Diagram downloader class for PySam Diagram library."""

from pathlib import Path
from typing import Union

from ansys.sam.sysml2.diagrams.api import SamApiConnector
from ansys.sam.sysml2.diagrams.utils import FileManager
from ansys.sam.sysml2.exception.connector_exception import DiagramConnectorException


class SamDiagramDownloader:
    """Class to manage and download diagrams."""

    def __init__(self, connector: SamApiConnector, project_id: str):
        """
        Initialize the SamDiagramDownloader.

        Parameters
        ----------
        connector : SamApiConnector
            The connector providing API access.
        project : str
            The project instance id.
        """
        self._connector = connector
        self._project_id = project_id

    def download_diagram(
        self,
        diagram_id: str,
        path: Union[str, Path],
        file_format: str = "svg",
        filename: str = "",
    ) -> str:
        """
        Download a single diagram and save it to disk.

        Parameters
        ----------
        diagram_id : str
            The diagram id to download.
        path : str or Path
            Destination file or directory.
        file_format : str
            Format of the diagram (e.g., 'svg', 'png', 'jpeg').
        filename : str, optional
            Name of the file. Default is diagram ID.

        Returns
        -------
        str
            Return the path of the file created.

        Raises
        ------
        DiagramNotAvailableException
            If diagram functionality is not available for this project.
        DiagramConnectorException
            If the download fails or HTTP response is not 200.
        """
        try:
            if file_format.lower() == "svg":
                content = self._connector.get_diagram_image_as_svg(self._project_id, diagram_id)
            elif file_format.lower() == "png":
                content = self._connector.get_diagram_image_as_png(self._project_id, diagram_id)
            elif file_format.lower() == "jpeg":
                content = self._connector.get_diagram_image_as_jpeg(self._project_id, diagram_id)
            else:
                raise DiagramConnectorException(f"Unsupported format: {file_format}")

            if not filename:
                filename = diagram_id

            file_path = FileManager.save_binary_content(content, path, filename, file_format)
            return str(file_path)

        except Exception as e:
            raise DiagramConnectorException(str(e)) from e

    def download_all_diagrams(
        self,
        path: Union[str, Path],
        file_format: str = "svg",
        filename: str = "",
    ) -> str:
        """
        Download all diagrams as a ZIP archive.

        Parameters
        ----------
        path : str or Path
            Destination directory or file path for the ZIP file.
        file_format : str, optional
            Format of the diagrams (e.g., 'png', 'jpeg', 'svg'). Default is "svg".
        filename : str, optional
            Name of the file. Default is "{Project Name}_{Image Extension}_diagrams.zip".

        Returns
        -------
        str
            Path to the saved ZIP file.

        Raises
        ------
        DiagramConnectorException
            If the download fails or HTTP response is not 200.
        """
        try:
            zip_content = self._connector.get_all_diagram_image_from_project(
                self._project_id, file_format
            )

            if not filename:
                filename = f"{self._project_id}_{file_format}_diagrams.zip"
            if not filename.lower().endswith(".zip"):
                filename += ".zip"

            file_path = FileManager.save_response_content(zip_content, path, filename)
            return str(file_path)

        except Exception as e:
            raise DiagramConnectorException(str(e)) from e
