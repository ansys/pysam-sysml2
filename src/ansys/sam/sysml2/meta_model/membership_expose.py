"""Generated membership expose class from metamodel."""

from .expose import Expose
from .membership_import import MembershipImport


class MembershipExpose(Expose, MembershipImport):
    """Java class 'com.ansys.metamodel.sysml2.MembershipExpose'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
