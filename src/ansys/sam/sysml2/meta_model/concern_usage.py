"""Generated concern usage class from metamodel."""

from __future__ import annotations

from .requirement_usage import RequirementUsage


class ConcernUsage(RequirementUsage):
    """Java class 'com.ansys.metamodel.sysml2.ConcernUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._concern_definition = None

    @property
    def concern_definition(self) -> "ConcernDefinition":  # noqa: F821
        """
        Get the concern definition property.

        Returns
        -------
        "ConcernDefinition"
            Value of property concern definition.
        """
        return self._concern_definition

    @concern_definition.setter
    def concern_definition(self, value: "ConcernDefinition"):  # noqa: F821
        """
        Set the concern_definition property.

        Parameters
        ----------
        value: "ConcernDefinition"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "concern_definition", value)
        self._concern_definition = value
