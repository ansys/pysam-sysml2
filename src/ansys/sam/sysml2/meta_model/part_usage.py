"""Generated part usage class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .item_usage import ItemUsage


class PartUsage(ItemUsage):
    """Java class 'com.ansys.metamodel.sysml2.PartUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._part_definition = ObservedList(self, "part_definition")

    @property
    def part_definition(self) -> list["PartDefinition"]:  # noqa: F821
        """
        Get the part definition property.

        Returns
        -------
        list["PartDefinition"]
            Value of property part definition.
        """
        return self._part_definition
