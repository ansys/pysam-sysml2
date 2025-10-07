# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
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

"""Unresolved field class."""

from ansys.sam.sysml2.classes.sysml_element import SysMLElement


class UnresolvedField:
    """Provides for resolving unresolved fields."""

    _owner: SysMLElement
    _owning_feature: str
    _element_id: str

    def __init__(self, owner: SysMLElement, owning_feature: str, element_id: str):
        """
        Construct a new instance.

        Parameters
        ----------
        owner : SysMLElement
            Owner element of the unresolved field.
        owning_feature : str
            Name of the owning feature.
        element_id : str
            ID of the missing element.
        """
        self._owner = owner
        self._owning_feature = owning_feature
        self._element_id = element_id

    def get_id(self) -> str:
        """
        Get the missing element ID.

        Returns
        -------
        str
            Missing element ID.
        """
        return self._element_id

    def resolve(self, element: SysMLElement):
        """
        Resolve the fields.

        Parameters
        ----------
        element : SysMLElement
            Missing element.
        """
        field = getattr(self._owner, self._owning_feature, None)
        if isinstance(field, list):
            field.remove(self._element_id)
            field.append(element)
        else:
            field = element
        setattr(self._owner, self._owning_feature, field)
