"""Generated import class from metamodel."""

from __future__ import annotations

from .relationship import Relationship


class Import(Relationship):
    """Java class 'com.ansys.metamodel.sysml2.Import'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._import_owning_namespace = None
        self._imported_element = None
        self._visibility = None
        self._is_import_all = False
        self._is_recursive = False

    @property
    def import_owning_namespace(self) -> "Namespace":  # noqa: F821
        """
        Get the import owning namespace property.

        Returns
        -------
        "Namespace"
            Value of property import owning namespace.
        """
        return self._import_owning_namespace

    @import_owning_namespace.setter
    def import_owning_namespace(self, value: "Namespace"):  # noqa: F821
        """
        Set the import_owning_namespace property.

        Parameters
        ----------
        value: "Namespace"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "import_owning_namespace", value)
        self._import_owning_namespace = value

    @property
    def imported_element(self) -> "Element":  # noqa: F821
        """
        Get the imported element property.

        Returns
        -------
        "Element"
            Value of property imported element.
        """
        return self._imported_element

    @imported_element.setter
    def imported_element(self, value: "Element"):  # noqa: F821
        """
        Set the imported_element property.

        Parameters
        ----------
        value: "Element"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "imported_element", value)
        self._imported_element = value

    @property
    def visibility(self) -> "VisibilityKind":  # noqa: F821
        """
        Get the visibility property.

        Returns
        -------
        "VisibilityKind"
            Value of property visibility.
        """
        return self._visibility

    @visibility.setter
    def visibility(self, value: "VisibilityKind"):  # noqa: F821
        """
        Set the visibility property.

        Parameters
        ----------
        value: "VisibilityKind"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "visibility", value)
        self._visibility = value

    @property
    def is_import_all(self) -> bool:  # noqa: F821
        """
        Get the is import all property.

        Returns
        -------
        bool
            Value of property is import all.
        """
        return self._is_import_all

    @is_import_all.setter
    def is_import_all(self, value: bool):  # noqa: F821
        """
        Set the is_import_all property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_import_all", value)
        self._is_import_all = value

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
