"""Generated port usage class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .occurrence_usage import OccurrenceUsage


class PortUsage(OccurrenceUsage):
    """Java class 'com.ansys.metamodel.sysml2.PortUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._port_definition = ObservedList(self, "port_definition")

    @property
    def port_definition(self) -> list["PortDefinition"]:  # noqa: F821
        """
        Get the port definition property.

        Returns
        -------
        list["PortDefinition"]
            Value of property port definition.
        """
        return self._port_definition
