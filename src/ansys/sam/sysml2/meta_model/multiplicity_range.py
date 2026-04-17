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

"""Generated multiplicity range class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .multiplicity import Multiplicity


class MultiplicityRange(Multiplicity):
    """Java class 'com.ansys.medini.metamodel.sysml.MultiplicityRange'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._upper_bound = None
        self._lower_bound = None
        self._bound = ObservedList(self, "bound")

    @property
    def upper_bound(self) -> "Expression":  # noqa: F821
        """
        Get the upper bound property.

        Returns
        -------
        "Expression"
            Value of property upper bound.
        """
        return self._upper_bound

    @upper_bound.setter
    def upper_bound(self, value: "Expression"):  # noqa: F821
        """
        Set the upper_bound property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "upper_bound", value)
        self._upper_bound = value

    @property
    def lower_bound(self) -> "Expression":  # noqa: F821
        """
        Get the lower bound property.

        Returns
        -------
        "Expression"
            Value of property lower bound.
        """
        return self._lower_bound

    @lower_bound.setter
    def lower_bound(self, value: "Expression"):  # noqa: F821
        """
        Set the lower_bound property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "lower_bound", value)
        self._lower_bound = value

    @property
    def bound(self) -> list["Expression"]:  # noqa: F821
        """
        Get the bound property.

        Returns
        -------
        list["Expression"]
            Value of property bound.
        """
        return self._bound
