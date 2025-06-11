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

"""Project Interface for users."""

from typing import List

from ansys.sam.sysml2.classes.sysml_element import SysMLElement


class Project:
    """Project Interface for users."""

    def get_root(self) -> List[SysMLElement]:
        """
        Return the list of root packages.

        Returns
        -------
        List[SysMLElement]
            List of roots elements
        """

    def get_root_package(self) -> SysMLElement:
        """
        Return root package.

        Returns
        -------
        SysMLElement
            Root element
        """

    def find_element_by_id(self, element_id: str) -> SysMLElement:
        """
        Find element with id.

        Parameters
        ----------
        element_id : str
            Element Id

        Returns
        -------
        SysMLElement
            Founded Element
        """

    def find_elements_by_name(self, elements_name: str) -> List[SysMLElement]:
        """
        Find all element with name.

        Parameters
        ----------
        elements_name : str
            Name if elements

        Returns
        -------
        List[SysMLElement]
            The list of elements found.
        """
