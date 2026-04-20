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

"""Generated documentation class from metamodel."""

from __future__ import annotations

from .comment import Comment


class Documentation(Comment):
    """Java class 'com.ansys.medini.metamodel.sysml.Documentation'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._documented_element = None

    @property
    def documented_element(self) -> "Element":  # noqa: F821
        """
        Get the documented element property.

        Returns
        -------
        "Element"
            Value of property documented element.
        """
        return self._documented_element

    @documented_element.setter
    def documented_element(self, value: "Element"):  # noqa: F821
        """
        Set the documented_element property.

        Parameters
        ----------
        value: "Element"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "documented_element", value)
        self._documented_element = value
