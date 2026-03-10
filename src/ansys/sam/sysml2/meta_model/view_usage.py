"""Generated view usage class from metamodel."""

from __future__ import annotations

from .part_usage import PartUsage


class ViewUsage(PartUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.ViewUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._view_definition = None

    @property
    def view_definition(self) -> None:  # noqa: F821
        """
        Get the view definition property.

        Returns
        -------
        None
            Value of property view definition.
        """
        return self._view_definition

    @view_definition.setter
    def view_definition(self, value: None):  # noqa: F821
        """
        Set the view_definition property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "view_definition", value)
        self._view_definition = value
