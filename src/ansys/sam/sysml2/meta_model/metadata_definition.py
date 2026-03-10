"""Generated metadata definition class from metamodel."""

from .item_definition import ItemDefinition
from .metaclass import Metaclass


class MetadataDefinition(ItemDefinition, Metaclass):
    """Java class 'com.ansys.medini.metamodel.sysml.MetadataDefinition'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
