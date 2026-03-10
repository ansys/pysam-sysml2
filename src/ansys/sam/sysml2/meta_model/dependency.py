"""Generated dependency class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .relationship import Relationship


class Dependency(Relationship):
    """Java class 'com.ansys.medini.metamodel.sysml.Dependency'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._supplier = ObservedList(self, "supplier")
        self._client = ObservedList(self, "client")

    @property
    def supplier(self) -> List["Element"]:  # noqa: F821
        """
        Get the supplier property.

        Returns
        -------
        List["Element"]
            Value of property supplier.
        """
        return self._supplier

    @property
    def client(self) -> List["Element"]:  # noqa: F821
        """
        Get the client property.

        Returns
        -------
        List["Element"]
            Value of property client.
        """
        return self._client
