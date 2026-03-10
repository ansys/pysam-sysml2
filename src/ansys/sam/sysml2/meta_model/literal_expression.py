"""Generated literal expression class from metamodel."""

from .expression import Expression


class LiteralExpression(Expression):
    """Java class 'com.ansys.medini.metamodel.sysml.LiteralExpression'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
