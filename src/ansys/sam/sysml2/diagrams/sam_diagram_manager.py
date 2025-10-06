# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
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
"""Main class of PySAM SysML2."""

from typing import Dict

from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.diagrams.api.sam_api_connector import SamApiConnector
from ansys.sam.sysml2.diagrams.builder import SamDiagramBuilder
from ansys.sam.sysml2.exception.connector_exception import DiagramNotAvailableException


class SAMDiagramManager:
    """Provides the SAM Diagram Manager."""

    _connector: SamApiConnector

    def __init__(self, connector: SamApiConnector):
        """Construct a new instance."""
        self._connector = connector

    def __enter__(self):
        """Enter method for context manager."""
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Exit method for context manager."""
        ...

    def load_diagrams(self, model: Project) -> None:
        """Load diagrams into a model."""
        builder = SamDiagramBuilder(self._connector)
        diagrams = builder.extract_and_build_diagrams(model)
        if diagrams == {}:
            raise DiagramNotAvailableException(
                f"Diagram functionality is not available for project {model._id}."
            )
        self._update_model(model, diagrams)

    def _update_model(self, model: Project, diagrams: Dict[str, dict]):
        """
        Update the model with the given diagrams.

        Parameters
        ----------
        model : Project
            Context model
        diagrams : Dict[str,dict]
            Diagrams
        """
        model.get_root_package()._observer.stop_observer()
        for id, element in diagrams.items():
            model_element = model.find_element_by_id(id)
            if model_element is not None:
                setattr(model_element, "__diagram", element)
        model.get_root_package()._observer.start_observer()
