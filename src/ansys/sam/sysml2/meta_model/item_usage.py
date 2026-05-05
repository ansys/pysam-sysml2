"""Generated item usage class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .occurrence_usage import OccurrenceUsage


class ItemUsage(OccurrenceUsage):
    """Java class 'com.ansys.metamodel.sysml2.ItemUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._item_definition = ObservedList(self, "item_definition")

    @property
    def item_definition(self) -> list["Structure"]:  # noqa: F821
        """
        Get the item definition property.

        Returns
        -------
        list["Structure"]
            Value of property item definition.
        """
        return self._item_definition
