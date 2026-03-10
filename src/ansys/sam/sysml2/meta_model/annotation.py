"""Generated annotation class from metamodel."""

from __future__ import annotations

from .relationship import Relationship


class Annotation(Relationship):
    """Java class 'com.ansys.medini.metamodel.sysml.Annotation'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._annotated_element = None
        self._annotating_element = None

    @property
    def annotated_element(self) -> "Element":  # noqa: F821
        """
        Get the annotated element property.

        Returns
        -------
        "Element"
            Value of property annotated element.
        """
        return self._annotated_element

    @annotated_element.setter
    def annotated_element(self, value: "Element"):  # noqa: F821
        """
        Set the annotated_element property.

        Parameters
        ----------
        value: "Element"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "annotated_element", value)
        self._annotated_element = value

    @property
    def annotating_element(self) -> None:  # noqa: F821
        """
        Get the annotating element property.

        Returns
        -------
        None
            Value of property annotating element.
        """
        return self._annotating_element

    @annotating_element.setter
    def annotating_element(self, value: None):  # noqa: F821
        """
        Set the annotating_element property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "annotating_element", value)
        self._annotating_element = value
