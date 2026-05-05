"""Generated attribute definition class from metamodel."""

from .data_type import DataType
from .definition import Definition


class AttributeDefinition(Definition, DataType):
    """Java class 'com.ansys.metamodel.sysml2.AttributeDefinition'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
