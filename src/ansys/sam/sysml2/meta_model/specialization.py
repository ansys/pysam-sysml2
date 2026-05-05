"""Generated specialization class from metamodel."""

from __future__ import annotations

from .relationship import Relationship


class Specialization(Relationship):
    """Java class 'com.ansys.metamodel.sysml2.Specialization'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._general = None
        self._owning_type = None
        self._specific = None

    @property
    def general(self) -> "Type":  # noqa: F821
        """
        Get the general property.

        Returns
        -------
        "Type"
            Value of property general.
        """
        return self._general

    @general.setter
    def general(self, value: "Type"):  # noqa: F821
        """
        Set the general property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "general", value)
        self._general = value

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

    @property
    def specific(self) -> "Type":  # noqa: F821
        """
        Get the specific property.

        Returns
        -------
        "Type"
            Value of property specific.
        """
        return self._specific

    @specific.setter
    def specific(self, value: "Type"):  # noqa: F821
        """
        Set the specific property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "specific", value)
        self._specific = value
