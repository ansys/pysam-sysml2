"""Generated namespace class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .element import Element


class Namespace(Element):
    """Java class 'com.ansys.medini.metamodel.sysml.Namespace'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._owned_member = ObservedList(self, "owned_member")
        self._owned_import = ObservedList(self, "owned_import")
        self._member = ObservedList(self, "member")
        self._owned_membership = ObservedList(self, "owned_membership")

    @property
    def owned_member(self) -> List["Element"]:  # noqa: F821
        """
        Get the owned member property.

        Returns
        -------
        List["Element"]
            Value of property owned member.
        """
        return self._owned_member

    @property
    def owned_import(self) -> List["Import"]:  # noqa: F821
        """
        Get the owned import property.

        Returns
        -------
        List["Import"]
            Value of property owned import.
        """
        return self._owned_import

    @property
    def member(self) -> List["Element"]:  # noqa: F821
        """
        Get the member property.

        Returns
        -------
        List["Element"]
            Value of property member.
        """
        return self._member

    @property
    def owned_membership(self) -> List["Membership"]:  # noqa: F821
        """
        Get the owned membership property.

        Returns
        -------
        List["Membership"]
            Value of property owned membership.
        """
        return self._owned_membership
