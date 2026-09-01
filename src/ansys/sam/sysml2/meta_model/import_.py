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

"""Generated import class from metamodel."""

from __future__ import annotations

from .relationship import Relationship


class Import(Relationship):
    """Java class 'com.ansys.medini.metamodel.sysml.Import'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._is_recursive = False
        self._imported_namespace = None

    @property
    def is_recursive(self) -> bool:  # noqa: F821
        """
        Get the is recursive property.

        Returns
        -------
        bool
            Value of property is recursive.
        """
        return self._is_recursive

    @is_recursive.setter
    def is_recursive(self, value: bool):  # noqa: F821
        """
        Set the is_recursive property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_recursive", value)
        self._is_recursive = value

    @property
    def imported_namespace(self) -> "Namespace":  # noqa: F821
        """
        Get the imported namespace property.

        Returns
        -------
        "Namespace"
            Value of property imported namespace.
        """
        return self._imported_namespace

    @imported_namespace.setter
    def imported_namespace(self, value: "Namespace"):  # noqa: F821
        """
        Set the imported_namespace property.

        Parameters
        ----------
        value: "Namespace"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "imported_namespace", value)
        self._imported_namespace = value
