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
        return sorted(set(base + children))

    def __getattr__(self, name):
        """Resolve hash-map children lazily; only fires when normal attribute lookup fails."""
        if name.startswith("__") and name.endswith("__"):
            raise AttributeError(name)
        hmap = self.__dict__.get("_element_hash_map", {})
        if name not in hmap:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
        return self._resolve_child(name, hmap)

    def _resolve_child(self, name, hmap):
        """Return the owned child raw, or an ``InheritedElement`` proxy, cached under the child name."""
        from ansys.sam.sysml2.classes.inherited_element import InheritedElement

        child = hmap[name]
        is_owned = name in self.__dict__.get("_owned_names", set())
        result = child if is_owned else InheritedElement(self, child)
        self.__dict__[name] = result
        return result

    @property
    def visibility(self):
        """Deprecated: redirects to the owning membership's visibility (moved in the new metamodel)."""
        own = self.__dict__.get("_visibility")
        if own is not None:
            return own
        om = self.__dict__.get("_owningMembership")
        if om is None:
            return None
        from ansys.sam.sysml2.tools.deprecation import warn_moved

        warn_moved("visibility", "_owningMembership._visibility")
        return getattr(om, "_visibility", None)

    def __setattr__(self, name: str, value: object):
        """Intercept attribute assignment: name is read-only, visibility redirects, others notify."""
        if name in ("name", "_name"):
            from ansys.sam.sysml2.tools.deprecation import raise_readonly

            raise_readonly(name, "_declaredName")
        if name == "visibility":
            from ansys.sam.sysml2.tools.deprecation import warn_moved

            warn_moved("visibility", "_owningMembership._visibility")
            om = self.__dict__.get("_owningMembership")
            if om is not None:
                om._visibility = value
            else:
                object.__setattr__(self, "_visibility", value)
            return
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

    def get_target(self):
        """Return the resolved leaf element pointed to by ``self._target``, or None."""
        return self._resolve_end(getattr(self, "_target", []) or [])

    def get_source(self):
        """Return the resolved leaf element pointed to by ``self._source``, or None."""
        return self._resolve_end(getattr(self, "_source", []) or [])

    def _resolve_end(self, ends):
        """Walk the first end's ``_chainingFeature`` via attribute access; passthrough direct references."""
        if not ends:
            return None
        end = ends[0]
        chain = getattr(end, "_chainingFeature", None) or []
        if not chain:
            return end
        current = getattr(self, "_owner", None)
        for hop in chain:
            if current is None:
                return None
            current = getattr(current, hop._name, None)
        return current

    def delete(self):
        """Delete the element from the model via the observer's commit to the server."""
        if self._observer is not None:
            self._observer.delete_element(self._id)
        del self
