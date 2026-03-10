"""Generated item usage class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .occurrence_usage import OccurrenceUsage


class ItemUsage(OccurrenceUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.ItemUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._item_definition = ObservedList(self, "item_definition")

    @property
    def item_definition(self) -> List["Structure"]:  # noqa: F821
        """
        Get the item definition property.

        Returns
        -------
        List["Structure"]
            Value of property item definition.
        """
        return self._item_definition
