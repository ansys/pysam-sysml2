"""Generated part definition class from metamodel."""

from .item_definition import ItemDefinition


class PartDefinition(ItemDefinition):
    """Java class 'com.ansys.medini.metamodel.sysml.PartDefinition'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
