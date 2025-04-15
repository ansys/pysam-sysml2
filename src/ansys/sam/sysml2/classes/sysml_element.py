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
"""Python base Class for SysML Element."""


from typing import Any, Union

from ansys.sam.sysml2.classes.feature_helper import FeatureHelper
from ansys.sam.sysml2.exception.runtime_exception import UnsupportedValueExpression
from ansys.sam.sysml2.observer.observer import ModificationObserver


class SysMLElement:
    """Python Base class for all SysML Element."""

    _id: str
    _IS_READ_ONLY: bool = False
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
        if self._IS_READ_ONLY and name != "_IS_READ_ONLY":
            print(f"You can't set element on this {self.__class__.__name__}")
        else:
            if self._observer is not None:
                self._observer.notify(self._id, name, value)
            super().__setattr__(name, value)

    def get_value(self) -> Any:
        """
        Return the value of the feature.

        Returns
        -------
        Any
            Value
        """
        if not hasattr(self, "_valuation"):
            print("""Could not found valuation field, please update value to the last version.""")
            return None
        value = self._valuation._value
        if hasattr(value, "_value"):
            return value._value  # Literal
        else:
            return self._parse_expression(value)

    def _parse_expression(self, value):
        """
        Parse Complex expression and return if supported.

        Parameters
        ----------
        value : Value object
            The value object
        """
        if value._operator == "[":
            value_v = [
                x._defaultValue._value
                for x in value._ownedMember
                if hasattr(x, "_defaultValue") and hasattr(x._defaultValue, "_value")
            ]
            if len(value_v) > 0:
                unit_v = [
                    x._defaultValue._referent
                    for x in value._ownedMember
                    if hasattr(x, "_defaultValue") and hasattr(x._defaultValue, "_referent")
                ]
                if len(unit_v) > 0 and hasattr(unit_v[0], "_shortName"):
                    return (value_v[0], unit_v[0]._shortName)

        raise UnsupportedValueExpression("Expression not supported!")

    def parse_and_set_value(self, value: str):
        """
        Parse the Value and Set into the Feature.

        Parameters
        ----------
        value : str
            The value to parse
        """
        if not self._IS_READ_ONLY:
            self.__set_or_update_value("operator", value)

    def set_value(self, value: Union[str | int | float | bool]):
        """
        Update the Feature value.

        Parameters
        ----------
        value : Union[str  |  int  |  float  |  bool]
            The new Value
        """
        if not self._IS_READ_ONLY:
            self.__set_or_update_value(type(value), value)

    def __set_or_update_value(self, type_v: type, value: Any):
        """
        Create the commit to update the value.

        Parameters
        ----------
        type_v : str
            The type of the value
        value : Any
            The value
        """
        FeatureHelper.create_value(self, type_v, value)
