"""Generated metaclass class from metamodel."""

from .structure import Structure


class Metaclass(Structure):
    """Java class 'com.ansys.metamodel.sysml2.Metaclass'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
