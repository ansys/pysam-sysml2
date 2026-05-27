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
"""Python base class for SysML elements."""

from __future__ import annotations

from ansys.sam.sysml2.classes.value_helper import ValueHelper
from ansys.sam.sysml2.observer.observer import ModificationObserver


class SysMLElement:
    """Provides the Python base class for all SysML elements."""

    _id: str
    _observer: ModificationObserver | None = None
    _element_hash_map: dict = {}

    def __init__(self, element_id: str) -> None:
        """
        Construct a new SysML element instance with its ID specified.

        Parameters
        ----------
        element_id : str
            Element identifier.
        """
        self._id = element_id

    def __dir__(self):
        """Get the attribute list from the real element."""
        base = super().__dir__()
        hmap = self.__dict__.get("_element_hash_map", {})
        children = [k for k in hmap if k is not None]
        return sorted(set(list(base) + children))

    def __getattr__(self, name):
        """Get the attribute from the real element."""
        from ansys.sam.sysml2.classes.inherited_element import InheritedElement

        if name.startswith("__") and name.endswith("__"):
            raise AttributeError(name)

        hmap = self.__dict__.get("_element_hash_map", {})
        if name in hmap:
            child = hmap[name]
            owned = self.__dict__.get("_ownedElement", [])
            is_owned = any(
                getattr(x, "_name", None) == name for x in owned if isinstance(x, SysMLElement)
            )
            if is_owned:
                return child
            return InheritedElement(self, child)

        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

    def __setattr__(self, name: str, value: object):
        """
        Intercept attribute assignment and notify the modification observer.

        Parameters
        ----------
        name : str
            Name of the key.
        value : object
            Value of the key.
        """
        from ansys.sam.sysml2.classes.inherited_element import InheritedElement

        if name != "_observer" and getattr(self, "_observer", None) is not None:
            self._observer.notify(self._id, name, value)
        if name.startswith("#"):
            name = name[1:]
            if any(name == getattr(x, "_name", None) for x in getattr(self, "_ownedElement", [])):
                super().__setattr__(name, value)
            else:
                super().__setattr__(name, InheritedElement(self, value))

        else:
            super().__setattr__(name, value)

    def get_value(self):
        """Get the value of the feature."""
        return ValueHelper.get_value_for_scripting_element(self)

    def parse_and_set_value(self, value: str):
        """Parse the value and create the valuation part in the feature."""
        ValueHelper.set_or_update_value(self, "operator", value)

    def set_value(self, new_value: str | int | float | bool):
        """Update the feature value."""
        ValueHelper.set_or_update_value(self, type(new_value), new_value)

    def delete(self):
        """Delete the element from the model via the observer's commit to the server."""
        if self._observer is not None:
            self._observer.delete_element(self._id)
        del self
