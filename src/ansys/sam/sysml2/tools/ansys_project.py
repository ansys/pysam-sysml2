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

"""Ansys Base Project to facilitate use of PySAM SysML2 library."""

from pathlib import Path
from typing import Union

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.diagrams.api.sam_rest_api_connector import SamRestApiConnector
from ansys.sam.sysml2.diagrams.sam_diagram_manager import SAMDiagramManager
from ansys.sam.sysml2.diagrams.tools.sam_diagram_downloader import SamDiagramDownloader
from ansys.sam.sysml2.exception.connector_exception import DiagramNotAvailableException
from ansys.sam.sysml2.tools.factory import Factory


class AnsysProject:
    """Complete Ansys SysML2 project implementation with integrated capabilities."""

    _project_id: str
    _downloader: SamDiagramDownloader
    _factory: Factory

    def __init__(
        self,
        server_url: str,
        token: str,
        organization_id: str,
        project_id: str,
        use_ssl: bool = True,
    ) -> None:
        """
        Initialize the AnsysSysML2Project with connection parameters.

        Parameters
        ----------
        server_url : str
            Base URL of the SysML2 server.
        token : str
            Authentication token for API access.
        organization_id : str
            Unique identifier of the organization.
        project_id : str
            Unique identifier of the project to manage.
        use_ssl : bool, optional
            Whether to use SSL/TLS for connections. Default is True.

        Raises
        ------
        ConnectionError
            If unable to establish connection to the server.
        AuthenticationError
            If the provided token is invalid.
        ProjectNotFoundError
            If the specified project does not exist.
        """
        self._project_id = project_id
        self.__diagrams_available = False
        self._initialize_components(server_url, token, organization_id, use_ssl)

    def _initialize_components(
        self,
        server_url: str,
        token: str,
        organization_id: str,
        use_ssl: bool = True,
    ) -> None:
        """Initialize all internal components and establish connections."""
        sysml2_connector = AnsysSysML2APIConnector(
            server_url=server_url,
            organization_id=organization_id,
            token=token,
            use_ssl=use_ssl,
        )

        self.__sam_connector = SamRestApiConnector(
            server_url=server_url, token=token, use_ssl=use_ssl
        )

        project = self._get_project(sysml2_connector)

        for attr_name, attr_value in project.__dict__.items():
            if attr_name.startswith("_"):
                setattr(self, attr_name, attr_value)

        self._factory = Factory(project=self, conn=sysml2_connector)

        self._initialize_diagram_capabilities()

    def _get_project(self, sysml2_connector: AnsysSysML2APIConnector):
        """Abstract method to retrieve the correct project type."""
        return None

    def _initialize_diagram_capabilities(self) -> None:
        """Initialize diagram download capabilities with graceful error handling."""
        try:
            with SAMDiagramManager(connector=self.__sam_connector) as diagram_manager:
                diagram_manager.load_diagrams(model=self)

            self._downloader = SamDiagramDownloader(
                connector=self.__sam_connector, project_id=self._project_id
            )
            self.__diagrams_available = True
        except Exception:
            self._downloader = None
            self.__diagrams_available = False

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
        if not self.__diagrams_available:
            raise DiagramNotAvailableException(
                f"Diagram functionality not available for project {self._project_id}"
            )

        return self._downloader.download_diagram(
            diagram_id=diagram_id, file_format=file_format, path=path, filename=filename
        )

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
        DiagramNotAvailableException
            If diagram functionality is not available for this project.
        DiagramConnectorException
            If the download fails or HTTP response is not 200.
        """
        if not self.__diagrams_available:
            raise DiagramNotAvailableException(
                f"Diagram functionality not available for project {self._project_id}"
            )

        return self._downloader.download_all_diagrams(
            path=path, file_format=file_format, filename=filename
        )

    def is_diagrams_available(self) -> bool:
        """
        Check if diagram functionality is available for this project.

        Returns
        -------
        bool
            True if diagrams can be downloaded, False otherwise.
        """
        return self.__diagrams_available

    def get_project_diagrams_info(self) -> dict:
        """
        Get information about available diagrams in the project.

        Returns
        -------
        dict
            Dictionary containing diagram information.

        Raises
        ------
        DiagramNotAvailableException
            If diagram functionality is not available for this project.
        """
        if not self.__diagrams_available:
            raise DiagramNotAvailableException(
                f"Diagram functionality not available for project {self._project_id}"
            )

        return self.__sam_connector.get_diagrams_info(self._project_id)

    def get_single_diagram_info(self, diagram_id: str) -> dict:
        """
        Get information about a diagram in the project.

        Parameters
        ----------
        diagram_id: str
            ID of the diagram we want info about.

        Returns
        -------
        dict
            Dictionary containing diagram information.

        Raises
        ------
        DiagramNotAvailableException
            If diagram functionality is not available for this project.
        """
        if not self.__diagrams_available:
            raise DiagramNotAvailableException(
                f"Diagram functionality not available for project {self._project_id}"
            )

        return self.__sam_connector.get_single_diagram_info(self._project_id, diagram_id)

    @property
    def factory(self) -> Factory:
        """Getter property for factory."""
        return self._factory
