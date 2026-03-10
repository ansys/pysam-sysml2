"""Generated invocation expression class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .expression import Expression


class InvocationExpression(Expression):
    """Java class 'com.ansys.medini.metamodel.sysml.InvocationExpression'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._argument = ObservedList(self, "argument")

    @property
    def argument(self) -> List["Expression"]:  # noqa: F821
        """
        Get the argument property.

        Returns
        -------
        List["Expression"]
            Value of property argument.
        """
        return self._argument
