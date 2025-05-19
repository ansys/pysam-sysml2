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
"""EMF2Object Mapper class."""

from typing import Dict, List

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from ansys.sam.sysml2.classes.project import Project
from ansys.sam.sysml2.diagrams.classes import DiagramElement, MappedElement, Plane, UnresolvedField
from ansys.sam.sysml2.diagrams.utils.diagram_utils import DiagramUtils

TYPE_KEY = "eClass"


class EMF2ObjectMapper:
    """EMF2ObjectMapper class for Diagram Element."""

    _connector: AnsysSysML2APIConnector
    _project: Project
    _project_id: str
    class_cache: dict

    def __init__(self):
        """Construct Method for new EMF2ObjectMapper instance."""
        self.class_cache: Dict[str, type] = {}

    def map(self, data: dict, mapped_element: DiagramElement = None) -> MappedElement:
        """
        Map the json into a Python element.

        Parameters
        ----------
        data : dict
            data
        mapped_element: DiagramElement
            mapped_element

        Returns
        -------
        MappedElement
            Mapped element
        """
        return self.__build_element(data, mapped_element)

    def __build_element(self, data: dict, element: DiagramElement = None) -> MappedElement:
        """
        Build a DiagramElement from raw data and collect unresolved references.

        Parameters
        ----------
        data : dict
            The input data for the element.
        element : DiagramElement, optional
            Optionally pre-initialized DiagramElement.

        Returns
        -------
        MappedElement
            A container with the built element and its unresolved references.
        """
        if element is None:
            element = DiagramElement(id=data["@id"])

        self.__assign_dynamic_class(element, data.get(TYPE_KEY, ""))

        unresolved_fields = self.__map_plane_if_present(data, element)
        unresolved_fields.extend(self.__add_fields(data, element))

        return MappedElement(element, unresolved_fields)

    def __assign_dynamic_class(self, element: DiagramElement, eclass: str):
        """
        Update the default Diagram definition to the corresponding Diagram Element.

        Parameters
        ----------
        element : DiagramElement
            The associated element
        eclass : str
            The name of the class
        """
        class_name = eclass.split("//")[-1] if "//" in eclass else eclass
        if class_name and class_name not in self.class_cache:
            self.class_cache[class_name] = type(class_name, (type(element),), {})
        element.__class__ = self.class_cache.get(class_name, type(element))

    def __map_plane_if_present(self, data: dict, element: DiagramElement) -> List[UnresolvedField]:
        """
        Map the 'plane' section of the data to a Plane object, extracting unresolved references.

        Parameters
        ----------
        data : dict
            The raw data potentially containing a 'plane' section.
        element : DiagramElement
            The element to which the Plane will be attached.

        Returns
        -------
        List[UnresolvedField]
            A list of unresolved references within the 'plane' section.
        """
        unresolved_fields = []

        plane_data = data.get("plane")
        if not plane_data:
            return unresolved_fields

        plane = Plane(id=plane_data.get("@id"))

        new_attr_name = DiagramUtils.to_snake_case("modelElement")
        attr_model = f"_{new_attr_name}"
        model_data = plane_data.get("modelElement", [])
        ref, unresolved = self.__extract_ref(model_data, plane, attr_model, unresolved_fields)
        setattr(plane, attr_model, ref)

        unresolved_fields.extend(unresolved)

        new_attr_owned = DiagramUtils.to_snake_case("ownedDiagramElements")
        attr_owned = f"_{new_attr_owned}"
        values, refs = self.__extract_refs(
            plane_data.get("ownedDiagramElements", []), plane, attr_owned
        )
        setattr(plane, attr_owned, values)

        unresolved_fields.extend(refs)
        element._plane = plane
        return unresolved_fields

    def __extract_ref(
        self, value: dict, owner, attr: str, unresolved_fields: List[UnresolvedField]
    ) -> tuple[str, List[UnresolvedField]]:
        """
        Extract a reference ID from a dictionary and track as unresolved.

        Parameters
        ----------
        value : dict
            The dict to inspect for a "$ref" key.
        owner
            The object owning the attribute.
        attr : str
            The name of the attribute.
        unresolved_fields : list of UnresolvedField
            The list to which unresolved fields are appended.

        Returns
        -------
        tuple[str, List[UnresolvedField]]
            The reference ID if found and the list of unresolved field,
            otherwise only the unresolved field.
        """
        if "$ref" in value:
            ref_id = value["$ref"]
            unresolved_fields.append(UnresolvedField(owner, attr, ref_id))
            return ref_id, unresolved_fields
        return None, unresolved_fields

    def __extract_refs(self, items: list, owner, attr: str) -> tuple[list, list[UnresolvedField]]:
        """
        Extract a list of references or embedded objects, and track unresolved references.

        Parameters
        ----------
        items : list
            List of items (raw values, dicts with $ref, or embedded objects).
        owner
            The owning element to which the unresolved fields are attached.
        attr : str
            Name of the attribute on the owner.

        Returns
        -------
        tuple[list, list[UnresolvedField]]
            - Resolved values (raw values, IDs, or objects)
            - List of unresolved references to be resolved later.
        """
        values = []
        unresolved = []

        for item in items:
            if isinstance(item, dict):
                if "$ref" in item:
                    ref_id = item["$ref"]
                    unresolved.append(UnresolvedField(owner, attr, ref_id))
                    values.append(ref_id)
                else:
                    mapped = self.__build_element(item)
                    values.append(mapped.get_element())
                    unresolved.extend(mapped.get_unresolved_fields())
            else:
                values.append(item)

        return values, unresolved

    def __handle_dict_field(
        self, value: dict, element: DiagramElement, attr: str
    ) -> List[UnresolvedField]:
        """
        Handle assignment of a dict field, either as a reference or nested element.

        Parameters
        ----------
        value : dict
            The dictionary value to assign.
        element : DiagramElement
            The target element.
        attr : str
            Attribute name on the element.

        Returns
        -------
        List[UnresolvedField]
            Unresolved references, if any.
        """
        unresolved_fields = []
        ref, unresolved = self.__extract_ref(value, element, attr, unresolved_fields)
        unresolved_fields.extend(unresolved)

        if ref:
            setattr(element, attr, ref)
        else:
            mapped = self.__build_element(value)
            setattr(element, attr, mapped.get_element())
            unresolved_fields.extend(mapped.get_unresolved_fields())
        return unresolved_fields

    def __handle_list_field(
        self, items: list, element: DiagramElement, attr: str
    ) -> List[UnresolvedField]:
        """
        Handle assignment of a list field, processing references and nested objects.

        Parameters
        ----------
        items : list
            List of values (strings, dicts with $ref, or nested objects).
        element : DiagramElement
            The element to assign the attribute to.
        attr : str
            The name of the attribute.

        Returns
        -------
        List[UnresolvedField]
            Unresolved references, if any.
        """
        unresolved_fields = []
        values = []

        for item in items:
            if isinstance(item, dict):
                ref, unresolved = self.__extract_ref(item, element, attr, unresolved_fields)
                unresolved_fields.extend(unresolved)
                if ref:
                    values.append(ref)
                else:
                    mapped = self.__build_element(item)
                    values.append(mapped.get_element())
                    unresolved_fields.extend(mapped.get_unresolved_fields())
            else:
                values.append(item)

        setattr(element, attr, values)
        return unresolved_fields

    def __add_fields(self, data: dict, element: DiagramElement) -> List[UnresolvedField]:
        """
        Map dynamic JSON fields to attributes on a DiagramElement.

        Parameters
        ----------
        data : dict
            The JSON data to map.
        element : DiagramElement
            The target object to which attributes are set.

        Returns
        -------
        List[UnresolvedField]
            List of unresolved references found during the mapping.
        """
        unresolved_fields = []

        for key, value in data.items():
            if key.startswith("@") or key in {"plane", TYPE_KEY}:
                continue

            new_key_name = DiagramUtils.to_snake_case(key)
            attr_name = f"_{new_key_name}"

            if isinstance(value, dict):
                unresolved_fields.extend(self.__handle_dict_field(value, element, attr_name))
            elif isinstance(value, list):
                unresolved_fields.extend(self.__handle_list_field(value, element, attr_name))
            else:
                setattr(element, attr_name, value)

        return unresolved_fields
