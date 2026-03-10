"""Generated class class from metamodel."""

from .classifier import Classifier


class Class(Classifier):
    """Java class 'com.ansys.medini.metamodel.sysml.Class'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
