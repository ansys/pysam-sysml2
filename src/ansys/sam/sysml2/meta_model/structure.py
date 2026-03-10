"""Generated structure class from metamodel."""

from .class_ import Class


class Structure(Class):
    """Java class 'com.ansys.medini.metamodel.sysml.Structure'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)
