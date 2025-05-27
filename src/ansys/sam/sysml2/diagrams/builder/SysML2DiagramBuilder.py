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
"""Diagram Builder."""

from __future__ import annotations

from typing import Dict, List

from ansys.sam.sysml2 import AnsysSysML2APIConnector
from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.diagrams.builder import EMF2ObjectMapper
from ansys.sam.sysml2.diagrams.classes import UnresolvedField
from ansys.sam.sysml2.diagrams.utils import DiagramDownloader


class SysML2DiagramBuilder:
    """Diagram Builder class."""

    _mapper: EMF2ObjectMapper

    def __init__(self, connector: AnsysSysML2APIConnector):
        """
        Construct method for new instance.

        Parameters
        ----------
        connector : AnsysSysML2APIConnector
            The connector
        """
        self._connector = connector
        self._mapper = EMF2ObjectMapper()

    def build_diagrams(self, project: Project) -> Dict[str, list]:
        """
        Call API and build the project from JSON.

        Parameters
        ----------
        project : Project
            The project context

        Returns
        -------
        Dict[str, list]
            List of Diagrams
        """
        data = self._connector.get_project_data(project._id)
        diagrams_extracted = self.extract_diagrams(data)
        diagrams = self._build_diagram_elements(diagrams_extracted, project)

        for diagram_list in diagrams.values():
            for diagram in diagram_list:
                DiagramDownloader.bind_download_method(diagram, self._connector, project)

        self._update_model(project, diagrams)

    def _build_diagram_elements(self, diagrams: dict, project: Project) -> dict:
        """Build all diagrams elements.

        Parameters
        ----------
        diagrams : dict
            Diagrams retrieved from API
        project : Project
            The project context

        Returns
        -------
        dict
            Diagrams dict with element resolved
        """
        data = {}
        for id, annotations in diagrams.items():
            elements = []
            for annotation in annotations:
                mapped = self._mapper.map(annotation)
                elements.append(mapped.get_element())
                unresolved = mapped.get_unresolved_fields()
                self.__resolve_unresolved_fields(project, unresolved)
            data[id] = elements
        return data

    def __resolve_unresolved_fields(
        self, project: Project, unresolved_fields: List[UnresolvedField]
    ):
        """
        Resolve all fields.

        Parameters
        ----------
        project : Project
            The project context
        unresolved_fields : List[UnresolvedField]
            The unresolved fields
        """
        for field in unresolved_fields:
            target_id = field.get_id()
            target_data = project.find_element_by_id(target_id)

            if target_data is not None:
                field.resolve(target_data)

    def extract_diagrams(self, data: dict) -> dict:
        """
        Extract all diagrams from the model data.

        Parameters
        ----------
        data : dict
            Model data

        Returns
        -------
        dict
            All diagrams, with parents Id.
        """
        return self.filter_diagrams(self.extract_e_annotations(data))

    def extract_e_annotations(self, data: dict) -> dict:
        """
        Extract all eAnnotations of the model.

        Parameters
        ----------
        data : dict
            the model data

        Returns
        -------
        dict
            all diagrams, with container ID
        """
        diagrams = {}
        if "eAnnotations" in data:
            diagrams[data["@id"]] = data["eAnnotations"]
        if "ownedMember" in data:
            for owned_element in data["ownedMember"]:
                diagrams.update(self.extract_e_annotations(owned_element))
        return diagrams

    def filter_diagrams(self, e_annotations: dict) -> dict:
        """
        Filter given e_annotation list to keep diagrams.

        Parameters
        ----------
        e_annotations : dict
            All eAnnotations

        Returns
        -------
        dict
            Only Diagrams eAnnotation
        """
        res = {}
        for id, annotations in e_annotations.items():
            diagram_annotations = []
            for annotation in annotations[0].get("contents", []):
                if annotation.get("eClass", "").endswith("SimpleDiagram"):
                    diagram_annotations.append(annotation)
            res[id] = diagram_annotations
        return res

    def _update_model(self, model: Project, diagrams: Dict[str, dict]):
        """
        Update the model with the given diagrams.

        Parameters
        ----------
        model : Project
            The context model
        diagrams : Dict[str,dict]
            Diagrams
        """
        model.get_root_package()._observer.stop_observer()
        for id, element in diagrams.items():
            model_element = model.find_element_by_id(id)
            if model_element is not None:
                setattr(model_element, "__diagram", element)
        model.get_root_package()._observer.start_observer()
