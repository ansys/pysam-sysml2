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

"""Generated event occurrence usage class from metamodel."""

from __future__ import annotations

from .occurrence_usage import OccurrenceUsage


class EventOccurrenceUsage(OccurrenceUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.EventOccurrenceUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._event_occurrence = None
        self._is_reference = False

    @property
    def event_occurrence(self) -> "OccurrenceUsage":  # noqa: F821
        """
        Get the event occurrence property.

        Returns
        -------
        "OccurrenceUsage"
            Value of property event occurrence.
        """
        return self._event_occurrence

    @event_occurrence.setter
    def event_occurrence(self, value: "OccurrenceUsage"):  # noqa: F821
        """
        Set the event_occurrence property.

        Parameters
        ----------
        value: "OccurrenceUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "event_occurrence", value)
        self._event_occurrence = value

    @property
    def is_reference(self) -> bool:  # noqa: F821
        """
        Get the is reference property.

        Returns
        -------
        bool
            Value of property is reference.
        """
        return self._is_reference

    @is_reference.setter
    def is_reference(self, value: bool):  # noqa: F821
        """
        Set the is_reference property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_reference", value)
        self._is_reference = value
