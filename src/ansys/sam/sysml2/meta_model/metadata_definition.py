"""Generated metadata definition class from metamodel."""

from .item_definition import ItemDefinition
from .metaclass import Metaclass


class MetadataDefinition(ItemDefinition, Metaclass):
    """Java class 'com.ansys.metamodel.sysml2.MetadataDefinition'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
