"""Generated comment class from metamodel."""

from __future__ import annotations

from .annotating_element import AnnotatingElement


class Comment(AnnotatingElement):
    """Java class 'com.ansys.medini.metamodel.sysml.Comment'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._locale = ""
        self._body = None

    @property
    def locale(self) -> str:  # noqa: F821
        """
        Get the locale property.

        Returns
        -------
        str
            Value of property locale.
        """
        return self._locale

    @locale.setter
    def locale(self, value: str):  # noqa: F821
        """
        Set the locale property.

        Parameters
        ----------
        value: str
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "locale", value)
        self._locale = value

    @property
    def body(self) -> None:  # noqa: F821
        """
        Get the body property.

        Returns
        -------
        None
            Value of property body.
        """
        return self._body

    @body.setter
    def body(self, value: None):  # noqa: F821
        """
        Set the body property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "body", value)
        self._body = value
