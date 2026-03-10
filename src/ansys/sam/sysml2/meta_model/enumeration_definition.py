"""Generated enumeration definition class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .attribute_definition import AttributeDefinition


class EnumerationDefinition(AttributeDefinition):
    """Java class 'com.ansys.medini.metamodel.sysml.EnumerationDefinition'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._enumerated_value = ObservedList(self, "enumerated_value")

    @property
    def enumerated_value(self) -> List["EnumerationUsage"]:  # noqa: F821
        """
        Get the enumerated value property.

        Returns
        -------
        List["EnumerationUsage"]
            Value of property enumerated value.
        """
        return self._enumerated_value
