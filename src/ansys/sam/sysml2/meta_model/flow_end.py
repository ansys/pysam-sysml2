"""Generated flow end class from metamodel."""

from .feature import Feature


class FlowEnd(Feature):
    """Java class 'com.ansys.metamodel.sysml2.FlowEnd'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
