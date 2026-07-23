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


class SysMLTools:
    """Provides the static class for all SysML tools."""

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

    @staticmethod
    def serialize_expression(value):
        """
        Render a value element to its text form.

        Parameters
        ----------
        value : SysMLElement or Element
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
        owning membership is not set. It resolves the value for both
        the metamodel and scripting flavors.

        Parameters
        ----------
        element : SysMLElement or Element
            Element whose visibility is read.

        Returns
        -------
        VisibilityKind or None
            The owning membership's visibility, or ``None`` when the element has no
            owning membership.
        """
        for attr in ("owning_membership", "owning_feature_membership"):
            membership = getattr(element, attr, None)
            if membership is not None:
                return membership.visibility
        for attr in ("_owningMembership", "_owningFeatureMembership"):
            membership = getattr(element, attr, None)
            if membership is not None:
                return getattr(membership, "_visibility", None)
        return None
