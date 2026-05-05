"""Generated relationship class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .element import Element


class Relationship(Element):
    """Java class 'com.ansys.metamodel.sysml2.Relationship'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._owned_related_element = ObservedList(self, "owned_related_element")
        self._owning_related_element = None
        self._related_element = ObservedList(self, "related_element")
        self._relationship_owner = None
        self._source = ObservedList(self, "source")
        self._target = ObservedList(self, "target")
        self._is_implied = False

    @property
    def owned_related_element(self) -> list["Element"]:  # noqa: F821
        """
        Get the owned related element property.

        Returns
        -------
        list["Element"]
            Value of property owned related element.
        """
        return self._owned_related_element

    @property
    def owning_related_element(self) -> "Element":  # noqa: F821
        """
        Get the owning related element property.

        Returns
        -------
        "Element"
            Value of property owning related element.
        """
        return self._owning_related_element

    @owning_related_element.setter
    def owning_related_element(self, value: "Element"):  # noqa: F821
        """
        Set the owning_related_element property.

        Parameters
        ----------
        value: "Element"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_related_element", value)
        self._owning_related_element = value

    @property
    def related_element(self) -> list["Element"]:  # noqa: F821
        """
        Get the related element property.

        Returns
        -------
        list["Element"]
            Value of property related element.
        """
        return self._related_element

    @property
    def relationship_owner(self) -> "Element":  # noqa: F821
        """
        Get the relationship owner property.

        Returns
        -------
        "Element"
            Value of property relationship owner.
        """
        return self._relationship_owner

    @relationship_owner.setter
    def relationship_owner(self, value: "Element"):  # noqa: F821
        """
        Set the relationship_owner property.

        Parameters
        ----------
        value: "Element"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "relationship_owner", value)
        self._relationship_owner = value

    @property
    def source(self) -> list["Element"]:  # noqa: F821
        """
        Get the source property.

        Returns
        -------
        list["Element"]
            Value of property source.
        """
        return self._source

    @property
    def target(self) -> list["Element"]:  # noqa: F821
        """
        Get the target property.

        Returns
        -------
        list["Element"]
            Value of property target.
        """
        return self._target

    @property
    def is_implied(self) -> bool:  # noqa: F821
        """
        Get the is implied property.

        Returns
        -------
        bool
            Value of property is implied.
        """
        return self._is_implied

    @is_implied.setter
    def is_implied(self, value: bool):  # noqa: F821
        """
        Set the is_implied property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_implied", value)
        self._is_implied = value
