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

"""Generated loop action usage class from metamodel."""

from __future__ import annotations

from .action_usage import ActionUsage


class LoopActionUsage(ActionUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.LoopActionUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._body_action = None

    @property
    def body_action(self) -> "ActionUsage":  # noqa: F821
        """
        Get the body action property.

        Returns
        -------
        "ActionUsage"
            Value of property body action.
        """
        return self._body_action

    @body_action.setter
    def body_action(self, value: "ActionUsage"):  # noqa: F821
        """
        Set the body_action property.

        Parameters
        ----------
        value: "ActionUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "body_action", value)
        self._body_action = value
