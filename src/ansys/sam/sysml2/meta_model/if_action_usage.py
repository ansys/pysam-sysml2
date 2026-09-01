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

"""Generated if action usage class from metamodel."""

from __future__ import annotations

from .action_usage import ActionUsage


class IfActionUsage(ActionUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.IfActionUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._else_action = None
        self._if_argument = None
        self._then_action = None

    @property
    def else_action(self) -> "ActionUsage":  # noqa: F821
        """
        Get the else action property.

        Returns
        -------
        "ActionUsage"
            Value of property else action.
        """
        return self._else_action

    @else_action.setter
    def else_action(self, value: "ActionUsage"):  # noqa: F821
        """
        Set the else_action property.

        Parameters
        ----------
        value: "ActionUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "else_action", value)
        self._else_action = value

    @property
    def if_argument(self) -> "Expression":  # noqa: F821
        """
        Get the if argument property.

        Returns
        -------
        "Expression"
            Value of property if argument.
        """
        return self._if_argument

    @if_argument.setter
    def if_argument(self, value: "Expression"):  # noqa: F821
        """
        Set the if_argument property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "if_argument", value)
        self._if_argument = value

    @property
    def then_action(self) -> "ActionUsage":  # noqa: F821
        """
        Get the then action property.

        Returns
        -------
        "ActionUsage"
            Value of property then action.
        """
        return self._then_action

    @then_action.setter
    def then_action(self, value: "ActionUsage"):  # noqa: F821
        """
        Set the then_action property.

        Parameters
        ----------
        value: "ActionUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "then_action", value)
        self._then_action = value
