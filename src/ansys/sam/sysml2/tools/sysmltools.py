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

from ansys.sam.sysml2.tools.feature_chaining_resolver import FeatureChainingResolver


class SysMLTools:
    """Provides tools operating on SysML elements."""

    @staticmethod
    def isinstance(element, element_type: str) -> bool:
        """
        Check the type of an element.

        Parameters
        ----------
        element : Element
            Element to check.
        element_type : str
            SysML class name.

        Returns
        -------
        bool
            ``True`` if yes, ``False`` otherwise.
        """
        return element.__class__.__name__.split(".")[-1] == element_type

    @staticmethod
    def serialize_expression(value):
        """
        Render a value element to its text form.

        Parameters
        ----------
        value : Element
            Value element returned by ``get_value`` (a literal or an operator expression).

        Returns
        -------
        str or None
            The rendered text (for example ``"1 + 1"`` or ``"5 [kg]"``), or ``None`` when
            ``value`` is ``None``.
        """
        from ansys.sam.sysml2.classes.value_helper import ValueHelper

        return ValueHelper.serialize(value)

    @staticmethod
    def get_element_visibility(element):
        """
        Return the visibility of an element, read from its owning membership.

        Visibility lives on the membership that owns the element. That membership is an
        ``OwningMembership`` for most elements and a ``FeatureMembership`` for features,
        so this helper falls back to the owning feature membership when the generic
        owning membership is not set.

        Parameters
        ----------
        element : Element
            Element whose visibility is read.

        Returns
        -------
        VisibilityKind or None
            The owning membership's visibility, or ``None`` when the element has no
            owning membership.
        """
        for attribute_name in ("owning_membership", "owning_feature_membership"):
            membership = getattr(element, attribute_name, None)
            if membership is not None:
                return membership.visibility
        return None

    @staticmethod
    def set_element_visibility(element, visibility):
        """
        Set the visibility of an element on its owning membership.

        Visibility lives on the membership that owns the element (an ``OwningMembership``
        for most elements, a ``FeatureMembership`` for features). This helper writes the
        value on that membership. Use :meth:`get_element_visibility` to read it back.

        Parameters
        ----------
        element : Element
            Element whose visibility is set.
        visibility : VisibilityKind
            New visibility value.

        Raises
        ------
        AttributeError
            If the element has no owning membership to store the value on.
        """
        for attribute_name in ("owning_membership", "owning_feature_membership"):
            membership = getattr(element, attribute_name, None)
            if membership is not None:
                membership.visibility = visibility
                return
        raise AttributeError("Cannot set visibility: the element has no owning membership.")

    @staticmethod
    def parse_and_set_value(feature, expression: str):
        """
        Parse an expression and set it as the feature's value.

        The text is sent as-is to the server, which builds the corresponding SysML v2
        expression (for example a unit expression, an arithmetic expression, or a
        reference expression). Use :meth:`serialize_expression` to render the resulting
        value element back to text.

        Parameters
        ----------
        feature : Element
            Feature whose value is set or updated.
        expression : str
            Expression text to parse (for example ``"10 [m]"`` or ``"5 + 5"``).
        """
        from ansys.sam.sysml2.classes.value_helper import ValueHelper

        ValueHelper.set_or_update_value(feature, "operator", expression)

    @staticmethod
    def resolve_feature_chaining(connection, end: str = "source"):
        """
        Resolve a connection end within the connection's own context.

        Parameters
        ----------
        connection : Element
            Connection (or relationship) whose end is resolved.
        end : str
            Which end to resolve: ``"source"`` (default) or ``"target"``.

        Returns
        -------
        Element or None
            The resolved representative element, or ``None`` when the end or
            context is missing.
        """
        if end not in ("source", "target"):
            raise ValueError(f"end must be 'source' or 'target', got {end!r}")
        return FeatureChainingResolver(connection).resolve_connector_end(end)

    @staticmethod
    def get_connector_ends(connection):
        """
        Resolve both ends of a connector at once.

        Parameters
        ----------
        connection : Element
            Connection (or relationship) whose ends are resolved.

        Returns
        -------
        tuple
            The resolved ``(source, target)`` representatives.
        """
        resolver = FeatureChainingResolver(connection)
        return (
            resolver.resolve_connector_end("source"),
            resolver.resolve_connector_end("target"),
        )
