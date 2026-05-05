"""Generated element class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .e_object import EObject


class Element(EObject):
    """Java class 'com.ansys.metamodel.sysml2.Element'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._alias_ids = ObservedList(self, "alias_ids")
        self._declared_name = ""
        self._declared_short_name = ""
        self._documentation = ObservedList(self, "documentation")
        self._element_id = ""
        self._name = ""
        self._owned_annotation = ObservedList(self, "owned_annotation")
        self._owned_element = ObservedList(self, "owned_element")
        self._owned_relationship = ObservedList(self, "owned_relationship")
        self._owner = None
        self._owning_membership = None
        self._owning_namespace = None
        self._owning_relationship = None
        self._qualified_name = ""
        self._short_name = ""
        self._textual_representation = ObservedList(self, "textual_representation")
        self._is_implied_included = False
        self._is_library_element = False

    @property
    def alias_ids(self) -> list[str]:  # noqa: F821
        """
        Get the alias ids property.

        Returns
        -------
        list[str]
            Value of property alias ids.
        """
        return self._alias_ids

    @property
    def declared_name(self) -> str:  # noqa: F821
        """
        Get the declared name property.

        Returns
        -------
        str
            Value of property declared name.
        """
        return self._declared_name

    @declared_name.setter
    def declared_name(self, value: str):  # noqa: F821
        """
        Set the declared_name property.

        Parameters
        ----------
        value: str
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "declared_name", value)
        self._declared_name = value

    @property
    def declared_short_name(self) -> str:  # noqa: F821
        """
        Get the declared short name property.

        Returns
        -------
        str
            Value of property declared short name.
        """
        return self._declared_short_name

    @declared_short_name.setter
    def declared_short_name(self, value: str):  # noqa: F821
        """
        Set the declared_short_name property.

        Parameters
        ----------
        value: str
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "declared_short_name", value)
        self._declared_short_name = value

    @property
    def documentation(self) -> list["Documentation"]:  # noqa: F821
        """
        Get the documentation property.

        Returns
        -------
        list["Documentation"]
            Value of property documentation.
        """
        return self._documentation

    @property
    def element_id(self) -> str:  # noqa: F821
        """
        Get the element id property.

        Returns
        -------
        str
            Value of property element id.
        """
        return self._element_id

    @element_id.setter
    def element_id(self, value: str):  # noqa: F821
        """
        Set the element_id property.

        Parameters
        ----------
        value: str
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "element_id", value)
        self._element_id = value

    @property
    def name(self) -> str:  # noqa: F821
        """
        Get the name property.

        Returns
        -------
        str
            Value of property name.
        """
        return self._name

    @property
    def owned_annotation(self) -> list["Annotation"]:  # noqa: F821
        """
        Get the owned annotation property.

        Returns
        -------
        list["Annotation"]
            Value of property owned annotation.
        """
        return self._owned_annotation

    @property
    def owned_element(self) -> list["Element"]:  # noqa: F821
        """
        Get the owned element property.

        Returns
        -------
        list["Element"]
            Value of property owned element.
        """
        return self._owned_element

    @property
    def owned_relationship(self) -> list["Relationship"]:  # noqa: F821
        """
        Get the owned relationship property.

        Returns
        -------
        list["Relationship"]
            Value of property owned relationship.
        """
        return self._owned_relationship

    @property
    def owner(self) -> "Element":  # noqa: F821
        """
        Get the owner property.

        Returns
        -------
        "Element"
            Value of property owner.
        """
        return self._owner

    @owner.setter
    def owner(self, value: "Element"):  # noqa: F821
        """
        Set the owner property.

        Parameters
        ----------
        value: "Element"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owner", value)
        self._owner = value

    @property
    def owning_membership(self) -> "OwningMembership":  # noqa: F821
        """
        Get the owning membership property.

        Returns
        -------
        "OwningMembership"
            Value of property owning membership.
        """
        return self._owning_membership

    @owning_membership.setter
    def owning_membership(self, value: "OwningMembership"):  # noqa: F821
        """
        Set the owning_membership property.

        Parameters
        ----------
        value: "OwningMembership"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_membership", value)
        self._owning_membership = value

    @property
    def owning_namespace(self) -> "Namespace":  # noqa: F821
        """
        Get the owning namespace property.

        Returns
        -------
        "Namespace"
            Value of property owning namespace.
        """
        return self._owning_namespace

    @owning_namespace.setter
    def owning_namespace(self, value: "Namespace"):  # noqa: F821
        """
        Set the owning_namespace property.

        Parameters
        ----------
        value: "Namespace"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_namespace", value)
        self._owning_namespace = value

    @property
    def owning_relationship(self) -> "Relationship":  # noqa: F821
        """
        Get the owning relationship property.

        Returns
        -------
        "Relationship"
            Value of property owning relationship.
        """
        return self._owning_relationship

    @owning_relationship.setter
    def owning_relationship(self, value: "Relationship"):  # noqa: F821
        """
        Set the owning_relationship property.

        Parameters
        ----------
        value: "Relationship"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_relationship", value)
        self._owning_relationship = value

    @property
    def qualified_name(self) -> str:  # noqa: F821
        """
        Get the qualified name property.

        Returns
        -------
        str
            Value of property qualified name.
        """
        return self._qualified_name

    @property
    def short_name(self) -> str:  # noqa: F821
        """
        Get the short name property.

        Returns
        -------
        str
            Value of property short name.
        """
        return self._short_name

    @property
    def textual_representation(self) -> list["TextualRepresentation"]:  # noqa: F821
        """
        Get the textual representation property.

        Returns
        -------
        list["TextualRepresentation"]
            Value of property textual representation.
        """
        return self._textual_representation

    @property
    def is_implied_included(self) -> bool:  # noqa: F821
        """
        Get the is implied included property.

        Returns
        -------
        bool
            Value of property is implied included.
        """
        return self._is_implied_included

    @is_implied_included.setter
    def is_implied_included(self, value: bool):  # noqa: F821
        """
        Set the is_implied_included property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_implied_included", value)
        self._is_implied_included = value

    @property
    def is_library_element(self) -> bool:  # noqa: F821
        """
        Get the is library element property.

        Returns
        -------
        bool
            Value of property is library element.
        """
        return self._is_library_element

    @is_library_element.setter
    def is_library_element(self, value: bool):  # noqa: F821
        """
        Set the is_library_element property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_library_element", value)
        self._is_library_element = value
