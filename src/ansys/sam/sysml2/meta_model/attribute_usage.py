"""Generated attribute usage class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .usage import Usage


class AttributeUsage(Usage):
    """Java class 'com.ansys.medini.metamodel.sysml.AttributeUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._attribute_definition = ObservedList(self, "attribute_definition")

    @property
    def attribute_definition(self) -> List["DataType"]:  # noqa: F821
        """
        Get the attribute definition property.

        Returns
        -------
        List["DataType"]
            Value of property attribute definition.
        """
        return self._attribute_definition
