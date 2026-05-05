"""Generated subclassification class from metamodel."""

from __future__ import annotations

from .specialization import Specialization


class Subclassification(Specialization):
    """Java class 'com.ansys.metamodel.sysml2.Subclassification'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._owning_classifier = None
        self._subclassifier = None
        self._superclassifier = None

    @property
    def owning_classifier(self) -> "Classifier":  # noqa: F821
        """
        Get the owning classifier property.

        Returns
        -------
        "Classifier"
            Value of property owning classifier.
        """
        return self._owning_classifier

    @owning_classifier.setter
    def owning_classifier(self, value: "Classifier"):  # noqa: F821
        """
        Set the owning_classifier property.

        Parameters
        ----------
        value: "Classifier"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_classifier", value)
        self._owning_classifier = value

    @property
    def subclassifier(self) -> "Classifier":  # noqa: F821
        """
        Get the subclassifier property.

        Returns
        -------
        "Classifier"
            Value of property subclassifier.
        """
        return self._subclassifier

    @subclassifier.setter
    def subclassifier(self, value: "Classifier"):  # noqa: F821
        """
        Set the subclassifier property.

        Parameters
        ----------
        value: "Classifier"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "subclassifier", value)
        self._subclassifier = value

    @property
    def superclassifier(self) -> "Classifier":  # noqa: F821
        """
        Get the superclassifier property.

        Returns
        -------
        "Classifier"
            Value of property superclassifier.
        """
        return self._superclassifier

    @superclassifier.setter
    def superclassifier(self, value: "Classifier"):  # noqa: F821
        """
        Set the superclassifier property.

        Parameters
        ----------
        value: "Classifier"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "superclassifier", value)
        self._superclassifier = value
