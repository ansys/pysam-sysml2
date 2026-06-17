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
        """List owned + inherited child names alongside normal attributes."""
        base = list(super().__dir__())
        hmap = self.__dict__.get("_element_hash_map", {})
        children = [k for k in hmap if k is not None]
        names = set(list(base) + children)
        if not ValueHelper.is_value_capable(self):
            names.difference_update({"get_value", "set_value", "parse_and_set_value"})
        return sorted(names)

    def __getattr__(self, name):
        """Resolve hash-map children lazily; only fires when normal attribute lookup fails."""
        if name.startswith("__") and name.endswith("__"):
            raise AttributeError(name)
        hmap = self.__dict__.get("_element_hash_map", {})
        if name not in hmap:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
        return self._resolve_child(name, hmap)

    def _resolve_child(self, name, hmap):
        """Return the owned child, or an ``InheritedElement`` proxy, cached under its name."""
        from ansys.sam.sysml2.classes.inherited_element import InheritedElement

        child = hmap[name]
        is_owned = name in self.__dict__.get("_owned_names", set())
        result = child if is_owned else InheritedElement(self, child)
        self.__dict__[name] = result
        return result

    def __setattr__(self, name: str, value: object):
        """Intercept attribute assignment and notify the modification observer."""
        if name != "_observer" and getattr(self, "_observer", None) is not None:
            self._observer.notify(self._id, name, value)
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

    def get(self, element_name: str):
        """Find an owned or inherited child by name (e.g. names with spaces)."""
        hmap = self.__dict__.get("_element_hash_map", {})
        if element_name not in hmap:
            return None
        return self.__getattr__(element_name)

    def delete(self):
        """Delete the element from the model via the observer's commit to the server."""
        if self._observer is not None:
            self._observer.delete_element(self._id)
        del self
