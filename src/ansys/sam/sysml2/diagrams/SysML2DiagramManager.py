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
"""Main class of the lib."""

from pathlib import Path
from typing import Union

from requests import RequestException

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.diagrams import AnsysRestApiConnector, DiagramDownloader, SysML2DiagramBuilder
from ansys.sam.sysml2.exception.connector_exception import (
    DiagramConnectorException,
    HTTPResponseException,
)


class SysML2DiagramManager:
    """Diagram Manager class."""

    _connector: AnsysRestApiConnector

    def __init__(self, connector: AnsysSysML2APIConnector):
        """
        Construct for new instance.

        Parameters
        ----------
        connector : AnsysRestApiConnector
            Ansys connector
        """
        self._connector = AnsysRestApiConnector(connector)

    def __enter__(self):
        """Enter method for context manager."""
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Exit method for context manager."""
        ...

    def load_diagrams(self, model: Project) -> None:
        """
        Load diagrams into a model.

        Parameters
        ----------
        model : Project
            The context model
        """
        builder = SysML2DiagramBuilder(self._connector)
        builder.build_diagrams(model)

    def download_all_diagrams(
        self,
        project: Project,
        path: Union[str, Path],
        file_format: str = "svg",
        filename: str = "",
    ) -> str:
        """
        Download all diagrams as a ZIP archive.

        Parameters
        ----------
        project : ProjectImpl
            The project instance.
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

        file_path = DiagramDownloader.resolve_file_path(path, filename)
        response = None
        try:
            response = DiagramDownloader.get_diagram_zip(self._connector, project._id, new_format)
        except RequestException as e:
            raise DiagramConnectorException from e

        if response.status_code == 200:
            DiagramDownloader.save_response_content(response, file_path)
            return file_path
        else:
            raise HTTPResponseException(response.text)
