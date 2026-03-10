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

"""Generated expression class from metamodel."""

from __future__ import annotations

from .step import Step


class Expression(Step):
    """Java class 'com.ansys.medini.metamodel.sysml.Expression'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._function = None
        self._result = None

    @property
    def function(self) -> "Function":  # noqa: F821
        """
        Get the function property.

        Returns
        -------
        "Function"
            Value of property function.
        """
        return self._function

    @function.setter
    def function(self, value: "Function"):  # noqa: F821
        """
        Set the function property.

        Parameters
        ----------
        value: "Function"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "function", value)
        self._function = value

    @property
    def result(self) -> None:  # noqa: F821
        """
        Get the result property.

        Returns
        -------
        None
            Value of property result.
        """
        return self._result

    @result.setter
    def result(self, value: None):  # noqa: F821
        """
        Set the result property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "result", value)
        self._result = value
