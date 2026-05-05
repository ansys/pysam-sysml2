"""Generated select expression class from metamodel."""

from .operator_expression import OperatorExpression


class SelectExpression(OperatorExpression):
    """Java class 'com.ansys.metamodel.sysml2.SelectExpression'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
