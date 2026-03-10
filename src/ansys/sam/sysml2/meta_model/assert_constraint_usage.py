"""Generated assert constraint usage class from metamodel."""

from __future__ import annotations

from .constraint_usage import ConstraintUsage
from .invariant import Invariant


class AssertConstraintUsage(ConstraintUsage, Invariant):
    """Java class 'com.ansys.medini.metamodel.sysml.AssertConstraintUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._asserted_constraint = None

    @property
    def asserted_constraint(self) -> "ConstraintUsage":  # noqa: F821
        """
        Get the asserted constraint property.

        Returns
        -------
        "ConstraintUsage"
            Value of property asserted constraint.
        """
        return self._asserted_constraint

    @asserted_constraint.setter
    def asserted_constraint(self, value: "ConstraintUsage"):  # noqa: F821
        """
        Set the asserted_constraint property.

        Parameters
        ----------
        value: "ConstraintUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "asserted_constraint", value)
        self._asserted_constraint = value
