"""Generated port definition class from metamodel."""

from .occurrence_definition import OccurrenceDefinition
from .structure import Structure


class PortDefinition(OccurrenceDefinition, Structure):
    """Java class 'com.ansys.medini.metamodel.sysml.PortDefinition'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
