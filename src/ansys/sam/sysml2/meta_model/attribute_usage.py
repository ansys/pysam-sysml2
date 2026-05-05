"""Generated attribute usage class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .usage import Usage


class AttributeUsage(Usage):
    """Java class 'com.ansys.metamodel.sysml2.AttributeUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._attribute_definition = ObservedList(self, "attribute_definition")

    @property
    def attribute_definition(self) -> list["DataType"]:  # noqa: F821
        """
        Get the attribute definition property.

        Returns
        -------
        list["DataType"]
            Value of property attribute definition.
        """
        return self._attribute_definition
