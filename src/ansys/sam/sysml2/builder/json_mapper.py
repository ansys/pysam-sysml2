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

"""JSON Mapper class."""

from io import UnsupportedOperation
from typing import List, Union

from ansys.sam.sysml2.builder.classes.derived_list import DerivedList
from ansys.sam.sysml2.classes.mapped_element import MappedElement
from ansys.sam.sysml2.classes.sysml_element import SysMLElement
from ansys.sam.sysml2.classes.unresolved_field import UnresolvedField
from ansys.sam.sysml2.exception.mapper_exception import InvalidProjectJSONMapperException
from ansys.sam.sysml2.tools.sysmltools import SysMLTools

TYPE_KEY = "@type"


class JsonMapper:
    """JSON Mapper class for Sysml Element."""

    class_cache = {}

    def map(self, name_space: str, element: dict, mapped_element: SysMLElement) -> MappedElement:
        """
        Map the json into a Python element.

        Parameters
        ----------
        element : dict
            element data
        name_space: str
            project name space

        Returns
        -------
        MappedElement
            Mapped element
        """
        if TYPE_KEY not in element:
            raise InvalidProjectJSONMapperException("Not valid sysml element data")

        return self.__build_element(name_space, element, mapped_element)

    def __build_element(self, name_space: str, data: dict, element: SysMLElement) -> MappedElement:
        """
        Map element data to Python Object.

        Parameters
        ----------
        data : dict
            Element data
        name_space: str
            project name space

        Returns
        -------
        MappedElement
            MappedElement with the sysml element and his unresolved fields
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
        Update the default SysML Element definition to the SysML Element.

        Parameters
        ----------
        data : dict
            element data
        element : SysMLElement
            The associated element
        """
        element_type = data[TYPE_KEY]
        try:
            element.__class__ = self.class_cache[element_type]
        except KeyError:
            self.class_cache[element_type] = type(
                element_type,
                (SysMLElement,),
                {},
            )
            element.__class__ = self.class_cache[element_type]

    def __add_fields(
        self, element: SysMLElement, key: str, value: Union[dict | list | str]
    ) -> List[UnresolvedField]:
        """
        Associate element and value with key.

        Parameters
        ----------
        element : SysMLElement
            destination element
        key : str
            field name
        value : Union[dict  |  list  |  str]
            field value

        Returns
        -------
        List[UnresolvedField]
            the list of all unresolved Fields
        """
        key = "_" + key
        if isinstance(value, list):
            return self.__add_list_to_field(element, key, value)
        if isinstance(value, dict):
            return self.__add_element_to_field(element, key, value)
        else:
            return self.__add_default_field(element, key, value)

    def __add_default_field(self, element: SysMLElement, key: str, value: str) -> List:
        """
        Adder for default type.

        Parameters
        ----------
        element : SysMLElement
            destination element
        key : str
            field name
        value : Union[dict  |  list  |  str]
            field value

        Returns
        -------
        List
            Empty list because fields already resolved.
        """
        setattr(element, key, value)
        return []

    def __add_element_to_field(self, element: SysMLElement, key: str, value: dict):
        """
        Adder for simple element field.

        Parameters
        ----------
        element : SysMLElement
            destination element
        key : str
            field name
        value : Union[dict  |  list  |  str]
            field value

        Returns
        -------
        List[UnresolvedField]
            A list with the unresolved Field
        """
        setattr(element, key, value["@id"])
        return [UnresolvedField(element, key, value["@id"])]

    def __add_list_to_field(self, element: SysMLElement, key: str, value: list):
        """
        Adder Function for list elements value.

        Parameters
        ----------
        element : SysMLElement
            destination element
        key : str
            field name
        value : Union[dict  |  list  |  str]
            field value

        Returns
        -------
        List[UnresolvedField]
            the list of all unresolved Fields created for the list elements.
        """
        if all(isinstance(e, dict) for e in value):
            setattr(
                element,
                key,
                DerivedList(element, key, *[e["@id"] for e in value]),
            )
            return [UnresolvedField(element, key, e["@id"]) for e in value]
        elif not any(isinstance(e, dict) for e in value):
            setattr(
                element,
                key,
                DerivedList(element, key, *value),
            )
            return []
        else:
            raise UnsupportedOperation(f"Could not index list for {key}.")
