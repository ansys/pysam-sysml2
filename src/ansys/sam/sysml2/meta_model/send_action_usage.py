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

"""Generated send action usage class from metamodel."""

from __future__ import annotations

from .action_usage import ActionUsage


class SendActionUsage(ActionUsage):
    """Java class 'com.ansys.metamodel.sysml2.SendActionUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._payload_argument = None
        self._receiver_argument = None
        self._sender_argument = None

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

    @payload_argument.setter
    def payload_argument(self, value: "Expression"):  # noqa: F821
        """
        Set the payload_argument property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "payload_argument", value)
        self._payload_argument = value

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
    def sender_argument(self) -> "Expression":  # noqa: F821
        """
        Get the sender argument property.

        Returns
        -------
        "Expression"
            Value of property sender argument.
        """
        return self._sender_argument

    @sender_argument.setter
    def sender_argument(self, value: "Expression"):  # noqa: F821
        """
        Set the sender_argument property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "sender_argument", value)
        self._sender_argument = value
