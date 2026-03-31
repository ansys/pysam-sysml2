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
"""SysML specific mapper for SysML version."""

from io import UnsupportedOperation
from typing import List, Union

from ansys.sam.sysml2.builder.classes.sysml_util import SysMLUtil
from ansys.sam.sysml2.builder.mapper.mapper import Mapper
from ansys.sam.sysml2.classes.mapped_element import MappedElement
from ansys.sam.sysml2.classes.unresolved_field import UnresolvedField
from ansys.sam.sysml2.data_structures.observed_list import ObservedList
from ansys.sam.sysml2.exception.mapper_exception import (
    InvalidProjectJSONMapperException,
)
from ansys.sam.sysml2.meta_model.element import Element
from ansys.sam.sysml2.meta_model.feature_value import FeatureValue

TYPE_KEY = "@type"


class SysmlMapper(Mapper):
    """JSON mapper class for SysML version."""

    class_cache = {}

    def map(self, name_space: str, json_element: dict, mapped_element: Element) -> MappedElement:
        """
        Map the JSON into a python element.

        Parameters
        ----------
        name_space : str
            Project namespace.
        json_element : dict
            Element data.
        mapped_element : Element
            Existing element.

        Returns
        -------
        MappedElement
            Mapped element.
        """
        if TYPE_KEY not in json_element:
            raise InvalidProjectJSONMapperException("Not valid sysml element data")

        return self.__build_element(name_space, json_element, mapped_element)

    def __build_element(self, name_space: str, data: dict, element: Element) -> MappedElement:
        """
        Map element data to python object.

        Parameters
        ----------
        name_space : str
            Project namespace.
        data : dict
            Element data.
        element : Element
            Existing element.

        Returns
        -------
        MappedElement
            Mapped element with the SysML element and its unresolved fields.
        """
        unresolved_fields = list()
        if element is None:
            constructor = SysMLUtil.get_sysml_constructor(data[TYPE_KEY])
            element = constructor(id=data["@id"])
        for k, v in data.items():
            if not k.startswith("@"):
                unresolved_fields.extend(self.__add_fields(element, k, v))
        if not getattr(element,"qualified_name","").startswith(name_space) and not isinstance(
            element, FeatureValue
        ):
            unresolved_fields = list()
        return MappedElement(element, unresolved_fields)

    def __add_fields(
        self,
        element: Element,
        field_name: str,
        field_values: Union[dict | list | str],
    ) -> List[UnresolvedField]:
        """
        Associate element and value with key.

        Parameters
        ----------
        element : Element
            Destination element.
        field_name : str
            Field name.
        field_values : Union[dict | list | str]
            Field value.

        Returns
        -------
        List[UnresolvedField]
            List of all unresolved fields.
        """
        from ansys.sam.sysml2.tools.name_utils import NameUtils

        field_name = "_" + NameUtils.to_snake_case(field_name)
        # Fix due to differences between Standard API and Metamodel
        if field_name == "_inherited_feature":
            field_name = "_owned_inherited_feature"
        if isinstance(field_values, list):
            return self.__add_list_to_field(element, field_name, field_values)
        if isinstance(field_values, dict):
            return self.__add_element_to_field(element, field_name, field_values)
        else:
            return self.__add_default_field(element, field_name, field_values)

    def __add_default_field(self, element: Element, field_name: str, field_value: str) -> List:
        """
        Adder for default type.

        Parameters
        ----------
        element : Element
            Destination element.
        field_name : str
            Field name.
        field_value : str
            Field value.

        Returns
        -------
        List
            Empty list because the fields are already resolved.
        """
        setattr(element, field_name, field_value)
        return []

    def __add_element_to_field(self, element: Element, key: str, value: dict):
        """
        Adder for simple element field.

        Parameters
        ----------
        element : Element
            Destination element.
        key : str
            Field name.
        value : dict
            Field value.

        Returns
        -------
        List[UnresolvedField]
            List of the unresolved field.
        """
        setattr(element, key, value["@id"])
        return [UnresolvedField(element, key, value["@id"])]

    def __add_list_to_field(self, element: Element, key: str, field_values: list):
        """
        Adder function for list elements value.

        Parameters
        ----------
        element : Element
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
