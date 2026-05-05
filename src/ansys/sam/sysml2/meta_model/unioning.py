"""Generated unioning class from metamodel."""

from __future__ import annotations

from .relationship import Relationship


class Unioning(Relationship):
    """Java class 'com.ansys.metamodel.sysml2.Unioning'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._type_unioned = None
        self._unioning_type = None

    @property
    def type_unioned(self) -> "Type":  # noqa: F821
        """
        Get the type unioned property.

        Returns
        -------
        "Type"
            Value of property type unioned.
        """
        return self._type_unioned

    @type_unioned.setter
    def type_unioned(self, value: "Type"):  # noqa: F821
        """
        Set the type_unioned property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "type_unioned", value)
        self._type_unioned = value

    @property
    def unioning_type(self) -> "Type":  # noqa: F821
        """
        Get the unioning type property.

        Returns
        -------
        "Type"
            Value of property unioning type.
        """
        return self._unioning_type

    @unioning_type.setter
    def unioning_type(self, value: "Type"):  # noqa: F821
        """
        Set the unioning_type property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "unioning_type", value)
        self._unioning_type = value
