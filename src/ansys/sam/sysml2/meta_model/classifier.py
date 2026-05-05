"""Generated classifier class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .type_ import Type


class Classifier(Type):
    """Java class 'com.ansys.metamodel.sysml2.Classifier'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._owned_subclassification = ObservedList(self, "owned_subclassification")

    @property
    def owned_subclassification(self) -> list["Subclassification"]:  # noqa: F821
        """
        Get the owned subclassification property.

        Returns
        -------
        list["Subclassification"]
            Value of property owned subclassification.
        """
        return self._owned_subclassification
