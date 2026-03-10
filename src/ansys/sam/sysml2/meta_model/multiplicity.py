"""Generated multiplicity class from metamodel."""

from .feature import Feature


class Multiplicity(Feature):
    """Java class 'com.ansys.medini.metamodel.sysml.Multiplicity'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
