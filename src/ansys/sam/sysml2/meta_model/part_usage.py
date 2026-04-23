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

"""Generated part usage class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .item_usage import ItemUsage


class PartUsage(ItemUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.PartUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._is_stakeholder = False
        self._part_definition = ObservedList(self, "part_definition")
        self._is_actor = False
        self._all_part_definition = ObservedList(self, "all_part_definition")

    @property
    def is_stakeholder(self) -> bool:  # noqa: F821
        """
        Get the is stakeholder property.

        Returns
        -------
        bool
            Value of property is stakeholder.
        """
        return self._is_stakeholder

    @is_stakeholder.setter
    def is_stakeholder(self, value: bool):  # noqa: F821
        """
        Set the is_stakeholder property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_stakeholder", value)
        self._is_stakeholder = value

    @property
    def part_definition(self) -> list["PartDefinition"]:  # noqa: F821
        """
        Get the part definition property.

        Returns
        -------
        list["PartDefinition"]
            Value of property part definition.
        """
        return self._part_definition

    @property
    def is_actor(self) -> bool:  # noqa: F821
        """
        Get the is actor property.

        Returns
        -------
        bool
            Value of property is actor.
        """
        return self._is_actor

    @is_actor.setter
    def is_actor(self, value: bool):  # noqa: F821
        """
        Set the is_actor property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_actor", value)
        self._is_actor = value

    @property
    def all_part_definition(self) -> list["PartDefinition"]:  # noqa: F821
        """
        Get the all part definition property.

        Returns
        -------
        list["PartDefinition"]
            Value of property all part definition.
        """
        return self._all_part_definition
