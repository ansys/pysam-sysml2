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
"""Python base Class for SysML Element."""

from typing import Union

from ansys.sam.sysml2.dto.commit.commit_class import Commit
from ansys.sam.sysml2.dto.commit.data_version import DataVersion
from ansys.sam.sysml2.exception.runtime_exception import UnsupportedValueExpression
from ansys.sam.sysml2.observer.observer import ModificationObserver


class SysMLElement:
    """Python Base class for all SysML Element."""

    _id: str
    _observer: ModificationObserver = None

    def __init__(self, id: str) -> None:
        """Init method construct new Instance.

        Parameters
        ----------
        id : str
            Element id
        """
        self._id = id

    def __setattr__(self, name: str, value: object):
        """
        Blocker function the set function of each classes.

        Parameters
        ----------
        name : Key name
            The name of the key
        value : object
            The value of the key
        """
        if name != "_observer" and getattr(self, "_observer", None) is not None:
            self._observer.notify(self._id, name, value)
        super().__setattr__(name, value)

    def get_value(self):
        """Return the value of the feature."""
        if hasattr(self, "_defaultValue"):
            value = self._defaultValue
            if hasattr(value, "_value"):
                return value._value  # Literal
            else:
                return self._parse_expression(value, is_old_format=True)

        if hasattr(self, "_valuation"):
            value = self._valuation._value
            if hasattr(value, "_value"):
                return value._value  # Literal
            else:
                return self._parse_expression(value)

        return None

    def _parse_expression(self, value: dict, is_old_format: bool = False):
        """Parse expression and return parsed value and unit using specified format."""
        if getattr(value, "_operator", None) != "[":
            raise UnsupportedValueExpression("Expression not supported!")

        return self._parse_format(value, is_old_format)

    def _parse_format(self, value: dict, is_old_format: bool):
        """
        Parse an expression using the specified format type.

        Parameters
        ----------
        value : dict
            The expression object containing members and potentially an operator.
        is_old_format : bool
            Format of the expression. Must be either True for old format or False otherwise.

        Returns
        -------
        tuple
            A tuple of (value, unit_name or None).

        Raises
        ------
        UnsupportedValueExpression
            If no parsable values are found in the expression.
        """
        owned_member = getattr(value, "_ownedMember", [])

        if is_old_format:
            values = [x._value for x in owned_member if hasattr(x, "_value")]
            return self._format_result_with_unit(values, owned_member, is_old_format)
        else:
            elements = [
                x
                for x in owned_member
                if hasattr(x, "_valuation") and hasattr(x._valuation, "_value")
            ]
            return self._format_result_with_unit(elements, owned_member, is_old_format)

    def _format_result_with_unit(self, elements: list, owned_member: list, is_old_format: bool):
        """Format a parsed expression value along with its associated unit (if available)."""
        if not elements:
            raise UnsupportedValueExpression("No values found in expression")

        try:
            if is_old_format:
                value = elements[0]
                referents = [x._referent for x in owned_member if hasattr(x, "_referent")]
            else:
                value = elements[0]._valuation._value._value
                referents = [
                    x._valuation._value._referent
                    for x in elements
                    if hasattr(x._valuation._value, "_referent")
                ]
        except NameError:
            raise UnsupportedValueExpression("No values found in expression")

        return (value, self._extract_unit_name(referents))

    def _extract_unit_name(self, referents):
        """Extract the unit name from referents, if any, otherwise return None."""
        if not referents:
            return None

        unit = referents[0]
        if hasattr(unit, "_shortName"):
            return unit._shortName
        elif hasattr(unit, "_name"):
            return unit._name

        return None

    def parse_and_set_value(self, value: str):
        """Parse the value and create the valuation part in the Feature."""
        self.__set_or_update_value("operator", value)

    def set_value(self, new_value: Union[str | int | float | bool]):
        """Update the Feature value."""
        self.__set_or_update_value(type(new_value), new_value)

    def __set_or_update_value(self, value_type: type, new_value: Union[str | int | float | bool]):
        """Create the commit to update the value of type value_type."""
        self._create_value(value_type, new_value)

    def _create_value(self, value_type: type, new_value: Union[str | int | float | bool]):
        """Create a new value of type value_type into the Feature."""
        project_id = self._observer._project_id
        commit = Commit(project_id)
        change = DataVersion()
        change.add_change("@type", "FeatureValue")
        if value_type != "operator":
            change.add_change("value", self._adapt_value(new_value))
        else:
            change.add_change("value", new_value)
        change.add_change("owner", self)
        commit.add_change(change)
        self._observer._connector.create_commit(project_id, commit.to_json())
        self._observer.reload_project()

    def _adapt_value(self, new_value: Union[str | int | float | bool]):
        """Convert the value to JSON format."""
        if isinstance(new_value, bool):
            return "true" if new_value else "false"
        if isinstance(new_value, str):
            return f'"{new_value}"'
        else:
            return str(new_value)
