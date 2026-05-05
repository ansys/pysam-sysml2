"""Generated package class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .namespace import Namespace


class Package(Namespace):
    """Java class 'com.ansys.metamodel.sysml2.Package'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._filter_condition = ObservedList(self, "filter_condition")

    @property
    def filter_condition(self) -> list["Expression"]:  # noqa: F821
        """
        Get the filter condition property.

        Returns
        -------
        list["Expression"]
            Value of property filter condition.
        """
        return self._filter_condition
