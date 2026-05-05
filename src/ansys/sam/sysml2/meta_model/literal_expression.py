"""Generated literal expression class from metamodel."""

from .expression import Expression


class LiteralExpression(Expression):
    """Java class 'com.ansys.metamodel.sysml2.LiteralExpression'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
