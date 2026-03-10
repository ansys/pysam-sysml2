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

"""Generated specialization class from metamodel."""

from __future__ import annotations

from .relationship import Relationship


class Specialization(Relationship):
    """Java class 'com.ansys.medini.metamodel.sysml.Specialization'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._owning_type = None
        self._specific = None
        self._general = None

    @property
    def owning_type(self) -> "Type":  # noqa: F821
        """
        Get the owning type property.

        Returns
        -------
        "Type"
            Value of property owning type.
        """
        return self._owning_type

    @owning_type.setter
    def owning_type(self, value: "Type"):  # noqa: F821
        """
        Set the owning_type property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_type", value)
        self._owning_type = value

    @property
    def specific(self) -> None:  # noqa: F821
        """
        Get the specific property.

        Returns
        -------
        None
            Value of property specific.
        """
        return self._specific

    @specific.setter
    def specific(self, value: None):  # noqa: F821
        """
        Set the specific property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "specific", value)
        self._specific = value

    @property
    def general(self) -> None:  # noqa: F821
        """
        Get the general property.

        Returns
        -------
        None
            Value of property general.
        """
        return self._general

    @general.setter
    def general(self, value: None):  # noqa: F821
        """
        Set the general property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "general", value)
        self._general = value
