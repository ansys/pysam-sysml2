"""Generated item flow class from metamodel."""

from __future__ import annotations

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .connector import Connector
from .step import Step


class ItemFlow(Step, Connector):
    """Java class 'com.ansys.medini.metamodel.sysml.ItemFlow'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._item_feature = None
        self._item_flow_end = ObservedList(self, "item_flow_end")
        self._item_type = ObservedList(self, "item_type")
        self._target_input_feature = None
        self._source_output_feature = None

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
    def item_flow_end(self) -> List["ItemFlowEnd"]:  # noqa: F821
        """
        Get the item flow end property.

        Returns
        -------
        List["ItemFlowEnd"]
            Value of property item flow end.
        """
        return self._item_flow_end

    @property
    def item_type(self) -> List["Classifier"]:  # noqa: F821
        """
        Get the item type property.

        Returns
        -------
        List["Classifier"]
            Value of property item type.
        """
        return self._item_type

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
    def source_output_feature(self) -> "Feature":  # noqa: F821
        """
        Get the source output feature property.

        Returns
        -------
        "Feature"
            Value of property source output feature.
        """
        return self._source_output_feature
