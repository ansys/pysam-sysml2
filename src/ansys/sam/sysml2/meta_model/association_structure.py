"""Generated association structure class from metamodel."""

from .association import Association
from .structure import Structure


class AssociationStructure(Association, Structure):
    """Java class 'com.ansys.metamodel.sysml2.AssociationStructure'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
