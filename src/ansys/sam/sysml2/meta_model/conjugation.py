"""Generated conjugation class from metamodel."""

from __future__ import annotations

from .relationship import Relationship


class Conjugation(Relationship):
    """Java class 'com.ansys.metamodel.sysml2.Conjugation'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._conjugated_type = None
        self._original_type = None
        self._owning_type = None

    @property
    def conjugated_type(self) -> "Type":  # noqa: F821
        """
        Get the conjugated type property.

        Returns
        -------
        "Type"
            Value of property conjugated type.
        """
        return self._conjugated_type

    @conjugated_type.setter
    def conjugated_type(self, value: "Type"):  # noqa: F821
        """
        Set the conjugated_type property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "conjugated_type", value)
        self._conjugated_type = value

    @property
    def original_type(self) -> "Type":  # noqa: F821
        """
        Get the original type property.

        Returns
        -------
        "Type"
            Value of property original type.
        """
        return self._original_type

    @original_type.setter
    def original_type(self, value: "Type"):  # noqa: F821
        """
        Set the original_type property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "original_type", value)
        self._original_type = value

    @property
    def owning_type(self) -> "Type":  # noqa: F821
        """
        Get the owning type property.

        Returns
        -------
        "Type"
            Value of property owning type.
        """
        return self._owning_type

    @owning_type.setter
    def owning_type(self, value: "Type"):  # noqa: F821
        """
        Set the owning_type property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_type", value)
        self._owning_type = value
