"""Generated requirement constraint membership class from metamodel."""

from __future__ import annotations

from .feature_membership import FeatureMembership


class RequirementConstraintMembership(FeatureMembership):
    """Java class 'com.ansys.metamodel.sysml2.RequirementConstraintMembership'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._kind = None
        self._owned_constraint = None
        self._referenced_constraint = None

    @property
    def kind(self) -> "RequirementConstraintKind":  # noqa: F821
        """
        Get the kind property.

        Returns
        -------
        "RequirementConstraintKind"
            Value of property kind.
        """
        return self._kind

    @kind.setter
    def kind(self, value: "RequirementConstraintKind"):  # noqa: F821
        """
        Set the kind property.

        Parameters
        ----------
        value: "RequirementConstraintKind"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "kind", value)
        self._kind = value

    @property
    def owned_constraint(self) -> "ConstraintUsage":  # noqa: F821
        """
        Get the owned constraint property.

        Returns
        -------
        "ConstraintUsage"
            Value of property owned constraint.
        """
        return self._owned_constraint

    @owned_constraint.setter
    def owned_constraint(self, value: "ConstraintUsage"):  # noqa: F821
        """
        Set the owned_constraint property.

        Parameters
        ----------
        value: "ConstraintUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_constraint", value)
        self._owned_constraint = value

    @property
    def referenced_constraint(self) -> "ConstraintUsage":  # noqa: F821
        """
        Get the referenced constraint property.

        Returns
        -------
        "ConstraintUsage"
            Value of property referenced constraint.
        """
        return self._referenced_constraint

    @referenced_constraint.setter
    def referenced_constraint(self, value: "ConstraintUsage"):  # noqa: F821
        """
        Set the referenced_constraint property.

        Parameters
        ----------
        value: "ConstraintUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "referenced_constraint", value)
        self._referenced_constraint = value
