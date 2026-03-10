"""Generated requirement constraint membership class from metamodel."""

from __future__ import annotations

from .feature_membership import FeatureMembership


class RequirementConstraintMembership(FeatureMembership):
    """Java class 'com.ansys.medini.metamodel.sysml.RequirementConstraintMembership'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._kind = None
        self._constraint = None

    @property
    def kind(self) -> None:  # noqa: F821
        """
        Get the kind property.

        Returns
        -------
        None
            Value of property kind.
        """
        return self._kind

    @kind.setter
    def kind(self, value: None):  # noqa: F821
        """
        Set the kind property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "kind", value)
        self._kind = value

    @property
    def constraint(self) -> None:  # noqa: F821
        """
        Get the constraint property.

        Returns
        -------
        None
            Value of property constraint.
        """
        return self._constraint

    @constraint.setter
    def constraint(self, value: None):  # noqa: F821
        """
        Set the constraint property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "constraint", value)
        self._constraint = value
