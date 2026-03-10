"""Generated import class from metamodel."""

from __future__ import annotations

from .relationship import Relationship


class Import(Relationship):
    """Java class 'com.ansys.medini.metamodel.sysml.Import'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._is_recursive = False
        self._imported_namespace = None

    @property
    def is_recursive(self) -> bool:  # noqa: F821
        """
        Get the is recursive property.

        Returns
        -------
        bool
            Value of property is recursive.
        """
        return self._is_recursive

    @is_recursive.setter
    def is_recursive(self, value: bool):  # noqa: F821
        """
        Set the is_recursive property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_recursive", value)
        self._is_recursive = value

    @property
    def imported_namespace(self) -> "Namespace":  # noqa: F821
        """
        Get the imported namespace property.

        Returns
        -------
        "Namespace"
            Value of property imported namespace.
        """
        return self._imported_namespace

    @imported_namespace.setter
    def imported_namespace(self, value: "Namespace"):  # noqa: F821
        """
        Set the imported_namespace property.

        Parameters
        ----------
        value: "Namespace"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "imported_namespace", value)
        self._imported_namespace = value
