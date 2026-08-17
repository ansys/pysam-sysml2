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

    def _property_for_scripting_field(self, field_name: str):
        """Return the property name a scripting ``_field`` write targets, or ``None``.

        Parameters
        ----------
        field_name : str
            Attribute being written, for example ``_declaredName`` or ``_name``.

        Returns
        -------
        str or None
            The snake_case property name (``declared_name``, ``name``, ...) when the
            class exposes it as a property, otherwise ``None`` (plain private field).
        """
        if not field_name.startswith("_") or field_name.startswith("__"):
            return None
        property_name = NameUtils.to_snake_case(field_name[1:])
        descriptor = getattr(type(self), property_name, None)
        return property_name if isinstance(descriptor, property) else None

    def __init__(self, *args, **kwargs):
        """Build the element, then enable scripting writes once construction is finished."""
        object.__setattr__(self, "_scripting_writes_enabled", False)
        object.__setattr__(self, "_is_writing_through_property", False)
        super().__init__(*args, **kwargs)
        object.__setattr__(self, "_scripting_writes_enabled", True)

    def __getattr__(self, name):
        """Resolve a ``_camelCase`` property or a named child; only fires on lookup failure."""
        if name.startswith("__") and name.endswith("__"):
            raise AttributeError(name)
        property_name = self._property_for_scripting_field(name)
        if property_name is not None:
            return getattr(self, property_name)
        children = self.__dict__.get("_element_hash_map", {})
        if name in children:
            return self._resolve_child(name, children)
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

    def __setattr__(self, name, value):
        """Mirror static write semantics: send a scripting ``_field`` write to its property.

        A read-only property (no setter) raises ``AttributeError`` exactly as in the
        static model; a writable property runs its setter and notifies the observer.
        Internal writes stay raw in two cases: during construction, and while a routed
        setter is writing its own backing field.
        """
        if not self.__dict__.get("_scripting_writes_enabled", False):
            super().__setattr__(name, value)
            return
        if self.__dict__.get("_is_writing_through_property", False):
            super().__setattr__(name, value)
            return
        property_name = self._property_for_scripting_field(name)
        if property_name is None:
            super().__setattr__(name, value)
            return
        object.__setattr__(self, "_is_writing_through_property", True)
        try:
            setattr(self, property_name, value)
        finally:
            object.__setattr__(self, "_is_writing_through_property", False)

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
        return sorted(accessors | methods | children)
