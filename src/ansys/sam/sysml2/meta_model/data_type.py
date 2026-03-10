"""Generated data type class from metamodel."""

from .classifier import Classifier


class DataType(Classifier):
    """Java class 'com.ansys.medini.metamodel.sysml.DataType'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
