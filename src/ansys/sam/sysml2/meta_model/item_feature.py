"""Generated item feature class from metamodel."""

from .feature import Feature


class ItemFeature(Feature):
    """Java class 'com.ansys.medini.metamodel.sysml.ItemFeature'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
