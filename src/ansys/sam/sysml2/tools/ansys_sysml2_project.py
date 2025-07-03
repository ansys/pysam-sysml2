# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
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
"""Ansys SysML2 Project to facilitate use of PySam library."""

from pathlib import Path
from typing import List, Optional, Set, Union

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.builder.classes.project_impl import ProjectImpl
from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.classes.sysml_element import SysMLElement
from ansys.sam.sysml2.classes.unresolved_field import UnresolvedField
from ansys.sam.sysml2.diagrams.api.sam_rest_api_connector import SamRestApiConnector
from ansys.sam.sysml2.diagrams.sam_diagram_manager import SAMDiagramManager
from ansys.sam.sysml2.diagrams.tools.sam_diagram_downloader import SamDiagramDownloader
from ansys.sam.sysml2.exception.connector_exception import DiagramNotAvailableException
from ansys.sam.sysml2.tools.factory import Factory


class AnsysSysML2Project(ProjectImpl):
    """
    Complete Ansys SysML2 project implementation with integrated capabilities.

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
    """

    _project_id: str

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
        # Store connection parameters
        self.server_url = server_url
        self.token = token
        self.organization_id = organization_id
        self._project_id = project_id
        self.use_ssl = use_ssl

        # Initialize connectors
        self._sysml2_connector: Optional[AnsysSysML2APIConnector] = None
        self._sam_connector: Optional[SamRestApiConnector] = None
        self._project_manager: Optional[SysML2ProjectManager] = None
        self._downloader: Optional[SamDiagramDownloader] = None
        self._factory: Optional[Factory] = None
        self._diagrams_available = False

        # Initialize all components
        self._initialize_components()

    def _initialize_components(self) -> None:
        """
        Initialize all internal components and establish connections.

        Raises
        ------
        ConnectionError
            If unable to establish connection to any of the services.
        ProjectNotFoundError
            If the specified project cannot be loaded.
        """
        # Initialize SysML2 API connector
        self._sysml2_connector = AnsysSysML2APIConnector(
            server_url=self.server_url,
            organization_id=self.organization_id,
            token=self.token,
            use_ssl=self.use_ssl,
        )

        # Initialize SAM API connector
        self._sam_connector = SamRestApiConnector(
            server_url=self.server_url, token=self.token, use_ssl=self.use_ssl
        )

        # Initialize project manager and load project
        self._project_manager = SysML2ProjectManager(connector=self._sysml2_connector)
        self._project = self._project_manager.get_project(self._project_id)

        # Initialize factory
        self._factory = Factory(project=self, conn=self._sysml2_connector)

        # Initialize diagram functionality with error handling
        self._initialize_diagram_capabilities()

    def _initialize_diagram_capabilities(self) -> None:
        """Initialize diagram download capabilities with graceful error handling."""
        try:
            # Initialize diagram manager
            with SAMDiagramManager(connector=self._sam_connector) as diagram_manager:
                diagram_manager.load_diagrams(model=self._project)

            # Initialize diagram downloader
            self._downloader = SamDiagramDownloader(
                connector=self._sam_connector, project_id=self._project._id
            )
            self._diagrams_available = True
        except Exception:
            print(f"No diagrams found for project {self._project_id}")
            self._downloader = None
            self._diagrams_available = False

    # === Properties to access and update project attributes ===

    @property
    def _id(self) -> str:
        """Get the project identifier."""
        return self._project._id

    @_id.setter
    def _id(self, value: str) -> None:
        """Set the project identifier."""
        self._project._id = value

    @property
    def _name(self) -> str:
        """Get the project name."""
        return self._project._name

    @_name.setter
    def _name(self, value: str) -> None:
        """Set the project name."""
        self._project._name = value

    @property
    def _env(self) -> dict:
        """Get the project environment configuration."""
        return self._project._env

    @_env.setter
    def _env(self, value: dict) -> None:
        """Set the project environment configuration."""
        self._project._env = value

    @property
    def _root(self) -> List[SysMLElement]:
        """Get the list of root SysML elements."""
        return self._project._root

    @_root.setter
    def _root(self, value: List[SysMLElement]) -> None:
        """Set the list of root SysML elements."""
        self._project._root = value

    @property
    def _unresolved_fields(self) -> List[UnresolvedField]:
        """Get the list of unresolved fields."""
        return self._project._unresolved_fields

    @_unresolved_fields.setter
    def _unresolved_fields(self, value: List[UnresolvedField]) -> None:
        """Set the list of unresolved fields."""
        self._project._unresolved_fields = value

    @property
    def _libraries_ids(self) -> Set[str]:
        """Get the set of library identifiers."""
        return self._project._libraries_ids

    @_libraries_ids.setter
    def _libraries_ids(self, value: Set[str]) -> None:
        """Set the set of library identifiers."""
        self._project._libraries_ids = value

    # === ProjectImpl methods delegation ===

    def add_element(self, element: SysMLElement):
        """Add an element to the project env."""
        return self._project.add_element(element)

    def update_unresolved_fields(self, unresolved_fields: List[UnresolvedField]):
        """Update all unresolved field."""
        return self._project.update_unresolved_fields(unresolved_fields)

    def get_root(self) -> List[SysMLElement]:
        """Return the list of root packages."""
        return self._project.get_root()

    def get_root_package(self) -> SysMLElement:
        """Return the root package."""
        return self._project.get_root_package()

    def get_name(self) -> str:
        """Getter for name."""
        return self._project.get_name()

    def find_element_by_id(self, element_id: str) -> SysMLElement:
        """Find element with id."""
        return self._project.find_element_by_id(element_id)

    def find_elements_by_name(self, elements_name: str) -> List[SysMLElement]:
        """Find all element with name."""
        return self._project.find_elements_by_name(elements_name)

    # === AnsysSysML2Project specific methods ===

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
        if not self._diagrams_available:
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
        if not self._diagrams_available:
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
        return self._diagrams_available

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
        if not self._diagrams_available:
            raise DiagramNotAvailableException(
                f"Diagram functionality not available for project {self._project_id}"
            )

        return self._sam_connector.get_diagrams_info(self._project_id)

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
        if not self._diagrams_available:
            raise DiagramNotAvailableException(
                f"Diagram functionality not available for project {self._project_id}"
            )

        return self._sam_connector.get_single_diagram_info(self._project_id, diagram_id)

    def create_element(self, element_type: str, **kwargs) -> SysMLElement:
        """
        Create a new SysML element in the project.

        Parameters
        ----------
        element_type : str
            Type of the SysML element to create.
        **kwargs
            Additional parameters for element creation.

        Returns
        -------
        SysMLElement
            The newly created SysML element instance.

        Raises
        ------
        ValueError
            If element_type is not supported or required parameters are missing.
        ConnectionError
            If unable to commit the new element to the server.
        """
        return self._factory.create_element(element_type, **kwargs)
