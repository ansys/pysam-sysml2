"""Generated index expression class from metamodel."""

from .operator_expression import OperatorExpression


class IndexExpression(OperatorExpression):
    """Java class 'com.ansys.metamodel.sysml2.IndexExpression'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
