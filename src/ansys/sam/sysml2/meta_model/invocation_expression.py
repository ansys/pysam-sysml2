"""Generated invocation expression class from metamodel."""

from .instantiation_expression import InstantiationExpression


class InvocationExpression(InstantiationExpression):
    """Java class 'com.ansys.metamodel.sysml2.InvocationExpression'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
