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

"""Generated occurrence definition class from metamodel."""

from __future__ import annotations

from .class_ import Class
from .definition import Definition


class OccurrenceDefinition(Definition, Class):
    """Java class 'com.ansys.medini.metamodel.sysml.OccurrenceDefinition'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._set_is_individual = False
        self._is_individual = None
        self._lifeclass = None

    @property
    def set_is_individual(self) -> bool:  # noqa: F821
        """
        Get the set is individual property.

        Returns
        -------
        bool
            Value of property set is individual.
        """
        return self._set_is_individual

    @property
    def is_individual(self) -> None:  # noqa: F821
        """
        Get the is individual property.

        Returns
        -------
        None
            Value of property is individual.
        """
        return self._is_individual

    @is_individual.setter
    def is_individual(self, value: None):  # noqa: F821
        """
        Set the is_individual property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_individual", value)
        self._is_individual = value

    @property
    def lifeclass(self) -> "LifeClass":  # noqa: F821
        """
        Get the lifeclass property.

        Returns
        -------
        "LifeClass"
            Value of property lifeclass.
        """
        return self._lifeclass

    @lifeclass.setter
    def lifeclass(self, value: "LifeClass"):  # noqa: F821
        """
        Set the lifeclass property.

        Parameters
        ----------
        value: "LifeClass"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "lifeclass", value)
        self._lifeclass = value
