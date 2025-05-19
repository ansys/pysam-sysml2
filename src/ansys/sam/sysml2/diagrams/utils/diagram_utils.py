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
"""Diagram utils class for PySam Diagram library."""

from pathlib import Path
import re
from typing import Union

import requests

from ansys.sam.sysml2 import AnsysSysML2APIConnector
from ansys.sam.sysml2.builder.classes.project_impl import ProjectImpl
from ansys.sam.sysml2.diagrams.classes import DiagramElement


def bind_download_method(diagram: DiagramElement, manager, project: ProjectImpl):
    """
    Bind utility methods to a single diagram instance.

    Parameters
    ----------
    diagram : Diagram
        The diagram instance to bind methods to.
    manager : SysML2DiagramManager
        The manager providing API access.
    project: ProjectImpl
        The project the diagram belongs to.
    """
    utils = DiagramUtils()

    def download_all_diagrams_bound(path, file_format="svg", filename=""):
        return utils.download_all_diagrams(
            project=project,
            connector=manager._connector,
            path=path,
            file_format=file_format,
            filename=filename,
        )

    setattr(manager, "download_all_diagrams", download_all_diagrams_bound)

    def download_diagram_bound(file_format, path):
        return utils.download_diagram(
            connector=manager._connector,
            project_id=project._id,
            diagram_id=diagram._id,
            file_format=file_format,
            output_path=path,
        )

    setattr(diagram, "download_diagram", download_diagram_bound)

    def get_content_bound(file_format):
        return utils.get_content_from_api(
            connector=manager._connector,
            project_id=project._id,
            diagram_id=diagram._id,
            file_format=file_format,
        )

    setattr(diagram, "get_content", get_content_bound)


class DiagramUtils:
    """Class to manipulate and retrieve diagrams."""

    def download_all_diagrams(
        self,
        project: ProjectImpl,
        connector: AnsysSysML2APIConnector,
        path: Union[str, Path],
        file_format: str = "svg",
        filename: str = "",
    ) -> dict:
        """
        Download all diagrams as a ZIP archive.

        Parameters
        ----------
        project : ProjectImpl
            The project instance.
        connector: AnsysSysML2APIConnector
            Connector instance providing access to the API.
        path : str or Path
            Destination directory or file path for the ZIP file.
        file_format : str, optional: default = "svg"
            Format of the diagrams (e.g., 'png', 'jpg', 'svg').
        filename : str, optional: default = "{Project Name}_{Image Extension}_diagrams.zip"
            Name of the file.

        Returns
        -------
        dict
            Result of the operation with status and message.
        """
        new_format = file_format
        if file_format == "jpeg":
            new_format = "jpg"
        if filename == "":
            filename = f"{project.get_name()}_{file_format}_diagrams.zip"

        try:
            file_path = self.__resolve_file_path(path, filename)
            response = self.__get_diagram_zip(connector, project._id, new_format)

            if response.status_code == 200:
                self.__save_response_content(response, file_path)
                return {"status": "success", "message": f"File saved to {file_path}"}
            else:
                return {
                    "status": "error",
                    "message": f"Download failed: {response.status_code} - {response.text}",
                }
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def download_diagram(
        self,
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
            content = self.get_content_from_api(connector, project_id, diagram_id, file_format)
            saved_path = self.save_content(content, output_path, diagram_id, file_format)
            return {"status": "success", "message": f"File saved to {saved_path}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def get_content_from_api(
        self, connector: AnsysSysML2APIConnector, project_id: str, diagram_id: str, file_format: str
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

    def save_content(
        self, content: bytes, path: Union[str, Path], filename: str, file_format: str
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
        file_path = self.__resolve_file_path(path, filename)
        self.__ensure_directory_exists(file_path.parent)
        with file_path.open("wb") as f:
            f.write(content)
        return file_path

    @staticmethod
    def __get_diagram_zip(
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

    def __resolve_file_path(self, path: Union[str, Path], filename: str) -> Path:
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
            self.__ensure_directory_exists(path)
            return path / filename
        return path

    @staticmethod
    def __ensure_directory_exists(directory_path: Path) -> None:
        """
        Ensure that a directory exists; create it if needed.

        Parameters
        ----------
        directory_path : Path
            Directory to check or create.
        """
        directory_path.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def __save_response_content(response: requests.Response, file_path: Path) -> None:
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

    @staticmethod
    def to_snake_case(name: str) -> str:
        """
        Convert a camelCase or PascalCase string to snake_case.

        Parameters
        ----------
        name : str
            The name to convert.

        Returns
        -------
        str
            The converted snake_case string.
        """
        return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()
