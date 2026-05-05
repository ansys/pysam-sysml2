"""Generated literal infinity class from metamodel."""

from .literal_expression import LiteralExpression


class LiteralInfinity(LiteralExpression):
    """Java class 'com.ansys.metamodel.sysml2.LiteralInfinity'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
