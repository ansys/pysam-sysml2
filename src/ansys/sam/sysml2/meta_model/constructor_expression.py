"""Generated constructor expression class from metamodel."""

from .instantiation_expression import InstantiationExpression


class ConstructorExpression(InstantiationExpression):
    """Java class 'com.ansys.metamodel.sysml2.ConstructorExpression'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
