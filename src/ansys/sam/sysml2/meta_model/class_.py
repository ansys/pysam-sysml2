"""Generated class class from metamodel."""

from .classifier import Classifier


class Class(Classifier):
    """Java class 'com.ansys.metamodel.sysml2.Class'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
