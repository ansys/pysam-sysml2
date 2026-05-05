"""Generated part definition class from metamodel."""

from .item_definition import ItemDefinition


class PartDefinition(ItemDefinition):
    """Java class 'com.ansys.metamodel.sysml2.PartDefinition'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
