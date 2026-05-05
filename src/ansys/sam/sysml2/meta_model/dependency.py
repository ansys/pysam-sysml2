"""Generated dependency class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .relationship import Relationship


class Dependency(Relationship):
    """Java class 'com.ansys.metamodel.sysml2.Dependency'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._client = ObservedList(self, "client")
        self._supplier = ObservedList(self, "supplier")

    @property
    def client(self) -> list["Element"]:  # noqa: F821
        """
        Get the client property.

        Returns
        -------
        list["Element"]
            Value of property client.
        """
        return self._client

    @property
    def supplier(self) -> list["Element"]:  # noqa: F821
        """
        Get the supplier property.

        Returns
        -------
        list["Element"]
            Value of property supplier.
        """
        return self._supplier
