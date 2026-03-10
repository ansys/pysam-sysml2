"""Generated invariant class from metamodel."""

from .boolean_expression import BooleanExpression


class Invariant(BooleanExpression):
    """Java class 'com.ansys.medini.metamodel.sysml.Invariant'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
