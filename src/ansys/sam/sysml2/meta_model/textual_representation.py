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

"""Generated textual representation class from metamodel."""

from __future__ import annotations

from .annotating_element import AnnotatingElement


class TextualRepresentation(AnnotatingElement):
    """Java class 'com.ansys.medini.metamodel.sysml.TextualRepresentation'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._language = ""
        self._body = None
        self._represented_element = None

    @property
    def language(self) -> str:  # noqa: F821
        """
        Get the language property.

        Returns
        -------
        str
            Value of property language.
        """
        return self._language

    @language.setter
    def language(self, value: str):  # noqa: F821
        """
        Set the language property.

        Parameters
        ----------
        value: str
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "language", value)
        self._language = value

    @property
    def body(self) -> None:  # noqa: F821
        """
        Get the body property.

        Returns
        -------
        None
            Value of property body.
        """
        return self._body

    @body.setter
    def body(self, value: None):  # noqa: F821
        """
        Set the body property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "body", value)
        self._body = value

    @property
    def represented_element(self) -> None:  # noqa: F821
        """
        Get the represented element property.

        Returns
        -------
        None
            Value of property represented element.
        """
        return self._represented_element

    @represented_element.setter
    def represented_element(self, value: None):  # noqa: F821
        """
        Set the represented_element property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "represented_element", value)
        self._represented_element = value
