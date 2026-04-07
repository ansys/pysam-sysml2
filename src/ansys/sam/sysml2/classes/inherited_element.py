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
"""A proxy class for the element that is not created yet."""

from ansys.sam.sysml2.classes.sysml_element import SysMLElement


def build_composed_name(owner, element, is_inherited):
    """
    Build a composed name for the inherited element.

    Parameters
    ----------
    owner : SysMLElement
        The owner of the inherited element.
    element : SysMLElement
        The inherited element.
    is_inherited : bool
        Whether the element is inherited or not.

    Returns
    -------
    str
         The composed name for the inherited element.
    """
    is_contained_in_inherited_element = isinstance(owner, InheritedElement)
    if is_inherited:
        is_inherited = (
            element in getattr(owner, "_inheritedFeature", []) or is_contained_in_inherited_element
        )
        if is_contained_in_inherited_element:
            return f"{owner._id}/?{element._identifier}"
        return f"{build_composed_name(owner._owner, owner, is_inherited)}/?{element._id}"
    return ""


class InheritedElement(SysMLElement):
    """A proxy class for the element that is not created yet."""

    def __init__(self, owner, element):
        """Construct a new instance."""
        # self._observer = owner._observer
        self._element = element
        self._id = build_composed_name(owner, element, True)
        self._owner = owner

    def __dir__(self):
        """Get the attribute list from the real element."""
        return dir(self._element)

    def __getattr__(self, name):
        """Get the attribute from the real element."""
        if name in ("_observer", "_element", "_id", "_owner"):
            return super().__getattribute__(name)
        if name.startswith("__") and name.endswith("__"):
            raise AttributeError(name)
        if hasattr(self._element, name):
            value = getattr(self._element, name)
            if isinstance(value, list):
                return value.copy()
            if isinstance(value, SysMLElement):
                return InheritedElement(self, value)
            return value
        return super().__getattribute__(name)
