"""Generated expose class from metamodel."""

from .import_ import Import


class Expose(Import):
    """Java class 'com.ansys.metamodel.sysml2.Expose'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
