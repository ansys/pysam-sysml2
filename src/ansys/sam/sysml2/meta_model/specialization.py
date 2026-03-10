"""Generated specialization class from metamodel."""

from __future__ import annotations

from .relationship import Relationship


class Specialization(Relationship):
    """Java class 'com.ansys.medini.metamodel.sysml.Specialization'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._owning_type = None
        self._specific = None
        self._general = None

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
    def specific(self) -> None:  # noqa: F821
        """
        Get the specific property.

        Returns
        -------
        None
            Value of property specific.
        """
        return self._specific

    @specific.setter
    def specific(self, value: None):  # noqa: F821
        """
        Set the specific property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "specific", value)
        self._specific = value

    @property
    def general(self) -> None:  # noqa: F821
        """
        Get the general property.

        Returns
        -------
        None
            Value of property general.
        """
        return self._general

    @general.setter
    def general(self, value: None):  # noqa: F821
        """
        Set the general property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "general", value)
        self._general = value
