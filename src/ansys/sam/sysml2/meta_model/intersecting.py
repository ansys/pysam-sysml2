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

"""Generated intersecting class from metamodel."""

from __future__ import annotations

from .relationship import Relationship


class Intersecting(Relationship):
    """Java class 'com.ansys.metamodel.sysml2.Intersecting'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._intersecting_type = None
        self._type_intersected = None

    @property
    def intersecting_type(self) -> "Type":  # noqa: F821
        """
        Get the intersecting type property.

        Returns
        -------
        "Type"
            Value of property intersecting type.
        """
        return self._intersecting_type

    @intersecting_type.setter
    def intersecting_type(self, value: "Type"):  # noqa: F821
        """
        Set the intersecting_type property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "intersecting_type", value)
        self._intersecting_type = value

    @property
    def type_intersected(self) -> "Type":  # noqa: F821
        """
        Get the type intersected property.

        Returns
        -------
        "Type"
            Value of property type intersected.
        """
        return self._type_intersected

    @type_intersected.setter
    def type_intersected(self, value: "Type"):  # noqa: F821
        """
        Set the type_intersected property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "type_intersected", value)
        self._type_intersected = value
