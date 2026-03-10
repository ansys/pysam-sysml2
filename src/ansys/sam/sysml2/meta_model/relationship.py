"""Generated relationship class from metamodel."""

from __future__ import annotations

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .element import Element


class Relationship(Element):
    """Java class 'com.ansys.medini.metamodel.sysml.Relationship'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._target = ObservedList(self, "target")
        self._source = ObservedList(self, "source")
        self._related_element = ObservedList(self, "related_element")
        self._owned_related_element = ObservedList(self, "owned_related_element")
        self._owning_related_element = None
        self._inheriting_element = None

    @property
    def target(self) -> List["Element"]:  # noqa: F821
        """
        Get the target property.

        Returns
        -------
        List["Element"]
            Value of property target.
        """
        return self._target

    @property
    def source(self) -> List["Element"]:  # noqa: F821
        """
        Get the source property.

        Returns
        -------
        List["Element"]
            Value of property source.
        """
        return self._source

    @property
    def related_element(self) -> List["Element"]:  # noqa: F821
        """
        Get the related element property.

        Returns
        -------
        List["Element"]
            Value of property related element.
        """
        return self._related_element

    @property
    def owned_related_element(self) -> List["Element"]:  # noqa: F821
        """
        Get the owned related element property.

        Returns
        -------
        List["Element"]
            Value of property owned related element.
        """
        return self._owned_related_element

    @property
    def owning_related_element(self) -> None:  # noqa: F821
        """
        Get the owning related element property.

        Returns
        -------
        None
            Value of property owning related element.
        """
        return self._owning_related_element

    @owning_related_element.setter
    def owning_related_element(self, value: None):  # noqa: F821
        """
        Set the owning_related_element property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_related_element", value)
        self._owning_related_element = value

    @property
    def inheriting_element(self) -> "Element":  # noqa: F821
        """
        Get the inheriting element property.

        Returns
        -------
        "Element"
            Value of property inheriting element.
        """
        return self._inheriting_element

    @inheriting_element.setter
    def inheriting_element(self, value: "Element"):  # noqa: F821
        """
        Set the inheriting_element property.

        Parameters
        ----------
        value: "Element"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "inheriting_element", value)
        self._inheriting_element = value
