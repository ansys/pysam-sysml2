"""Generated owning membership class from metamodel."""

from __future__ import annotations

from .membership import Membership


class OwningMembership(Membership):
    """Java class 'com.ansys.metamodel.sysml2.OwningMembership'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._owned_member_element = None
        self._owned_member_element_id = ""
        self._owned_member_name = ""
        self._owned_member_short_name = ""

    @property
    def owned_member_element(self) -> "Element":  # noqa: F821
        """
        Get the owned member element property.

        Returns
        -------
        "Element"
            Value of property owned member element.
        """
        return self._owned_member_element

    @owned_member_element.setter
    def owned_member_element(self, value: "Element"):  # noqa: F821
        """
        Set the owned_member_element property.

        Parameters
        ----------
        value: "Element"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_member_element", value)
        self._owned_member_element = value

    @property
    def owned_member_element_id(self) -> str:  # noqa: F821
        """
        Get the owned member element id property.

        Returns
        -------
        str
            Value of property owned member element id.
        """
        return self._owned_member_element_id

    @owned_member_element_id.setter
    def owned_member_element_id(self, value: str):  # noqa: F821
        """
        Set the owned_member_element_id property.

        Parameters
        ----------
        value: str
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_member_element_id", value)
        self._owned_member_element_id = value

    @property
    def owned_member_name(self) -> str:  # noqa: F821
        """
        Get the owned member name property.

        Returns
        -------
        str
            Value of property owned member name.
        """
        return self._owned_member_name

    @owned_member_name.setter
    def owned_member_name(self, value: str):  # noqa: F821
        """
        Set the owned_member_name property.

        Parameters
        ----------
        value: str
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_member_name", value)
        self._owned_member_name = value

    @property
    def owned_member_short_name(self) -> str:  # noqa: F821
        """
        Get the owned member short name property.

        Returns
        -------
        str
            Value of property owned member short name.
        """
        return self._owned_member_short_name

    @owned_member_short_name.setter
    def owned_member_short_name(self, value: str):  # noqa: F821
        """
        Set the owned_member_short_name property.

        Parameters
        ----------
        value: str
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_member_short_name", value)
        self._owned_member_short_name = value
