"""Generated item definition class from metamodel."""

from .occurrence_definition import OccurrenceDefinition
from .structure import Structure


class ItemDefinition(OccurrenceDefinition, Structure):
    """Java class 'com.ansys.medini.metamodel.sysml.ItemDefinition'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
