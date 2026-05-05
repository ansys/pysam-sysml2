"""Generated comment class from metamodel."""

from __future__ import annotations

from .annotating_element import AnnotatingElement


class Comment(AnnotatingElement):
    """Java class 'com.ansys.metamodel.sysml2.Comment'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._body = ""
        self._locale = ""

    @property
    def body(self) -> str:  # noqa: F821
        """
        Get the body property.

        Returns
        -------
        str
            Value of property body.
        """
        return self._body

    @body.setter
    def body(self, value: str):  # noqa: F821
        """
        Set the body property.

        Parameters
        ----------
        value: str
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "body", value)
        self._body = value

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
