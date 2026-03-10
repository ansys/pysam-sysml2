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

"""Generated while loop action usage class from metamodel."""

from __future__ import annotations

from .loop_action_usage import LoopActionUsage


class WhileLoopActionUsage(LoopActionUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.WhileLoopActionUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._while_argument = None
        self._until_argument = None

    @property
    def while_argument(self) -> None:  # noqa: F821
        """
        Get the while argument property.

        Returns
        -------
        None
            Value of property while argument.
        """
        return self._while_argument

    @while_argument.setter
    def while_argument(self, value: None):  # noqa: F821
        """
        Set the while_argument property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "while_argument", value)
        self._while_argument = value

    @property
    def until_argument(self) -> "Expression":  # noqa: F821
        """
        Get the until argument property.

        Returns
        -------
        "Expression"
            Value of property until argument.
        """
        return self._until_argument

    @until_argument.setter
    def until_argument(self, value: "Expression"):  # noqa: F821
        """
        Set the until_argument property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "until_argument", value)
        self._until_argument = value
