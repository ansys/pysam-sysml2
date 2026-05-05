"""Generated port conjugation class from metamodel."""

from __future__ import annotations

from .conjugation import Conjugation


class PortConjugation(Conjugation):
    """Java class 'com.ansys.metamodel.sysml2.PortConjugation'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._conjugated_port_definition = None
        self._original_port_definition = None

    @property
    def conjugated_port_definition(self) -> "ConjugatedPortDefinition":  # noqa: F821
        """
        Get the conjugated port definition property.

        Returns
        -------
        "ConjugatedPortDefinition"
            Value of property conjugated port definition.
        """
        return self._conjugated_port_definition

    @conjugated_port_definition.setter
    def conjugated_port_definition(self, value: "ConjugatedPortDefinition"):  # noqa: F821
        """
        Set the conjugated_port_definition property.

        Parameters
        ----------
        value: "ConjugatedPortDefinition"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "conjugated_port_definition", value)
        self._conjugated_port_definition = value

    @property
    def original_port_definition(self) -> "PortDefinition":  # noqa: F821
        """
        Get the original port definition property.

        Returns
        -------
        "PortDefinition"
            Value of property original port definition.
        """
        return self._original_port_definition

    @original_port_definition.setter
    def original_port_definition(self, value: "PortDefinition"):  # noqa: F821
        """
        Set the original_port_definition property.

        Parameters
        ----------
        value: "PortDefinition"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "original_port_definition", value)
        self._original_port_definition = value
