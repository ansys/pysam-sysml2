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

"""Mapped Element class."""

from typing import List

from ansys.sam.sysml2.classes.sysml_element import SysMLElement
from ansys.sam.sysml2.classes.unresolved_field import UnresolvedField


class MappedElement:
    """Mapped Element class."""

    _element: SysMLElement
    _unresolved_fields: List[UnresolvedField]

    def __init__(self, element: SysMLElement, unresolved_fields: List[UnresolvedField]):
        """
        Construct Method for new instance.

        Parameters
        ----------
        element : SysMLElement
            The mapped Element
        _unresolved_fields : List[UnresolvedField]
            List of all his unresolved fields=
        """
        self._element = element
        self._unresolved_fields = unresolved_fields

    def get_element(self) -> SysMLElement:
        """
        Getter for the mapped element.

        Returns
        -------
        SysMLElement
            The mapped element
        """
        return self._element

    def get_unresolved_fields(self) -> List[UnresolvedField]:
        """
        Getter for the list of all unresolved Fields.

        Returns
        -------
        List[UnresolvedField]
            The list of all unresolved Fields
        """
        return self._unresolved_fields
