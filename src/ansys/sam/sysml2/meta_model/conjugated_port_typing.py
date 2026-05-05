"""Generated conjugated port typing class from metamodel."""

from __future__ import annotations

from .feature_typing import FeatureTyping


class ConjugatedPortTyping(FeatureTyping):
    """Java class 'com.ansys.metamodel.sysml2.ConjugatedPortTyping'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._conjugated_port_definition = None

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
