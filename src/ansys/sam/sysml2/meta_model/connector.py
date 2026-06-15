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

"""Generated connector class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .feature import Feature
from .relationship import Relationship


class Connector(Feature, Relationship):
    """Java class 'com.ansys.metamodel.sysml2.Connector'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._association = ObservedList(self, "association")
        self._connector_end = ObservedList(self, "connector_end")
        self._default_featuring_type = None
        self._related_feature = ObservedList(self, "related_feature")
        self._source_feature = None
        self._target_feature = ObservedList(self, "target_feature")

    @property
    def association(self) -> list["Association"]:  # noqa: F821
        """
        Get the association property.

        Returns
        -------
        list["Association"]
            Value of property association.
        """
        return self._association

    @property
    def connector_end(self) -> list["Feature"]:  # noqa: F821
        """
        Get the connector end property.

        Returns
        -------
        list["Feature"]
            Value of property connector end.
        """
        return self._connector_end

    @property
    def default_featuring_type(self) -> "Type":  # noqa: F821
        """
        Get the default featuring type property.

        Returns
        -------
        "Type"
            Value of property default featuring type.
        """
        return self._default_featuring_type

    @default_featuring_type.setter
    def default_featuring_type(self, value: "Type"):  # noqa: F821
        """
        Set the default_featuring_type property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "default_featuring_type", value)
        self._default_featuring_type = value

    @property
    def related_feature(self) -> list["Feature"]:  # noqa: F821
        """
        Get the related feature property.

        Returns
        -------
        list["Feature"]
            Value of property related feature.
        """
        return self._related_feature

    @property
    def source_feature(self) -> "Feature":  # noqa: F821
        """
        Get the source feature property.

        Returns
        -------
        "Feature"
            Value of property source feature.
        """
        return self._source_feature

    @source_feature.setter
    def source_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the source_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "source_feature", value)
        self._source_feature = value

    @property
    def target_feature(self) -> list["Feature"]:  # noqa: F821
        """
        Get the target feature property.

        Returns
        -------
        list["Feature"]
            Value of property target feature.
        """
        return self._target_feature
