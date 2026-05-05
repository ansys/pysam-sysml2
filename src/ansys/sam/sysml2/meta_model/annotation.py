"""Generated annotation class from metamodel."""

from __future__ import annotations

from .relationship import Relationship


class Annotation(Relationship):
    """Java class 'com.ansys.metamodel.sysml2.Annotation'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._annotated_element = None
        self._annotating_element = None
        self._owned_annotating_element = None
        self._owning_annotated_element = None
        self._owning_annotating_element = None

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
    def annotating_element(self) -> "AnnotatingElement":  # noqa: F821
        """
        Get the annotating element property.

        Returns
        -------
        "AnnotatingElement"
            Value of property annotating element.
        """
        return self._annotating_element

    @annotating_element.setter
    def annotating_element(self, value: "AnnotatingElement"):  # noqa: F821
        """
        Set the annotating_element property.

        Parameters
        ----------
        value: "AnnotatingElement"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "annotating_element", value)
        self._annotating_element = value

    @property
    def owned_annotating_element(self) -> "AnnotatingElement":  # noqa: F821
        """
        Get the owned annotating element property.

        Returns
        -------
        "AnnotatingElement"
            Value of property owned annotating element.
        """
        return self._owned_annotating_element

    @owned_annotating_element.setter
    def owned_annotating_element(self, value: "AnnotatingElement"):  # noqa: F821
        """
        Set the owned_annotating_element property.

        Parameters
        ----------
        value: "AnnotatingElement"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_annotating_element", value)
        self._owned_annotating_element = value

    @property
    def owning_annotated_element(self) -> "Element":  # noqa: F821
        """
        Get the owning annotated element property.

        Returns
        -------
        "Element"
            Value of property owning annotated element.
        """
        return self._owning_annotated_element

    @owning_annotated_element.setter
    def owning_annotated_element(self, value: "Element"):  # noqa: F821
        """
        Set the owning_annotated_element property.

        Parameters
        ----------
        value: "Element"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_annotated_element", value)
        self._owning_annotated_element = value

    @property
    def owning_annotating_element(self) -> "AnnotatingElement":  # noqa: F821
        """
        Get the owning annotating element property.

        Returns
        -------
        "AnnotatingElement"
            Value of property owning annotating element.
        """
        return self._owning_annotating_element

    @owning_annotating_element.setter
    def owning_annotating_element(self, value: "AnnotatingElement"):  # noqa: F821
        """
        Set the owning_annotating_element property.

        Parameters
        ----------
        value: "AnnotatingElement"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_annotating_element", value)
        self._owning_annotating_element = value
