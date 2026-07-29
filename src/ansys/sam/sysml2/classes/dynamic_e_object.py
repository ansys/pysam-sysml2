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
"""Dynamic-notation mixin for the generated metamodel."""

from ansys.sam.sysml2.tools.name_utils import NameUtils


class DynamicEObject:
    """Dynamic-notation behaviour mixed in front of a generated metamodel class."""

    def _resolve_property(self, name: str):
        """Return the property matched by a ``_camelCase`` accessor and its descriptor."""
        if not name.startswith("_") or name.startswith("__"):
            return None, None
        prop = NameUtils.to_snake_case(name[1:])
        if name == "_" + prop:
            return None, None
        attr = getattr(type(self), prop, None)
        if isinstance(attr, property):
            return prop, attr
        return None, None

    def __getattr__(self, name):
        """Resolve a ``_camelCase`` property or a named child; only fires on lookup failure."""
        if name.startswith("__") and name.endswith("__"):
            raise AttributeError(name)
        prop, _ = self._resolve_property(name)
        if prop is not None:
            return getattr(self, prop)
        hmap = self.__dict__.get("_element_hash_map", {})
        if name in hmap:
            return self._resolve_child(name, hmap)
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

    def __setattr__(self, name, value):
        """Route a ``_camelCase`` accessor to its property; leave backing fields untouched."""
        prop, attr = self._resolve_property(name)
        if prop is not None:
            if attr.fset is None:
                raise AttributeError(f"'{prop}' is read-only")
            setattr(self, prop, value)
            return
        super().__setattr__(name, value)

    def __dir__(self):
        """Expose the dynamic view: ``_camelCase`` accessors, named children and action methods."""
        from ansys.sam.sysml2.classes.value_helper import ValueHelper

        accessors = set()
        methods = set()
        for klass in type(self).__mro__:
            for attr_name, attr in vars(klass).items():
                if isinstance(attr, property):
                    accessors.add("_" + NameUtils.snake_to_camel(attr_name))
                elif callable(attr) and not attr_name.startswith("_"):
                    methods.add(attr_name)
        children = {name for name in self.__dict__.get("_element_hash_map", {}) if name}
        if not ValueHelper.is_value_capable(self):
            methods.difference_update({"get_value", "set_value"})
        if not getattr(self, "source", None):
            methods.discard("get_source")
        if not getattr(self, "target", None):
            methods.discard("get_target")
        return sorted(accessors | methods | children)
