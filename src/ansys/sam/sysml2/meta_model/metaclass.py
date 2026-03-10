"""Generated metaclass class from metamodel."""

from .structure import Structure


class Metaclass(Structure):
    """Java class 'com.ansys.medini.metamodel.sysml.Metaclass'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
