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

"""Tool module for SysML elements."""

from ansys.sam.sysml2.tools._feature_chaining import resolve_connector_end


class SysMLTools:
    """Provides tools operating on SysML elements."""

    @staticmethod
    def isinstance(element, element_type: str) -> bool:
        """
        Check the type of an element.

        Parameters
        ----------
        element : SysMLElement
            Element to check.
        element_type : str
            SysML class name.

        Returns
        -------
        bool
            ``True`` if yes, ``False`` otherwise.
        """
        return element.__class__.__name__.split(".")[-1] == element_type

    def resolve_feature_chaining(self, connection, end: str = "source"):
        """
        Resolve a connection end within the connection's own context.

        Parameters
        ----------
        connection : Element | SysMLElement
            Connection (or relationship) whose end is resolved.
        end : str
            Which end to resolve: ``"source"`` (default) or ``"target"``.

        Returns
        -------
        Element | SysMLElement | None
            The resolved representative element, or ``None`` when the end or
            context is missing.
        """
        if end not in ("source", "target"):
            raise ValueError(f"end must be 'source' or 'target', got {end!r}")
        return resolve_connector_end(connection, end)

    def get_connector_ends(self, connection):
        """
        Resolve both ends of a connector at once.

        Parameters
        ----------
        connection : Element | SysMLElement
            Connection (or relationship) whose ends are resolved.

        Returns
        -------
        tuple
            The resolved ``(source, target)`` representatives.
        """
        return (
            resolve_connector_end(connection, "source"),
            resolve_connector_end(connection, "target"),
        )
