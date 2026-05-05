"""Generated disjoining class from metamodel."""

from __future__ import annotations

from .relationship import Relationship


class Disjoining(Relationship):
    """Java class 'com.ansys.metamodel.sysml2.Disjoining'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._disjoining_type = None
        self._owning_type = None
        self._type_disjoined = None

    @property
    def disjoining_type(self) -> "Type":  # noqa: F821
        """
        Get the disjoining type property.

        Returns
        -------
        "Type"
            Value of property disjoining type.
        """
        return self._disjoining_type

    @disjoining_type.setter
    def disjoining_type(self, value: "Type"):  # noqa: F821
        """
        Set the disjoining_type property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "disjoining_type", value)
        self._disjoining_type = value

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
    def type_disjoined(self) -> "Type":  # noqa: F821
        """
        Get the type disjoined property.

        Returns
        -------
        "Type"
            Value of property type disjoined.
        """
        return self._type_disjoined

    @type_disjoined.setter
    def type_disjoined(self, value: "Type"):  # noqa: F821
        """
        Set the type_disjoined property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "type_disjoined", value)
        self._type_disjoined = value
