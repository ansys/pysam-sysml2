"""Generated element filter membership class from metamodel."""

from __future__ import annotations

from .owning_membership import OwningMembership


class ElementFilterMembership(OwningMembership):
    """Java class 'com.ansys.metamodel.sysml2.ElementFilterMembership'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._condition = None

    @property
    def condition(self) -> "Expression":  # noqa: F821
        """
        Get the condition property.

        Returns
        -------
        "Expression"
            Value of property condition.
        """
        return self._condition

    @condition.setter
    def condition(self, value: "Expression"):  # noqa: F821
        """
        Set the condition property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "condition", value)
        self._condition = value
