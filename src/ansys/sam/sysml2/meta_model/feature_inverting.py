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

"""Generated feature inverting class from metamodel."""

from __future__ import annotations

from .relationship import Relationship


class FeatureInverting(Relationship):
    """Java class 'com.ansys.metamodel.sysml2.FeatureInverting'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._feature_inverted = None
        self._inverting_feature = None
        self._owning_feature = None

    @property
    def feature_inverted(self) -> "Feature":  # noqa: F821
        """
        Get the feature inverted property.

        Returns
        -------
        "Feature"
            Value of property feature inverted.
        """
        return self._feature_inverted

    @feature_inverted.setter
    def feature_inverted(self, value: "Feature"):  # noqa: F821
        """
        Set the feature_inverted property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "feature_inverted", value)
        self._feature_inverted = value

    @property
    def inverting_feature(self) -> "Feature":  # noqa: F821
        """
        Get the inverting feature property.

        Returns
        -------
        "Feature"
            Value of property inverting feature.
        """
        return self._inverting_feature

    @inverting_feature.setter
    def inverting_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the inverting_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "inverting_feature", value)
        self._inverting_feature = value

    @property
    def owning_feature(self) -> "Feature":  # noqa: F821
        """
        Get the owning feature property.

        Returns
        -------
        "Feature"
            Value of property owning feature.
        """
        return self._owning_feature

    @owning_feature.setter
    def owning_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the owning_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_feature", value)
        self._owning_feature = value
