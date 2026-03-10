"""Generated classifier class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .type_ import Type


class Classifier(Type):
    """Java class 'com.ansys.medini.metamodel.sysml.Classifier'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._super_classifier = ObservedList(self, "super_classifier")
        self._owned_subclassification = ObservedList(self, "owned_subclassification")

    @property
    def super_classifier(self) -> List["Classifier"]:  # noqa: F821
        """
        Get the super classifier property.

        Returns
        -------
        List["Classifier"]
            Value of property super classifier.
        """
        return self._super_classifier

    @property
    def owned_subclassification(self) -> List["Subclassification"]:  # noqa: F821
        """
        Get the owned subclassification property.

        Returns
        -------
        List["Subclassification"]
            Value of property owned subclassification.
        """
        return self._owned_subclassification
