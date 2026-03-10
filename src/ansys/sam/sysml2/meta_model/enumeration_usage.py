"""Generated enumeration usage class from metamodel."""

from __future__ import annotations

from .attribute_usage import AttributeUsage


class EnumerationUsage(AttributeUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.EnumerationUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._enumeration_definition = None

    @property
    def enumeration_definition(self) -> "EnumerationDefinition":  # noqa: F821
        """
        Get the enumeration definition property.

        Returns
        -------
        "EnumerationDefinition"
            Value of property enumeration definition.
        """
        return self._enumeration_definition

    @enumeration_definition.setter
    def enumeration_definition(self, value: "EnumerationDefinition"):  # noqa: F821
        """
        Set the enumeration_definition property.

        Parameters
        ----------
        value: "EnumerationDefinition"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "enumeration_definition", value)
        self._enumeration_definition = value
