"""Generated framed concern membership class from metamodel."""

from __future__ import annotations

from .requirement_constraint_membership import RequirementConstraintMembership


class FramedConcernMembership(RequirementConstraintMembership):
    """Java class 'com.ansys.metamodel.sysml2.FramedConcernMembership'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._owned_concern = None
        self._referenced_concern = None

    @property
    def owned_concern(self) -> "ConcernUsage":  # noqa: F821
        """
        Get the owned concern property.

        Returns
        -------
        "ConcernUsage"
            Value of property owned concern.
        """
        return self._owned_concern

    @owned_concern.setter
    def owned_concern(self, value: "ConcernUsage"):  # noqa: F821
        """
        Set the owned_concern property.

        Parameters
        ----------
        value: "ConcernUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_concern", value)
        self._owned_concern = value

    @property
    def referenced_concern(self) -> "ConcernUsage":  # noqa: F821
        """
        Get the referenced concern property.

        Returns
        -------
        "ConcernUsage"
            Value of property referenced concern.
        """
        return self._referenced_concern

    @referenced_concern.setter
    def referenced_concern(self, value: "ConcernUsage"):  # noqa: F821
        """
        Set the referenced_concern property.

        Parameters
        ----------
        value: "ConcernUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "referenced_concern", value)
        self._referenced_concern = value
