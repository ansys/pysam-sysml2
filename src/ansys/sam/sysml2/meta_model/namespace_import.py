"""Generated namespace import class from metamodel."""

from __future__ import annotations

from .import_ import Import


class NamespaceImport(Import):
    """Java class 'com.ansys.metamodel.sysml2.NamespaceImport'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._imported_namespace = None

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
