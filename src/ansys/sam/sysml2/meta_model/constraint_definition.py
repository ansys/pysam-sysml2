"""Generated constraint definition class from metamodel."""

from .occurrence_definition import OccurrenceDefinition
from .predicate import Predicate


class ConstraintDefinition(OccurrenceDefinition, Predicate):
    """Java class 'com.ansys.metamodel.sysml2.ConstraintDefinition'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
