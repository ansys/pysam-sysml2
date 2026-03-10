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

"""Generated metadata feature class from metamodel."""

from __future__ import annotations

from .annotating_element import AnnotatingElement
from .feature import Feature


class MetadataFeature(Feature, AnnotatingElement):
    """Java class 'com.ansys.medini.metamodel.sysml.MetadataFeature'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._metaclass = None

    @property
    def metaclass(self) -> "Metaclass":  # noqa: F821
        """
        Get the metaclass property.

        Returns
        -------
        "Metaclass"
            Value of property metaclass.
        """
        return self._metaclass

    @metaclass.setter
    def metaclass(self, value: "Metaclass"):  # noqa: F821
        """
        Set the metaclass property.

        Parameters
        ----------
        value: "Metaclass"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "metaclass", value)
        self._metaclass = value
