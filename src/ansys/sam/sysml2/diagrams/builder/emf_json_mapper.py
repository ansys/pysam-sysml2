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
"""EMFJSON mapper class."""

from typing import Dict, List, Tuple, Union

from ansys.sam.sysml2.classes.scripting_project import ScriptingProject
from ansys.sam.sysml2.diagrams.classes import (
    DiagramElement,
    MappedElement,
    Plane,
    UnresolvedField,
)
from ansys.sam.sysml2.exception.mapper_exception import (
    InvalidProjectJSONMapperException,
)

TYPE_KEY = "eClass"


class EMFJSONMapper:
    """Provides the EMFJSON mapper for a diagram element."""

    _project: ScriptingProject
    _project_id: str
    class_cache: dict

    def __init__(self):
        """Construct a new instance."""
        self.class_cache: Dict[str, type] = {}

    def map(self, data: dict) -> MappedElement:
        """
        Convert JSON-like dictionary data into a diagram element.

        Parameters
        ----------
        data : dict
            Input JSON data representing the element to map.

        Returns
        -------
        MappedElement
            Object containing the mapped diagram element and any unresolved references.
        """
        if "@id" not in data:
            raise InvalidProjectJSONMapperException("Not valid JSON-like dictionary data.")

        return self.__build_element(data)

    def __build_element(self, data: dict) -> MappedElement:
        """Core implementation for mapping data into a diagram element."""
        eclass = data.get(TYPE_KEY, None)

        element = DiagramElement(element_id=data["@id"])

        if eclass is not None:
            self.__assign_dynamic_class(element, eclass)

        unresolved_fields = self.__map_plane_if_present(data, element)
        unresolved_fields.extend(self.__add_fields(data, element))

        return MappedElement(element, unresolved_fields)

    def __assign_dynamic_class(self, element: DiagramElement, eclass: str):
        """
        Assign a dynamic class to the element based on the provided class name.

        Parameters
        ----------
        element : DiagramElement
            Element whose class is to be updated.
        eclass : str
            Class name string, possibly namespaced (for example, containing "//").
        """
        class_name = eclass.split("//")[-1] if "//" in eclass else eclass
        if class_name and class_name not in self.class_cache:
            self.class_cache[class_name] = type(class_name, (type(element),), {})
        element.__class__ = self.class_cache.get(class_name, type(element))

    def __map_plane_if_present(self, data: dict, element: DiagramElement) -> List[UnresolvedField]:
        """
        Map the plane section of the data to a Plane object, extracting unresolved references.

        Parameters
        ----------
        data : dict
            Raw data potentially containing a plane section.
        element : DiagramElement
            Element to attach the plane to.

        Returns
        -------
        List[UnresolvedField]
            List of unresolved references within the plane section.
        """
        unresolved_fields = []

        plane_data = data.get("plane")
        if not plane_data:
            return unresolved_fields

        plane = Plane(element_id=plane_data.get("@id"))

        unresolved_fields.extend(
            self.__extract_references_and_set_attributes("modelElement", plane_data, plane)
            + self.__extract_references_and_set_attributes(
                "ownedDiagramElements", plane_data, plane
            )
        )

        element._plane = plane
        return unresolved_fields

    def __extract_references_and_set_attributes(
        self, attribute_name: str, plane_data: dict, plane: DiagramElement
    ) -> List[UnresolvedField]:
        """
        Extract references from plane data, assign to a plane, and return unresolved references.

        Parameters
        ----------
        attribute_name : str
            Key in the plane data to extract references from.
        plane_data : dict
            Dictionary containing data with potential references.
        plane : DiagramElement
            Target object for setting the extracted references on as an attribute.

        Returns
        -------
        List[UnresolvedField]
            List of unresolved references found during extraction.
        """
        from ansys.sam.sysml2.tools.name_utils import NameUtils

        new_attr_name = NameUtils.to_key(attribute_name)
        raw_value = plane_data.get(attribute_name, [])
        resolved, unresolved = self.__extract_reference(
            raw_value, plane, new_attr_name, attribute_name
        )

        if isinstance(raw_value, list):
            value_to_set = resolved
        elif resolved is not None and len(resolved) > 0:
            value_to_set = resolved[0]
        else:
            value_to_set = None

        setattr(plane, new_attr_name, value_to_set)

        return unresolved

    def __extract_reference(
        self,
        data: Union[dict, list],
        owner: DiagramElement,
        attr: str,
        original_key: str = None,
    ) -> Tuple[List, List[UnresolvedField]]:
        """
        Extract references from a dictionary or list of dictionaries.

        Parameters
        ----------
        data : dict or list
            Single dictionary or a list of items to inspect.
        owner : DiagramElement
            Object owning the attribute.
        attr : str
            Name of the attribute.
        original_key : str, optional
            Original key for context propagation.

        Returns
        -------
        tuple[list, list[UnresolvedField]]
            Tuple containing:

            - A list of resolved values.
            - A list of unresolved fields.
        """
        if isinstance(data, dict):
            return self.__process_single_item(data, owner, attr, original_key)

        if isinstance(data, list):
            return self.__process_list_items(data, owner, attr, original_key)

        return [data], []

    def __process_single_item(
        self,
        item: dict,
        owner: DiagramElement,
        attr: str,
        original_key: str = None,
    ) -> Tuple[List, List[UnresolvedField]]:
        """
        Handle a single dictionary item, resolving references or building nested elements.

        Parameters
        ----------
        item : dict
            Dictionary representing a single element, possibly containing a reference key "$ref".
        owner : DiagramElement
            Object that owns the attribute being set.
        attr : str
            Name of the attribute on the owner.
        original_key : str, optional
            Original key for context propagation.

        Returns
        -------
        tuple[list, list[UnresolvedField]]
            - List containing exactly one resolved element or reference ID.
            - List of unresolved references discovered during processing.
        """
        unresolved_fields = []

        if "$ref" in item:
            ref_id = item["$ref"]
            unresolved_fields.append(UnresolvedField(owner, attr, ref_id))
            return [ref_id], unresolved_fields

        mapped = self.map(item)
        element = mapped.get_element()

        if original_key == "points" and not hasattr(element, TYPE_KEY):
            self.__assign_dynamic_class(element, "Point")

        return [element], mapped.get_unresolved_fields()

    def __process_list_items(
        self,
        items: list,
        owner: DiagramElement,
        attr: str,
        original_key: str = None,
    ) -> Tuple[List, List[UnresolvedField]]:
        """
        Handle a list of items, resolving references and building nested elements.

        Parameters
        ----------
        items : list
            List containing dictionaries or simple values.
        owner : DiagramElement
            Object that owns the attribute being set.
        attr : str
            Name of the attribute on the owner.
        original_key : str, default: None
            Original key for context propagation.

        Returns
        -------
        tuple[list, list[UnresolvedField]]
            - List of resolved elements and/or simple values.
            - List of unresolved references.
        """
        values = []
        unresolved_fields: List[UnresolvedField] = []

        for item in items:
            if isinstance(item, dict):
                extracted, new_unresolved = self.__process_single_item(
                    item, owner, attr, original_key
                )
                values.extend(extracted)
                unresolved_fields.extend(new_unresolved)
            else:
                values.append(item)

        return values, unresolved_fields

    def __handle_dict_field(
        self, value: dict, element: DiagramElement, attr: str
    ) -> List[UnresolvedField]:
        """
        Assign a dictionary field to an element attribute, handling references and nested elements.

        Parameters
        ----------
        value : dict
            Dictionary value representing a single element or reference.
        element : DiagramElement
            Target element to update.
        attr : str
            Attribute name on the element to set.

        Returns
        -------
        list[UnresolvedField]
            List of unresolved references found while processing this dictionary.
        """
        extracted_value, unresolved = self.__extract_reference(value, element, attr)

        if extracted_value is not None and len(extracted_value) > 0:
            setattr(element, attr, extracted_value[0])
        else:
            setattr(element, attr, None)

        return unresolved

    def __handle_list_field(
        self, items: list, element: DiagramElement, attr: str, original_key: str
    ) -> List[UnresolvedField]:
        """
        Assign a list field to an element attribute, resolving references and nested elements.

        Parameters
        ----------
        items : list
            List of values.
        element : DiagramElement
            Target element to update.
        attr : str
            Attribute name on the element to set.
        original_key : str
            Original key from JSON data for context propagation.

        Returns
        -------
        list[UnresolvedField]
            List of unresolved references found while processing the list.
        """
        extracted_value, unresolved = self.__extract_reference(items, element, attr, original_key)
        setattr(element, attr, extracted_value)
        return unresolved

    def __add_fields(self, data: dict, element: DiagramElement) -> List[UnresolvedField]:
        """
        Map dynamic JSON fields onto a diagram element's attributes, handling nested structures.

        Parameters
        ----------
        data : dict
            JSON data to map.
        element : DiagramElement
            Target object to set attributes on.

        Returns
        -------
        List[UnresolvedField]
            List of unresolved references found during the mapping.
        """
        from ansys.sam.sysml2.tools.name_utils import NameUtils

        unresolved_fields = []

        for key, value in data.items():
            if key.startswith("@") or key in {"plane", TYPE_KEY}:
                continue

            attr_name = NameUtils.to_key(key)

            if isinstance(value, dict):
                unresolved_fields += self.__handle_dict_field(value, element, attr_name)
            elif isinstance(value, list):
                unresolved_fields += self.__handle_list_field(value, element, attr_name, key)
            else:
                setattr(element, attr_name, value)

        return unresolved_fields
