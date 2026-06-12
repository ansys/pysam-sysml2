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

"""Generated instantiation expression class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .expression import Expression


class InstantiationExpression(Expression):
    """Java class 'com.ansys.metamodel.sysml2.InstantiationExpression'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._argument = ObservedList(self, "argument")
        self._instantiated_type = None

    @property
    def argument(self) -> list["Expression"]:  # noqa: F821
        """
        Get the argument property.

        Returns
        -------
        list["Expression"]
            Value of property argument.
        """
        return self._argument

    @property
    def instantiated_type(self) -> "Type":  # noqa: F821
        """
        Get the instantiated type property.

        Returns
        -------
        "Type"
            Value of property instantiated type.
        """
        return self._instantiated_type

    @instantiated_type.setter
    def instantiated_type(self, value: "Type"):  # noqa: F821
        """
        Set the instantiated_type property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "instantiated_type", value)
        self._instantiated_type = value
