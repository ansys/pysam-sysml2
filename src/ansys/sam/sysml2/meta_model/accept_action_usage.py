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

"""Generated accept action usage class from metamodel."""

from __future__ import annotations

from .action_usage import ActionUsage


class AcceptActionUsage(ActionUsage):
    """Java class 'com.ansys.metamodel.sysml2.AcceptActionUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._payload_argument = None
        self._payload_parameter = None
        self._receiver_argument = None
        self._trigger_action = False

    @property
    def payload_argument(self) -> "Expression":  # noqa: F821
        """
        Get the payload argument property.

        Returns
        -------
        "Expression"
            Value of property payload argument.
        """
        return self._payload_argument

    @property
    def payload_parameter(self) -> "ReferenceUsage":  # noqa: F821
        """
        Get the payload parameter property.

        Returns
        -------
        "ReferenceUsage"
            Value of property payload parameter.
        """
        return self._payload_parameter

    @payload_parameter.setter
    def payload_parameter(self, value: "ReferenceUsage"):  # noqa: F821
        """
        Set the payload_parameter property.

        Parameters
        ----------
        value: "ReferenceUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "payload_parameter", value)
        self._payload_parameter = value

    @property
    def receiver_argument(self) -> "Expression":  # noqa: F821
        """
        Get the receiver argument property.

        Returns
        -------
        "Expression"
            Value of property receiver argument.
        """
        return self._receiver_argument

    @receiver_argument.setter
    def receiver_argument(self, value: "Expression"):  # noqa: F821
        """
        Set the receiver_argument property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "receiver_argument", value)
        self._receiver_argument = value

    @property
    def trigger_action(self) -> bool:  # noqa: F821
        """
        Get the trigger action property.

        Returns
        -------
        bool
            Value of property trigger action.
        """
        return self._trigger_action
