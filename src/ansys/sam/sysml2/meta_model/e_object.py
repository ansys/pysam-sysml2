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
"""Base class of the metamodel."""

from ansys.sam.sysml2.classes.value_helper import ValueHelper
from ansys.sam.sysml2.observer.observer import ModificationObserver


class EObject:
    """Base class of the metamodel."""

    _observer: ModificationObserver | None

    def __init__(self, element_id: str):
        """
        Construct a new instance.

        Parameters
        ----------
        element_id : str
            Element ID.
        """
        self._id = element_id
        self._identifier = element_id
        self._observer = None
        self._element_hash_map = {}

    def get(self, element_name: str) -> "Element | None":  # noqa: F821
        """
        Find an owned element by its name.

        Parameters
        ----------
        element_name : str
            Element name

        Returns
        -------
        Element
            The Element or None if not found
        """
        from ansys.sam.sysml2.classes.sysml_inherited_element import (
            SysMLInheritedElement,
        )

        hmap = self.__dict__.get("_element_hash_map", {})
        if element_name in hmap:
            child = hmap[element_name]
            owned = self.__dict__.get("_owned_element", [])
            is_owned = any(
                getattr(x, "name", None) == element_name for x in owned if isinstance(x, EObject)
            )
            if is_owned:
                return child
            return SysMLInheritedElement(self, child)

        return None

    @property
    def id(self):
        """Get the id of the element."""
        return self._id

    @id.setter
    def id(self, new_id):
        """Set the id of the element."""
        self._id = new_id
        self._identifier = new_id

    @property
    def identifier(self):
        """Get the identifier of the element."""
        return self._identifier

    def get_value(self):
        """Return the value of the feature."""
        return ValueHelper.get_value_for_sysml_element(self)

    def delete(self):
        """Delete the element from the model via the observer's commit to the server."""
        if self._observer is not None:
            self._observer.delete_element(self.id)
        del self

    def parse_and_set_value(self, value: str):
        """Parse the value and create the valuation part in the Feature."""
        ValueHelper.set_or_update_value(self, "operator", value)

    def set_value(self, new_value: str | int | float | bool):
        """Update the Feature value."""
        ValueHelper.set_or_update_value(self, type(new_value), new_value)
