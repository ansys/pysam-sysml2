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

"""Generated item flow class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .connector import Connector
from .step import Step


class ItemFlow(Step, Connector):
    """Java class 'com.ansys.medini.metamodel.sysml.ItemFlow'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._item_type = ObservedList(self, "item_type")
        self._item_feature = None
        self._source_output_feature = None
        self._target_input_feature = None
        self._item_flow_end = ObservedList(self, "item_flow_end")

    @property
    def item_type(self) -> list["Classifier"]:  # noqa: F821
        """
        Get the item type property.

        Returns
        -------
        list["Classifier"]
            Value of property item type.
        """
        return self._item_type

    @property
    def item_feature(self) -> "ItemFeature":  # noqa: F821
        """
        Get the item feature property.

        Returns
        -------
        "ItemFeature"
            Value of property item feature.
        """
        return self._item_feature

    @property
    def source_output_feature(self) -> "Feature":  # noqa: F821
        """
        Get the source output feature property.

        Returns
        -------
        "Feature"
            Value of property source output feature.
        """
        return self._source_output_feature

    @property
    def target_input_feature(self) -> "Feature":  # noqa: F821
        """
        Get the target input feature property.

        Returns
        -------
        "Feature"
            Value of property target input feature.
        """
        return self._target_input_feature

    @property
    def item_flow_end(self) -> list["ItemFlowEnd"]:  # noqa: F821
        """
        Get the item flow end property.

        Returns
        -------
        list["ItemFlowEnd"]
            Value of property item flow end.
        """
        return self._item_flow_end
