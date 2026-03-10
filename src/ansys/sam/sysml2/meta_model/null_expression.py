"""Generated null expression class from metamodel."""

from .expression import Expression


class NullExpression(Expression):
    """Java class 'com.ansys.medini.metamodel.sysml.NullExpression'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
