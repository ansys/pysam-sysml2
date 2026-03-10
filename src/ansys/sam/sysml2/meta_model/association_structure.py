"""Generated association structure class from metamodel."""

from .association import Association
from .structure import Structure


class AssociationStructure(Structure, Association):
    """Java class 'com.ansys.medini.metamodel.sysml.AssociationStructure'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
