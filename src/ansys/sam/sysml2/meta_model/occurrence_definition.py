"""Generated occurrence definition class from metamodel."""

from __future__ import annotations

from .class_ import Class
from .definition import Definition


class OccurrenceDefinition(Definition, Class):
    """Java class 'com.ansys.metamodel.sysml2.OccurrenceDefinition'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._is_individual = False

    @property
    def is_individual(self) -> bool:  # noqa: F821
        """
        Get the is individual property.

        Returns
        -------
        bool
            Value of property is individual.
        """
        return self._is_individual

    @is_individual.setter
    def is_individual(self, value: bool):  # noqa: F821
        """
        Set the is_individual property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_individual", value)
        self._is_individual = value
