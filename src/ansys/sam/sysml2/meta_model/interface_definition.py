"""Generated interface definition class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .connection_definition import ConnectionDefinition


class InterfaceDefinition(ConnectionDefinition):
    """Java class 'com.ansys.medini.metamodel.sysml.InterfaceDefinition'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._interface_end = ObservedList(self, "interface_end")

    @property
    def interface_end(self) -> List["PortUsage"]:  # noqa: F821
        """
        Get the interface end property.

        Returns
        -------
        List["PortUsage"]
            Value of property interface end.
        """
        return self._interface_end
