"""Generated multiplicity range class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .multiplicity import Multiplicity


class MultiplicityRange(Multiplicity):
    """Java class 'com.ansys.metamodel.sysml2.MultiplicityRange'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._bound = ObservedList(self, "bound")
        self._lower_bound = None
        self._upper_bound = None

    @property
    def bound(self) -> list["Expression"]:  # noqa: F821
        """
        Get the bound property.

        Returns
        -------
        list["Expression"]
            Value of property bound.
        """
        return self._bound

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
