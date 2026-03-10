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
    """Java class 'com.ansys.medini.metamodel.sysml.SendActionUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

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
