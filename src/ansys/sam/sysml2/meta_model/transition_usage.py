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

"""Generated transition usage class from metamodel."""

from __future__ import annotations

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .action_usage import ActionUsage


class TransitionUsage(ActionUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.TransitionUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._source = None
        self._target = None
        self._effect_action = ObservedList(self, "effect_action")
        self._trigger_action = ObservedList(self, "trigger_action")
        self._guard_expression = ObservedList(self, "guard_expression")
        self._succession = None
        self._inherited_effect_action = ObservedList(self, "inherited_effect_action")
        self._inherited_trigger_action = ObservedList(self, "inherited_trigger_action")
        self._inherited_guard_expression = ObservedList(self, "inherited_guard_expression")

    @property
    def source(self) -> None:  # noqa: F821
        """
        Get the source property.

        Returns
        -------
        None
            Value of property source.
        """
        return self._source

    @source.setter
    def source(self, value: None):  # noqa: F821
        """
        Set the source property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "source", value)
        self._source = value

    @property
    def target(self) -> "ActionUsage":  # noqa: F821
        """
        Get the target property.

        Returns
        -------
        "ActionUsage"
            Value of property target.
        """
        return self._target

    @target.setter
    def target(self, value: "ActionUsage"):  # noqa: F821
        """
        Set the target property.

        Parameters
        ----------
        value: "ActionUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "target", value)
        self._target = value

    @property
    def effect_action(self) -> List["ActionUsage"]:  # noqa: F821
        """
        Get the effect action property.

        Returns
        -------
        List["ActionUsage"]
            Value of property effect action.
        """
        return self._effect_action

    @property
    def trigger_action(self) -> List["AcceptActionUsage"]:  # noqa: F821
        """
        Get the trigger action property.

        Returns
        -------
        List["AcceptActionUsage"]
            Value of property trigger action.
        """
        return self._trigger_action

    @property
    def guard_expression(self) -> List["Expression"]:  # noqa: F821
        """
        Get the guard expression property.

        Returns
        -------
        List["Expression"]
            Value of property guard expression.
        """
        return self._guard_expression

    @property
    def succession(self) -> "Succession":  # noqa: F821
        """
        Get the succession property.

        Returns
        -------
        "Succession"
            Value of property succession.
        """
        return self._succession

    @succession.setter
    def succession(self, value: "Succession"):  # noqa: F821
        """
        Set the succession property.

        Parameters
        ----------
        value: "Succession"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "succession", value)
        self._succession = value

    @property
    def inherited_effect_action(self) -> List["ActionUsage"]:  # noqa: F821
        """
        Get the inherited effect action property.

        Returns
        -------
        List["ActionUsage"]
            Value of property inherited effect action.
        """
        return self._inherited_effect_action

    @property
    def inherited_trigger_action(self) -> List["AcceptActionUsage"]:  # noqa: F821
        """
        Get the inherited trigger action property.

        Returns
        -------
        List["AcceptActionUsage"]
            Value of property inherited trigger action.
        """
        return self._inherited_trigger_action

    @property
    def inherited_guard_expression(self) -> List["Expression"]:  # noqa: F821
        """
        Get the inherited guard expression property.

        Returns
        -------
        List["Expression"]
            Value of property inherited guard expression.
        """
        return self._inherited_guard_expression
