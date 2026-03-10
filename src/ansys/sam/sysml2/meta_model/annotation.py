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

"""Generated annotation class from metamodel."""

from __future__ import annotations

from .relationship import Relationship


class Annotation(Relationship):
    """Java class 'com.ansys.medini.metamodel.sysml.Annotation'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._annotated_element = None
        self._annotating_element = None

    @property
    def annotated_element(self) -> "Element":  # noqa: F821
        """
        Get the annotated element property.

        Returns
        -------
        "Element"
            Value of property annotated element.
        """
        return self._annotated_element

    @annotated_element.setter
    def annotated_element(self, value: "Element"):  # noqa: F821
        """
        Set the annotated_element property.

        Parameters
        ----------
        value: "Element"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "annotated_element", value)
        self._annotated_element = value

    @property
    def annotating_element(self) -> None:  # noqa: F821
        """
        Get the annotating element property.

        Returns
        -------
        None
            Value of property annotating element.
        """
        return self._annotating_element

    @annotating_element.setter
    def annotating_element(self, value: None):  # noqa: F821
        """
        Set the annotating_element property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "annotating_element", value)
        self._annotating_element = value
