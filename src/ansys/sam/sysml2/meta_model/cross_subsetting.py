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

"""Generated cross subsetting class from metamodel."""

from __future__ import annotations

from .subsetting import Subsetting


class CrossSubsetting(Subsetting):
    """Java class 'com.ansys.metamodel.sysml2.CrossSubsetting'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._crossed_feature = None
        self._crossing_feature = None

    @property
    def crossed_feature(self) -> "Feature":  # noqa: F821
        """
        Get the crossed feature property.

        Returns
        -------
        "Feature"
            Value of property crossed feature.
        """
        return self._crossed_feature

    @crossed_feature.setter
    def crossed_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the crossed_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "crossed_feature", value)
        self._crossed_feature = value

    @property
    def crossing_feature(self) -> "Feature":  # noqa: F821
        """
        Get the crossing feature property.

        Returns
        -------
        "Feature"
            Value of property crossing feature.
        """
        return self._crossing_feature

    @crossing_feature.setter
    def crossing_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the crossing_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "crossing_feature", value)
        self._crossing_feature = value
