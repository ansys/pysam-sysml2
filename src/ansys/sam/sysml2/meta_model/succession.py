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

"""Generated succession class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .connector import Connector


class Succession(Connector):
    """Java class 'com.ansys.medini.metamodel.sysml.Succession'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._guard_expression = ObservedList(self, "guard_expression")
        self._trigger_step = ObservedList(self, "trigger_step")
        self._transition_step = None
        self._effect_step = ObservedList(self, "effect_step")

    @property
    def guard_expression(self) -> list["Expression"]:  # noqa: F821
        """
        Get the guard expression property.

        Returns
        -------
        list["Expression"]
            Value of property guard expression.
        """
        return self._guard_expression

    @property
    def trigger_step(self) -> list["Step"]:  # noqa: F821
        """
        Get the trigger step property.

        Returns
        -------
        list["Step"]
            Value of property trigger step.
        """
        return self._trigger_step

    @property
    def transition_step(self) -> "Step":  # noqa: F821
        """
        Get the transition step property.

        Returns
        -------
        "Step"
            Value of property transition step.
        """
        return self._transition_step

    @transition_step.setter
    def transition_step(self, value: "Step"):  # noqa: F821
        """
        Set the transition_step property.

        Parameters
        ----------
        value: "Step"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "transition_step", value)
        self._transition_step = value

    @property
    def effect_step(self) -> list["Step"]:  # noqa: F821
        """
        Get the effect step property.

        Returns
        -------
        list["Step"]
            Value of property effect step.
        """
        return self._effect_step
