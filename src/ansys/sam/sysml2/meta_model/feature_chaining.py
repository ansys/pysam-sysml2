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

"""Generated feature chaining class from metamodel."""

from __future__ import annotations

from .relationship import Relationship


class FeatureChaining(Relationship):
    """Java class 'com.ansys.medini.metamodel.sysml.FeatureChaining'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._chaining_feature = None
        self._feature_chained = None

    @property
    def chaining_feature(self) -> "Feature":  # noqa: F821
        """
        Get the chaining feature property.

        Returns
        -------
        "Feature"
            Value of property chaining feature.
        """
        return self._chaining_feature

    @chaining_feature.setter
    def chaining_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the chaining_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "chaining_feature", value)
        self._chaining_feature = value

    @property
    def feature_chained(self) -> "Feature":  # noqa: F821
        """
        Get the feature chained property.

        Returns
        -------
        "Feature"
            Value of property feature chained.
        """
        return self._feature_chained

    @feature_chained.setter
    def feature_chained(self, value: "Feature"):  # noqa: F821
        """
        Set the feature_chained property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "feature_chained", value)
        self._feature_chained = value
