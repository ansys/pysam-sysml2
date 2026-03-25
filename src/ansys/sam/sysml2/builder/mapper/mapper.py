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
"""Generic interface for mappers."""

from abc import ABC, abstractmethod
from io import UnsupportedOperation
from typing import List, Union

from ansys.sam.sysml2.classes.mapped_element import MappedElement
from ansys.sam.sysml2.classes.sysml_element import SysMLElement
from ansys.sam.sysml2.classes.unresolved_field import UnresolvedField
from ansys.sam.sysml2.data_structures.observed_list import ObservedList
from ansys.sam.sysml2.meta_model.element import Element


class Mapper(ABC):
    """Generic interface for mappers."""

    @abstractmethod
    def map(
        self,
        name_space: str,
        json_element: dict,
        mapped_element: Union[Element, SysMLElement],
    ) -> MappedElement:
        """
        Map abstract function.

        Parameters
        ----------
        name_space : str
            Current namespace.
        json_element : dict
            Data.
        mapped_element : Union[Element, SysMLElement]
            Existing element.

        Returns
        -------
        MappedElement
            Mapper element.
        """

    def _add_default_field(self, element, field_name: str, field_value) -> List:
        """Set a scalar field on the element.

        Parameters
        ----------
        element : Union[Element, SysMLElement]
            Destination element.
        field_name : str
            Field name.
        field_value : Any
            Field value.

        Returns
        -------
        List
            Empty list because the field is already resolved.
        """
        setattr(element, field_name, field_value)
        return []

    def _add_element_to_field(self, element, key: str, value: dict) -> List[UnresolvedField]:
        """Set a reference field and create an unresolved link.

        Parameters
        ----------
        element : Union[Element, SysMLElement]
            Destination element.
        key : str
            Field name.
        value : dict
            Field value containing an ``@id`` key.

        Returns
        -------
        List[UnresolvedField]
            List containing the unresolved field.
        """
        setattr(element, key, value["@id"])
        return [UnresolvedField(element, key, value["@id"])]

    def _add_list_to_field(self, element, key: str, field_values: list) -> List[UnresolvedField]:
        """Set a list field, creating unresolved links for reference items.

        Parameters
        ----------
        element : Union[Element, SysMLElement]
            Destination element.
        key : str
            Field name.
        field_values : list
            Field values.

        Returns
        -------
        List[UnresolvedField]
            List of all unresolved fields created for reference items.
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
