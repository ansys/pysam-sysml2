"""Generated namespace class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .element import Element


class Namespace(Element):
    """Java class 'com.ansys.metamodel.sysml2.Namespace'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._imported_membership = ObservedList(self, "imported_membership")
        self._member = ObservedList(self, "member")
        self._membership = ObservedList(self, "membership")
        self._owned_import = ObservedList(self, "owned_import")
        self._owned_member = ObservedList(self, "owned_member")
        self._owned_membership = ObservedList(self, "owned_membership")

    @property
    def imported_membership(self) -> list["Membership"]:  # noqa: F821
        """
        Get the imported membership property.

        Returns
        -------
        list["Membership"]
            Value of property imported membership.
        """
        return self._imported_membership

    @property
    def member(self) -> list["Element"]:  # noqa: F821
        """
        Get the member property.

        Returns
        -------
        list["Element"]
            Value of property member.
        """
        return self._member

    @property
    def membership(self) -> list["Membership"]:  # noqa: F821
        """
        Get the membership property.

        Returns
        -------
        list["Membership"]
            Value of property membership.
        """
        return self._membership

    @property
    def owned_import(self) -> list["Import"]:  # noqa: F821
        """
        Get the owned import property.

        Returns
        -------
        list["Import"]
            Value of property owned import.
        """
        return self._owned_import

    @property
    def owned_member(self) -> list["Element"]:  # noqa: F821
        """
        Get the owned member property.

        Returns
        -------
        list["Element"]
            Value of property owned member.
        """
        return self._owned_member

    @property
    def owned_membership(self) -> list["Membership"]:  # noqa: F821
        """
        Get the owned membership property.

        Returns
        -------
        list["Membership"]
            Value of property owned membership.
        """
        return self._owned_membership
