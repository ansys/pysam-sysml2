"""Generated namespace expose class from metamodel."""

from .expose import Expose
from .namespace_import import NamespaceImport


class NamespaceExpose(Expose, NamespaceImport):
    """Java class 'com.ansys.metamodel.sysml2.NamespaceExpose'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
