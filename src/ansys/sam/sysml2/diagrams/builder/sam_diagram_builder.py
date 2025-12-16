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
"""Diagram builder."""

from typing import List

from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.diagrams.api import SamApiConnector
from ansys.sam.sysml2.diagrams.builder import EMFJSONMapper
from ansys.sam.sysml2.diagrams.classes import UnresolvedField


class SamDiagramBuilder:
    """Provides the diagram builder with integrated extraction capabilities."""

    _mapper: EMFJSONMapper

    def __init__(self, connector: SamApiConnector):
        """Construct a new instance with the SAM API Connector instance specified."""
        self._connector = connector
        self._mapper = EMFJSONMapper()

    def extract_and_build_diagrams(self, project: Project) -> dict:
        """Extract and build all diagrams from a project."""
        data = self._connector.get_project_data(project._id)
        diagrams_extracted = self.__extract_diagrams(data)
        return self.__build_diagrams(diagrams_extracted, project)

    def __extract_diagrams(self, data: dict) -> dict:
        """Extract all diagrams from the model data."""
        return self.__filter_diagrams(self.__extract_e_annotations(data))

    def __build_diagrams(self, diagrams_extracted: dict, project: Project) -> dict:
        """
        Build all diagram elements from extracted annotations.

        Parameters
        ----------
        diagrams_extracted : dict
            Dictionary mapping diagram IDs to their annotation lists.
        project : Project
            Project instance used for resolving unresolved fields.

        Returns
        -------
        dict
            Dictionary mapping diagram IDs to their built element lists.
        """
        data = {}
        for id, annotations in diagrams_extracted.items():
            elements = []
            for annotation in annotations:
                mapped = self._mapper.map(annotation)
                elements.append(mapped.get_element())
                unresolved = mapped.get_unresolved_fields()
                self.__resolve_unresolved_fields(project, unresolved)
            data[id] = elements
        return data

    def __extract_e_annotations(self, data: dict) -> dict:
        """
        Extract all eAnnotations of the model.

        Parameters
        ----------
        data : dict
            Model data.

        Returns
        -------
        dict
            All diagrams, with container ID.
        """
        diagrams = {}
        if "eAnnotations" in data:
            diagrams[data["@id"]] = data["eAnnotations"]
        if "ownedMember" in data:
            for owned_element in data["ownedMember"]:
                diagrams.update(self.__extract_e_annotations(owned_element))
        return diagrams

    def __filter_diagrams(self, e_annotations: dict) -> dict:
        """
        Filter a given eAnnotations list to keep diagrams.

        Parameters
        ----------
        e_annotations : dict
            All eAnnotations

        Returns
        -------
        dict
            Only diagram eAnnotations.
        """
        res = {}
        for id, annotations in e_annotations.items():
            diagram_annotations = []
            for annotation in annotations[0].get("contents", []):
                if annotation.get("eClass", "").endswith("SimpleDiagram"):
                    diagram_annotations.append(annotation)
            res[id] = diagram_annotations
        return res

    def __resolve_unresolved_fields(
        self, project: Project, unresolved_fields: List[UnresolvedField]
    ):
        """
        Resolve all fields.

        Parameters
        ----------
        project : Project
            Project context
        unresolved_fields : List[UnresolvedField]
            Unresolved fields.
        """
        for field in unresolved_fields:
            target_id = field.get_id()
            target_data = project.find_element_by_id(target_id)

            if target_data is not None:
                field.resolve(target_data)
