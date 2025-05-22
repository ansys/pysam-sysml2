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

import requests

from ansys.sam.sysml2 import AnsysSysML2APIConnector
from ansys.sam.sysml2.builder.classes.project_impl import ProjectImpl
from ansys.sam.sysml2.diagrams.classes import DiagramElement


class DiagramDownloader:
    """Class to manipulate and download diagrams."""

    @staticmethod
    def bind_download_method(
        diagram: DiagramElement, connector: AnsysSysML2APIConnector, project: ProjectImpl
    ):
        """
        Bind utility methods to a single diagram instance.

        Parameters
        ----------
        diagram : Diagram
            The diagram instance to bind methods to.
        connector : AnsysSysML2APIConnector
            The connector providing API access.
        project: ProjectImpl
            The project the diagram belongs to.
        """
        setattr(
            diagram,
            "download_diagram",
            lambda file_format, path: DiagramDownloader.download_diagram(
                connector=connector,
                project_id=project._id,
                diagram_id=diagram._id,
                file_format=file_format,
                output_path=path,
            ),
        )

        setattr(
            diagram,
            "get_content",
            lambda file_format: DiagramDownloader.get_content_from_api(
                connector=connector,
                project_id=project._id,
                diagram_id=diagram._id,
                file_format=file_format,
            ),
        )

    @staticmethod
    def download_diagram(
        connector: AnsysSysML2APIConnector,
        project_id: str,
        diagram_id: str,
        file_format: str,
        output_path: Union[str, Path],
    ) -> dict:
        """
        Download a single diagram and save it to disk.

        Parameters
        ----------
        connector: AnsysSysML2APIConnector
            Connector instance providing access to the API.
        project_id : str
            ID of the project the diagram belongs to.
        diagram_id : str
            ID of the diagram to download.
        file_format : str
            Format of the diagram (e.g., 'svg', 'png').
        output_path : str or Path
            Destination file or directory.

        Returns
        -------
        dict
            Result of the operation with status and message.
        """
        try:
            content = DiagramDownloader.get_content_from_api(
                connector, project_id, diagram_id, file_format
            )
            saved_path = DiagramDownloader.save_content(
                content, output_path, diagram_id, file_format
            )
            return {"status": "success", "message": f"File saved to {saved_path}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    @staticmethod
    def get_content_from_api(
        connector: AnsysSysML2APIConnector, project_id: str, diagram_id: str, file_format: str
    ) -> bytes:
        """
        Fetch a diagram as binary content in a specified format.

        Parameters
        ----------
        connector: AnsysSysML2APIConnector
            Connector instance for API access.
        project_id : str
            ID of the project.
        diagram_id : str
            ID of the diagram.
        file_format : str
            Desired image format (e.g., 'svg', 'png').

        Returns
        -------
        bytes
            Binary content of the diagram file.
        """
        url = (
            f"{connector._server_url}/api/projects/{project_id}/diagrams/{diagram_id}/{file_format}"
        )
        headers = {"Authorization": f"Bearer {connector._token}"}
        response = requests.get(url, headers=headers, verify=connector._use_ssl)
        response.raise_for_status()
        return response.content

    @staticmethod
    def save_content(
        content: bytes, path: Union[str, Path], filename: str, file_format: str
    ) -> Path:
        """
        Save binary content to a file.

        Parameters
        ----------
        content : bytes
            The binary content to write.
        path : str or Path
            Path to a file or directory.
        filename : str
            Name of the file to be saved.

        Returns
        -------
        Path
            Path where the file was saved.
        """
        filename = f"{filename}.{file_format}"
        file_path = DiagramDownloader.resolve_file_path(path, filename)
        DiagramDownloader.ensure_directory_exists(file_path.parent)
        with file_path.open("wb") as f:
            f.write(content)
        return file_path

    @staticmethod
    def get_diagram_zip(
        connector: AnsysSysML2APIConnector, project_id: str, file_format: str
    ) -> requests.Response:
        """
        Retrieve all diagrams of a project as a ZIP file.

        Parameters
        ----------
        connector: AnsysSysML2APIConnector
            Connector instance for API access.
        project_id : str
            ID of the project.
        file_format : str
            Format of the diagrams.

        Returns
        -------
        requests.Response
            The response object from the GET request.
        """
        url = f"{connector._server_url}/api/projects/{project_id}/diagrams/all/{file_format}"
        headers = {"Authorization": f"Bearer {connector._token}"}
        return requests.get(url, headers=headers, verify=connector._use_ssl, stream=True)

    @staticmethod
    def resolve_file_path(path: Union[str, Path], filename: str) -> Path:
        """
        Resolve a valid file path from the given path and default filename.

        Parameters
        ----------
        path : str or Path
            A directory or file path.
        filename : str
            Default filename if path is a directory.

        Returns
        -------
        Path
            Resolved file path.
        """
        path = Path(path)
        if path.is_dir() or (not path.suffix and not path.exists()):
            DiagramDownloader.ensure_directory_exists(path)
            return path / filename
        return path

    @staticmethod
    def ensure_directory_exists(directory_path: Path) -> None:
        """
        Ensure that a directory exists; create it if needed.

        Parameters
        ----------
        directory_path : Path
            Directory to check or create.
        """
        directory_path.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def save_response_content(response: requests.Response, file_path: Path) -> None:
        """
        Write streamed response content to a file.

        Parameters
        ----------
        response : requests.Response
            Response object containing streamed data.
        file_path : Path
            Path to the file where content should be saved.
        """
        with file_path.open("wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
