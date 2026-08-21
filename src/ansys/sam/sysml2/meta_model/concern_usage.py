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

"""Generated concern usage class from metamodel."""

from __future__ import annotations

from .requirement_usage import RequirementUsage


class ConcernUsage(RequirementUsage):
    """Java class 'com.ansys.metamodel.sysml2.ConcernUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._concern_definition = None

    @property
    def concern_definition(self) -> "ConcernDefinition":  # noqa: F821
        """
        Get the concern definition property.

        Returns
        -------
        "ConcernDefinition"
            Value of property concern definition.
        """
        return self._concern_definition

    @concern_definition.setter
    def concern_definition(self, value: "ConcernDefinition"):  # noqa: F821
        """
        Set the concern_definition property.

        Parameters
        ----------
        value: "ConcernDefinition"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "concern_definition", value)
        self._concern_definition = value
