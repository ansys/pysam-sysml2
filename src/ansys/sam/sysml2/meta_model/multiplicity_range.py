"""Generated multiplicity range class from metamodel."""

from __future__ import annotations

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .multiplicity import Multiplicity


class MultiplicityRange(Multiplicity):
    """Java class 'com.ansys.medini.metamodel.sysml.MultiplicityRange'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._lower_bound = None
        self._upper_bound = None
        self._bound = ObservedList(self, "bound")

    @property
    def lower_bound(self) -> "Expression":  # noqa: F821
        """
        Get the lower bound property.

        Returns
        -------
        "Expression"
            Value of property lower bound.
        """
        return self._lower_bound

    @lower_bound.setter
    def lower_bound(self, value: "Expression"):  # noqa: F821
        """
        Set the lower_bound property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "lower_bound", value)
        self._lower_bound = value

    @property
    def upper_bound(self) -> "Expression":  # noqa: F821
        """
        Get the upper bound property.

        Returns
        -------
        "Expression"
            Value of property upper bound.
        """
        return self._upper_bound

    @upper_bound.setter
    def upper_bound(self, value: "Expression"):  # noqa: F821
        """
        Set the upper_bound property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "upper_bound", value)
        self._upper_bound = value

    @property
    def bound(self) -> List["Expression"]:  # noqa: F821
        """
        Get the bound property.

        Returns
        -------
        List["Expression"]
            Value of property bound.
        """
        return self._bound
