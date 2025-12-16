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

"""JSON Mapper class."""

from io import UnsupportedOperation
from typing import List, Union

from ansys.sam.sysml2.classes.mapped_element import MappedElement
from ansys.sam.sysml2.classes.sysml_element import SysMLElement
from ansys.sam.sysml2.classes.unresolved_field import UnresolvedField
from ansys.sam.sysml2.data_structures.observed_list import ObservedList
from ansys.sam.sysml2.exception.mapper_exception import (
    InvalidProjectJSONMapperException,
)
from ansys.sam.sysml2.tools.sysmltools import SysMLTools

TYPE_KEY = "@type"


class JsonMapper:
    """Provides the JSON mapper class for a SysML element."""

    class_cache = {}

    def map(
        self, name_space: str, json_element: dict, mapped_element: SysMLElement
    ) -> MappedElement:
        """
        Map the JSON into a Python element.

        Parameters
        ----------
        json_element : dict
            Element data.
        name_space: str
            Project name space.
        mapped_element: SysMLElement
            SysMLElement.

        Returns
        -------
        MappedElement
            Mapped element.
        """
        if TYPE_KEY not in json_element:
            raise InvalidProjectJSONMapperException("Not valid SysML2 element data.")

        return self.__build_element(name_space, json_element, mapped_element)

    def __build_element(self, name_space: str, data: dict, element: SysMLElement) -> MappedElement:
        """
        Map element data to a Python object.

        Parameters
        ----------
        data : dict
            Element data.
        name_space: str
            Project name space.
        element: SysMLElement
            SysMLElement.

        Returns
        -------
        MappedElement
            MappedElement with the Sysml element and its unresolved fields.
        """
        unresolved_fields = list()
        if element is None:
            element = SysMLElement(id=data["@id"])
        for k, v in data.items():
            if not k.startswith("@"):
                unresolved_fields.extend(self.__add_fields(element, k, v))
        self.__update_element_definition(data, element)
        if not element._qualifiedName.startswith(name_space) and not SysMLTools.isinstance(
            element, "FeatureValue"
        ):
            unresolved_fields = list()
        return MappedElement(element, unresolved_fields)

    def __update_element_definition(self, data: dict, element: SysMLElement) -> None:
        """
        Update the default SysML2 element definition to the SysML2 element.

        Parameters
        ----------
        data : dict
            Element data.
        element : SysMLElement
            Associated element.
        """
        element_type = data[TYPE_KEY]
        try:
            element.__class__ = self.class_cache[element_type]
        except KeyError:
            self.class_cache[element_type] = type(element_type, (SysMLElement,), {})
            element.__class__ = self.class_cache[element_type]

    def __add_fields(
        self,
        element: SysMLElement,
        field_name: str,
        field_values: Union[dict | list | str],
    ) -> List[UnresolvedField]:
        """
        Associate the element and value with a key.

        Parameters
        ----------
        element : SysMLElement
            Destination element.
        field_name : str
            Field name.
        field_values : Union[dict  |  list  |  str]
            Field value.

        Returns
        -------
        List[UnresolvedField]
            List of all unresolved fields.
        """
        field_name = "_" + field_name
        if isinstance(field_values, list):
            return self.__add_list_to_field(element, field_name, field_values)
        if isinstance(field_values, dict):
            return self.__add_element_to_field(element, field_name, field_values)
        else:
            return self.__add_default_field(element, field_name, field_values)

    def __add_default_field(self, element: SysMLElement, field_name: str, field_value: str) -> List:
        """
        Adder function for default type.

        Parameters
        ----------
        element : SysMLElement
            Destination element.
        field_name : str
            Field name.
        field_value : str
            Field value.

        Returns
        -------
        List
            Empty list because fields are already resolved.
        """
        setattr(element, field_name, field_value)
        return []

    def __add_element_to_field(
        self, element: SysMLElement, key: str, value: dict
    ) -> List[UnresolvedField]:
        """
        Adder function for simple element field.

        Parameters
        ----------
        element : SysMLElement
            Destination element.
        key : str
            Field name.
        value : dict
            Field value.

        Returns
        -------
        List[UnresolvedField]
            List with the unresolved fields.
        """
        setattr(element, key, value["@id"])
        return [UnresolvedField(element, key, value["@id"])]

    def __add_list_to_field(
        self, element: SysMLElement, key: str, field_values: list
    ) -> List[UnresolvedField]:
        """
        Adder function for list elements value.

        Parameters
        ----------
        element : SysMLElement
            Destination element.
        key : str
            Field name.
        field_values : list
            Field values.

        Returns
        -------
        List[UnresolvedField]
            List of all unresolved fields created for the list elements.
        """
        if all(isinstance(value, dict) for value in field_values):
            setattr(
                element,
                key,
                ObservedList(element, key, *[value["@id"] for value in field_values]),
            )
            return [UnresolvedField(element, key, value["@id"]) for value in field_values]
        elif not any(isinstance(value, dict) for value in field_values):
            setattr(
                element,
                key,
                ObservedList(element, key, *field_values),
            )
            return []
        else:
            raise UnsupportedOperation(f"Could not index list for {key}.")
