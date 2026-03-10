"""Generated view definition class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .part_definition import PartDefinition


class ViewDefinition(PartDefinition):
    """Java class 'com.ansys.medini.metamodel.sysml.ViewDefinition'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._view = ObservedList(self, "view")
        self._view_condition = ObservedList(self, "view_condition")

    @property
    def view(self) -> List["ViewUsage"]:  # noqa: F821
        """
        Get the view property.

        Returns
        -------
        List["ViewUsage"]
            Value of property view.
        """
        return self._view

    @property
    def view_condition(self) -> List["Expression"]:  # noqa: F821
        """
        Get the view condition property.

        Returns
        -------
        List["Expression"]
            Value of property view condition.
        """
        return self._view_condition
