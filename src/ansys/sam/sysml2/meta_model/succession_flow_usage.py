"""Generated succession flow usage class from metamodel."""

from .flow_usage import FlowUsage
from .succession_flow import SuccessionFlow


class SuccessionFlowUsage(FlowUsage, SuccessionFlow):
    """Java class 'com.ansys.metamodel.sysml2.SuccessionFlowUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)
