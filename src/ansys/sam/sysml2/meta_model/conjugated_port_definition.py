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

"""Generated conjugated port definition class from metamodel."""

from __future__ import annotations

from .port_definition import PortDefinition


class ConjugatedPortDefinition(PortDefinition):
    """Java class 'com.ansys.metamodel.sysml2.ConjugatedPortDefinition'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._original_port_definition = None
        self._owned_port_conjugator = None

    @property
    def original_port_definition(self) -> "PortDefinition":  # noqa: F821
        """
        Get the original port definition property.

        Returns
        -------
        "PortDefinition"
            Value of property original port definition.
        """
        return self._original_port_definition

    @original_port_definition.setter
    def original_port_definition(self, value: "PortDefinition"):  # noqa: F821
        """
        Set the original_port_definition property.

        Parameters
        ----------
        value: "PortDefinition"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "original_port_definition", value)
        self._original_port_definition = value

    @property
    def owned_port_conjugator(self) -> "PortConjugation":  # noqa: F821
        """
        Get the owned port conjugator property.

        Returns
        -------
        "PortConjugation"
            Value of property owned port conjugator.
        """
        return self._owned_port_conjugator

    @owned_port_conjugator.setter
    def owned_port_conjugator(self, value: "PortConjugation"):  # noqa: F821
        """
        Set the owned_port_conjugator property.

        Parameters
        ----------
        value: "PortConjugation"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_port_conjugator", value)
        self._owned_port_conjugator = value
