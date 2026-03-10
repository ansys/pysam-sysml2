"""Generated attribute definition class from metamodel."""

from .data_type import DataType
from .definition import Definition


class AttributeDefinition(Definition, DataType):
    """Java class 'com.ansys.medini.metamodel.sysml.AttributeDefinition'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
