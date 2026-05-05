"""Generated reference usage class from metamodel."""

from .usage import Usage


class ReferenceUsage(Usage):
    """Java class 'com.ansys.metamodel.sysml2.ReferenceUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
