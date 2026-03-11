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

"""Generated feature value class from metamodel."""

from __future__ import annotations

from .membership import Membership


class FeatureValue(Membership):
    """Java class 'com.ansys.medini.metamodel.sysml.FeatureValue'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._value = None
        self._set_is_initial = False
        self._is_default = False
        self._set_is_default = False
        self._is_initial = False

    @property
    def value(self) -> "Expression":  # noqa: F821
        """
        Get the value property.

        Returns
        -------
        "Expression"
            Value of property value.
        """
        return self._value

    @value.setter
    def value(self, value: "Expression"):  # noqa: F821
        """
        Set the value property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "value", value)
        self._value = value

    @property
    def set_is_initial(self) -> bool:  # noqa: F821
        """
        Get the set is initial property.

        Returns
        -------
        bool
            Value of property set is initial.
        """
        return self._set_is_initial

    @property
    def is_default(self) -> bool:  # noqa: F821
        """
        Get the is default property.

        Returns
        -------
        bool
            Value of property is default.
        """
        return self._is_default

    @is_default.setter
    def is_default(self, value: bool):  # noqa: F821
        """
        Set the is_default property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_default", value)
        self._is_default = value

    @property
    def set_is_default(self) -> bool:  # noqa: F821
        """
        Get the set is default property.

        Returns
        -------
        bool
            Value of property set is default.
        """
        return self._set_is_default

    @property
    def is_initial(self) -> bool:  # noqa: F821
        """
        Get the is initial property.

        Returns
        -------
        bool
            Value of property is initial.
        """
        return self._is_initial

    @is_initial.setter
    def is_initial(self, value: bool):  # noqa: F821
        """
        Set the is_initial property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_initial", value)
        self._is_initial = value
