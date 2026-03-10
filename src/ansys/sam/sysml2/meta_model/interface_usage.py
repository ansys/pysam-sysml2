"""Generated interface usage class from metamodel."""

from __future__ import annotations

from .connection_usage import ConnectionUsage


class InterfaceUsage(ConnectionUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.InterfaceUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._interface_definition = None

    @property
    def interface_definition(self) -> None:  # noqa: F821
        """
        Get the interface definition property.

        Returns
        -------
        None
            Value of property interface definition.
        """
        return self._interface_definition

    @interface_definition.setter
    def interface_definition(self, value: None):  # noqa: F821
        """
        Set the interface_definition property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "interface_definition", value)
        self._interface_definition = value
