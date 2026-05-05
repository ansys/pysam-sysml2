"""Generated membership class from metamodel."""

from __future__ import annotations

from .relationship import Relationship


class Membership(Relationship):
    """Java class 'com.ansys.metamodel.sysml2.Membership'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._member_element = None
        self._member_element_id = ""
        self._member_name = ""
        self._member_short_name = ""
        self._membership_owning_namespace = None
        self._visibility = None
        self._distinguishable_from = False

    @property
    def member_element(self) -> "Element":  # noqa: F821
        """
        Get the member element property.

        Returns
        -------
        "Element"
            Value of property member element.
        """
        return self._member_element

    @member_element.setter
    def member_element(self, value: "Element"):  # noqa: F821
        """
        Set the member_element property.

        Parameters
        ----------
        value: "Element"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "member_element", value)
        self._member_element = value

    @property
    def member_element_id(self) -> str:  # noqa: F821
        """
        Get the member element id property.

        Returns
        -------
        str
            Value of property member element id.
        """
        return self._member_element_id

    @member_element_id.setter
    def member_element_id(self, value: str):  # noqa: F821
        """
        Set the member_element_id property.

        Parameters
        ----------
        value: str
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "member_element_id", value)
        self._member_element_id = value

    @property
    def member_name(self) -> str:  # noqa: F821
        """
        Get the member name property.

        Returns
        -------
        str
            Value of property member name.
        """
        return self._member_name

    @member_name.setter
    def member_name(self, value: str):  # noqa: F821
        """
        Set the member_name property.

        Parameters
        ----------
        value: str
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "member_name", value)
        self._member_name = value

    @property
    def member_short_name(self) -> str:  # noqa: F821
        """
        Get the member short name property.

        Returns
        -------
        str
            Value of property member short name.
        """
        return self._member_short_name

    @member_short_name.setter
    def member_short_name(self, value: str):  # noqa: F821
        """
        Set the member_short_name property.

        Parameters
        ----------
        value: str
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "member_short_name", value)
        self._member_short_name = value

    @property
    def membership_owning_namespace(self) -> "Namespace":  # noqa: F821
        """
        Get the membership owning namespace property.

        Returns
        -------
        "Namespace"
            Value of property membership owning namespace.
        """
        return self._membership_owning_namespace

    @membership_owning_namespace.setter
    def membership_owning_namespace(self, value: "Namespace"):  # noqa: F821
        """
        Set the membership_owning_namespace property.

        Parameters
        ----------
        value: "Namespace"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "membership_owning_namespace", value)
        self._membership_owning_namespace = value

    @property
    def visibility(self) -> "VisibilityKind":  # noqa: F821
        """
        Get the visibility property.

        Returns
        -------
        "VisibilityKind"
            Value of property visibility.
        """
        return self._visibility

    @visibility.setter
    def visibility(self, value: "VisibilityKind"):  # noqa: F821
        """
        Set the visibility property.

        Parameters
        ----------
        value: "VisibilityKind"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "visibility", value)
        self._visibility = value

    @property
    def distinguishable_from(self) -> bool:  # noqa: F821
        """
        Get the distinguishable from property.

        Returns
        -------
        bool
            Value of property distinguishable from.
        """
        return self._distinguishable_from
