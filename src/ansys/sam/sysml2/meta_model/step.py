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

"""Generated step class from metamodel."""

from __future__ import annotations

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .feature import Feature


class Step(Feature):
    """Java class 'com.ansys.medini.metamodel.sysml.Step'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._parameter = ObservedList(self, "parameter")
        self._behavior = ObservedList(self, "behavior")
        self._general_parameter = ObservedList(self, "general_parameter")
        self._transition_feature_kind = None

    @property
    def parameter(self) -> List["Feature"]:  # noqa: F821
        """
        Get the parameter property.

        Returns
        -------
        List["Feature"]
            Value of property parameter.
        """
        return self._parameter

    @property
    def behavior(self) -> List["Behavior"]:  # noqa: F821
        """
        Get the behavior property.

        Returns
        -------
        List["Behavior"]
            Value of property behavior.
        """
        return self._behavior

    @property
    def general_parameter(self) -> List["Feature"]:  # noqa: F821
        """
        Get the general parameter property.

        Returns
        -------
        List["Feature"]
            Value of property general parameter.
        """
        return self._general_parameter

    @property
    def transition_feature_kind(self) -> None:  # noqa: F821
        """
        Get the transition feature kind property.

        Returns
        -------
        None
            Value of property transition feature kind.
        """
        return self._transition_feature_kind

    @transition_feature_kind.setter
    def transition_feature_kind(self, value: None):  # noqa: F821
        """
        Set the transition_feature_kind property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "transition_feature_kind", value)
        self._transition_feature_kind = value
