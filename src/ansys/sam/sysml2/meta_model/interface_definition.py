"""Generated interface definition class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .connection_definition import ConnectionDefinition


class InterfaceDefinition(ConnectionDefinition):
    """Java class 'com.ansys.metamodel.sysml2.InterfaceDefinition'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._interface_end = ObservedList(self, "interface_end")

    @property
    def interface_end(self) -> list["PortUsage"]:  # noqa: F821
        """
        Get the interface end property.

        Returns
        -------
        list["PortUsage"]
            Value of property interface end.
        """
        return self._interface_end
