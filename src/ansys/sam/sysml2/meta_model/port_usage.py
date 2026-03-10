"""Generated port usage class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .occurrence_usage import OccurrenceUsage


class PortUsage(OccurrenceUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.PortUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._port_definition = ObservedList(self, "port_definition")

    @property
    def port_definition(self) -> List["PortDefinition"]:  # noqa: F821
        """
        Get the port definition property.

        Returns
        -------
        List["PortDefinition"]
            Value of property port definition.
        """
        return self._port_definition
