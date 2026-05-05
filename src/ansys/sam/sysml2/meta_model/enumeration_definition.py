"""Generated enumeration definition class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .attribute_definition import AttributeDefinition


class EnumerationDefinition(AttributeDefinition):
    """Java class 'com.ansys.metamodel.sysml2.EnumerationDefinition'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._enumerated_value = ObservedList(self, "enumerated_value")

    @property
    def enumerated_value(self) -> list["EnumerationUsage"]:  # noqa: F821
        """
        Get the enumerated value property.

        Returns
        -------
        list["EnumerationUsage"]
            Value of property enumerated value.
        """
        return self._enumerated_value
