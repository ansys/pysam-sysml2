"""Generated reference usage class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .usage import Usage


class ReferenceUsage(Usage):
    """Java class 'com.ansys.medini.metamodel.sysml.ReferenceUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._reference_type = ObservedList(self, "reference_type")

    @property
    def reference_type(self) -> List["Classifier"]:  # noqa: F821
        """
        Get the reference type property.

        Returns
        -------
        List["Classifier"]
            Value of property reference type.
        """
        return self._reference_type
