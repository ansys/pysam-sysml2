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

"""Generated occurrence usage class from metamodel."""

from __future__ import annotations

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .usage import Usage


class OccurrenceUsage(Usage):
    """Java class 'com.ansys.medini.metamodel.sysml.OccurrenceUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._portion_kind = None
        self._set_is_individual = False
        self._is_individual = None
        self._portioning_feature = None
        self._occurrence_definition = ObservedList(self, "occurrence_definition")
        self._individual_definition = None

    @property
    def portion_kind(self) -> None:  # noqa: F821
        """
        Get the portion kind property.

        Returns
        -------
        None
            Value of property portion kind.
        """
        return self._portion_kind

    @portion_kind.setter
    def portion_kind(self, value: None):  # noqa: F821
        """
        Set the portion_kind property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "portion_kind", value)
        self._portion_kind = value

    @property
    def set_is_individual(self) -> bool:  # noqa: F821
        """
        Get the set is individual property.

        Returns
        -------
        bool
            Value of property set is individual.
        """
        return self._set_is_individual

    @property
    def is_individual(self) -> None:  # noqa: F821
        """
        Get the is individual property.

        Returns
        -------
        None
            Value of property is individual.
        """
        return self._is_individual

    @is_individual.setter
    def is_individual(self, value: None):  # noqa: F821
        """
        Set the is_individual property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_individual", value)
        self._is_individual = value

    @property
    def portioning_feature(self) -> None:  # noqa: F821
        """
        Get the portioning feature property.

        Returns
        -------
        None
            Value of property portioning feature.
        """
        return self._portioning_feature

    @portioning_feature.setter
    def portioning_feature(self, value: None):  # noqa: F821
        """
        Set the portioning_feature property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "portioning_feature", value)
        self._portioning_feature = value

    @property
    def occurrence_definition(self) -> List["Class"]:  # noqa: F821
        """
        Get the occurrence definition property.

        Returns
        -------
        List["Class"]
            Value of property occurrence definition.
        """
        return self._occurrence_definition

    @property
    def individual_definition(self) -> "OccurrenceDefinition":  # noqa: F821
        """
        Get the individual definition property.

        Returns
        -------
        "OccurrenceDefinition"
            Value of property individual definition.
        """
        return self._individual_definition

    @individual_definition.setter
    def individual_definition(self, value: "OccurrenceDefinition"):  # noqa: F821
        """
        Set the individual_definition property.

        Parameters
        ----------
        value: "OccurrenceDefinition"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "individual_definition", value)
        self._individual_definition = value
