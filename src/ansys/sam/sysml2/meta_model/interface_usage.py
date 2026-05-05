"""Generated interface usage class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .connection_usage import ConnectionUsage


class InterfaceUsage(ConnectionUsage):
    """Java class 'com.ansys.metamodel.sysml2.InterfaceUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._interface_definition = ObservedList(self, "interface_definition")

    @property
    def interface_definition(self) -> list["InterfaceDefinition"]:  # noqa: F821
        """
        Get the interface definition property.

        Returns
        -------
        list["InterfaceDefinition"]
            Value of property interface definition.
        """
        return self._interface_definition
