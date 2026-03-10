"""Generated predicate class from metamodel."""

from .function import Function


class Predicate(Function):
    """Java class 'com.ansys.medini.metamodel.sysml.Predicate'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
