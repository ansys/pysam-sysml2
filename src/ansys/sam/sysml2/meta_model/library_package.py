"""Generated library package class from metamodel."""

from __future__ import annotations

from .package import Package


class LibraryPackage(Package):
    """Java class 'com.ansys.medini.metamodel.sysml.LibraryPackage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._is_standard = False

    @property
    def is_standard(self) -> bool:  # noqa: F821
        """
        Get the is standard property.

        Returns
        -------
        bool
            Value of property is standard.
        """
        return self._is_standard

    @is_standard.setter
    def is_standard(self, value: bool):  # noqa: F821
        """
        Set the is_standard property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_standard", value)
        self._is_standard = value
