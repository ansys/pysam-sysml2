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

"""Tool module for SysML elements."""

from ansys.sam.sysml2.classes.sysml_element import SysMLElement


class SysMLTools:
    """Static class for all sysml tools."""

    @staticmethod
    def isinstance(element: SysMLElement, type: str) -> bool:
        """
        Use this function to check type of an element.

        Parameters
        ----------
        element : SysMLElement
            The element to check
        type : str
            SysML class name

        Returns
        -------
        bool
            True if yes, False else
        """
        return element.__class__.__name__.split(".")[-1] == type

    @staticmethod
    def extract_value(feature: SysMLElement) -> object:
        """
        Extract value from a feature.

        Parameters
        ----------
        feature : SysMLElement
            Feature

        Returns
        -------
        object
            value None if no value
        """
        default_value = getattr(feature, "_defaultValue", None)
        if default_value is not None:
            value = getattr(default_value, "_value", None)
            if value is not None:
                return value
            value = getattr(default_value, "_ownedMember", [])
            if len(value) > 0:
                return SysMLTools.extract_value(value[0])
        return getattr(feature, "_value", None)
