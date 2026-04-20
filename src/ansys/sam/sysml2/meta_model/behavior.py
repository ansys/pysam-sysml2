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

"""Generated behavior class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .class_ import Class


class Behavior(Class):
    """Java class 'com.ansys.medini.metamodel.sysml.Behavior'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._step = ObservedList(self, "step")
        self._parameter = ObservedList(self, "parameter")
        self._general_parameter = ObservedList(self, "general_parameter")

    @property
    def step(self) -> list["Step"]:  # noqa: F821
        """
        Get the step property.

        Returns
        -------
        list["Step"]
            Value of property step.
        """
        return self._step

    @property
    def parameter(self) -> list["Feature"]:  # noqa: F821
        """
        Get the parameter property.

        Returns
        -------
        list["Feature"]
            Value of property parameter.
        """
        return self._parameter

    @property
    def general_parameter(self) -> list["Feature"]:  # noqa: F821
        """
        Get the general parameter property.

        Returns
        -------
        list["Feature"]
            Value of property general parameter.
        """
        return self._general_parameter
