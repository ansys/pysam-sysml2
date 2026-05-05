"""Generated predicate class from metamodel."""

from .function import Function


class Predicate(Function):
    """Java class 'com.ansys.metamodel.sysml2.Predicate'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
