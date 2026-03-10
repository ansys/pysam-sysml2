"""Generated part usage class from metamodel."""

from __future__ import annotations

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .item_usage import ItemUsage


class PartUsage(ItemUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.PartUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._all_part_definition = ObservedList(self, "all_part_definition")
        self._part_definition = ObservedList(self, "part_definition")
        self._is_actor = False
        self._is_stakeholder = False

    @property
    def all_part_definition(self) -> List["PartDefinition"]:  # noqa: F821
        """
        Get the all part definition property.

        Returns
        -------
        List["PartDefinition"]
            Value of property all part definition.
        """
        return self._all_part_definition

    @property
    def part_definition(self) -> List["PartDefinition"]:  # noqa: F821
        """
        Get the part definition property.

        Returns
        -------
        List["PartDefinition"]
            Value of property part definition.
        """
        return self._part_definition

    @property
    def is_actor(self) -> bool:  # noqa: F821
        """
        Get the is actor property.

        Returns
        -------
        bool
            Value of property is actor.
        """
        return self._is_actor

    @is_actor.setter
    def is_actor(self, value: bool):  # noqa: F821
        """
        Set the is_actor property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_actor", value)
        self._is_actor = value

    @property
    def is_stakeholder(self) -> bool:  # noqa: F821
        """
        Get the is stakeholder property.

        Returns
        -------
        bool
            Value of property is stakeholder.
        """
        return self._is_stakeholder

    @is_stakeholder.setter
    def is_stakeholder(self, value: bool):  # noqa: F821
        """
        Set the is_stakeholder property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_stakeholder", value)
        self._is_stakeholder = value
