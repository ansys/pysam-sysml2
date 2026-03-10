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

"""Generated reference subsetting class from metamodel."""

from __future__ import annotations

from .subsetting import Subsetting


class ReferenceSubsetting(Subsetting):
    """Java class 'com.ansys.medini.metamodel.sysml.ReferenceSubsetting'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._referenced_feature = None
        self._referencing_feature = None

    @property
    def referenced_feature(self) -> "Feature":  # noqa: F821
        """
        Get the referenced feature property.

        Returns
        -------
        "Feature"
            Value of property referenced feature.
        """
        return self._referenced_feature

    @referenced_feature.setter
    def referenced_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the referenced_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "referenced_feature", value)
        self._referenced_feature = value

    @property
    def referencing_feature(self) -> "Feature":  # noqa: F821
        """
        Get the referencing feature property.

        Returns
        -------
        "Feature"
            Value of property referencing feature.
        """
        return self._referencing_feature

    @referencing_feature.setter
    def referencing_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the referencing_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "referencing_feature", value)
        self._referencing_feature = value
