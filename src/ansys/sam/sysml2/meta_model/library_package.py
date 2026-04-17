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

"""Generated library package class from metamodel."""

from __future__ import annotations

from .package import Package


class LibraryPackage(Package):
    """Java class 'com.ansys.medini.metamodel.sysml.LibraryPackage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._is_standard = False

    @property
    def is_standard(self) -> bool:  # noqa: F821
        """
        Get the is standard property.

        Returns
        -------
        bool
            Value of property is standard.
        """
        return self._is_standard

    @is_standard.setter
    def is_standard(self, value: bool):  # noqa: F821
        """
        Set the is_standard property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_standard", value)
        self._is_standard = value
