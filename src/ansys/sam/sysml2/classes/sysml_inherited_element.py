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

from ansys.sam.sysml2.meta_model.e_object import EObject


class SysMLInheritedElement(EObject):
    """Proxy that exposes an inherited element under its on-the-fly owner."""

    def __init__(self, owner, element):
        """Construct a new instance."""
        super().__init__("")
        self._observer = owner._observer
        self._element = element
        self._element_hash_map = element._element_hash_map
        self.id = element.id
        self.owner = owner

    def __dir__(self):
        """Get the attribute list from the real element."""
        return dir(self._element)

    def get_value(self):
        """Read the value from the wrapped feature (the proxy itself is not a Feature)."""
        return self._element.get_value()

    def __getattr__(self, name):
        """Get the attribute from the real element."""
        if name in ("_observer", "_element", "id", "owner"):
            return super().__getattribute__(name)
        if name.startswith("__") and name.endswith("__"):
            raise AttributeError(name)
        if hasattr(self._element, name):
            value = getattr(self._element, name)
            if isinstance(value, list):
                return value.copy()
            if isinstance(value, EObject):
                return SysMLInheritedElement(self, value)
            return value
        return super().__getattribute__(name)
