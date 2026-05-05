"""Generated textual representation class from metamodel."""

from __future__ import annotations

from .annotating_element import AnnotatingElement


class TextualRepresentation(AnnotatingElement):
    """Java class 'com.ansys.metamodel.sysml2.TextualRepresentation'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._body = ""
        self._language = ""
        self._represented_element = None

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
    def language(self) -> str:  # noqa: F821
        """
        Get the language property.

        Returns
        -------
        str
            Value of property language.
        """
        return self._language

    @language.setter
    def language(self, value: str):  # noqa: F821
        """
        Set the language property.

        Parameters
        ----------
        value: str
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "language", value)
        self._language = value

    @property
    def represented_element(self) -> "Element":  # noqa: F821
        """
        Get the represented element property.

        Returns
        -------
        "Element"
            Value of property represented element.
        """
        return self._represented_element

    @represented_element.setter
    def represented_element(self, value: "Element"):  # noqa: F821
        """
        Set the represented_element property.

        Parameters
        ----------
        value: "Element"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "represented_element", value)
        self._represented_element = value
