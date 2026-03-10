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

"""Generated state definition class from metamodel."""

from __future__ import annotations

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .action_definition import ActionDefinition


class StateDefinition(ActionDefinition):
    """Java class 'com.ansys.medini.metamodel.sysml.StateDefinition'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._set_exit_action = False
        self._state = ObservedList(self, "state")
        self._exit_action = None
        self._do_action = None
        self._set_is_parallel = False
        self._set_do_action = False
        self._entry_action = None
        self._is_parallel = False
        self._set_entry_action = False

    @property
    def set_exit_action(self) -> bool:  # noqa: F821
        """
        Get the set exit action property.

        Returns
        -------
        bool
            Value of property set exit action.
        """
        return self._set_exit_action

    @property
    def state(self) -> List["StateUsage"]:  # noqa: F821
        """
        Get the state property.

        Returns
        -------
        List["StateUsage"]
            Value of property state.
        """
        return self._state

    @property
    def exit_action(self) -> None:  # noqa: F821
        """
        Get the exit action property.

        Returns
        -------
        None
            Value of property exit action.
        """
        return self._exit_action

    @exit_action.setter
    def exit_action(self, value: None):  # noqa: F821
        """
        Set the exit_action property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "exit_action", value)
        self._exit_action = value

    @property
    def do_action(self) -> "ActionUsage":  # noqa: F821
        """
        Get the do action property.

        Returns
        -------
        "ActionUsage"
            Value of property do action.
        """
        return self._do_action

    @do_action.setter
    def do_action(self, value: "ActionUsage"):  # noqa: F821
        """
        Set the do_action property.

        Parameters
        ----------
        value: "ActionUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "do_action", value)
        self._do_action = value

    @property
    def set_is_parallel(self) -> bool:  # noqa: F821
        """
        Get the set is parallel property.

        Returns
        -------
        bool
            Value of property set is parallel.
        """
        return self._set_is_parallel

    @property
    def set_do_action(self) -> bool:  # noqa: F821
        """
        Get the set do action property.

        Returns
        -------
        bool
            Value of property set do action.
        """
        return self._set_do_action

    @property
    def entry_action(self) -> "ActionUsage":  # noqa: F821
        """
        Get the entry action property.

        Returns
        -------
        "ActionUsage"
            Value of property entry action.
        """
        return self._entry_action

    @entry_action.setter
    def entry_action(self, value: "ActionUsage"):  # noqa: F821
        """
        Set the entry_action property.

        Parameters
        ----------
        value: "ActionUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "entry_action", value)
        self._entry_action = value

    @property
    def is_parallel(self) -> bool:  # noqa: F821
        """
        Get the is parallel property.

        Returns
        -------
        bool
            Value of property is parallel.
        """
        return self._is_parallel

    @is_parallel.setter
    def is_parallel(self, value: bool):  # noqa: F821
        """
        Set the is_parallel property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_parallel", value)
        self._is_parallel = value

    @property
    def set_entry_action(self) -> bool:  # noqa: F821
        """
        Get the set entry action property.

        Returns
        -------
        bool
            Value of property set entry action.
        """
        return self._set_entry_action
