"""Generated satisfy requirement usage class from metamodel."""

from __future__ import annotations

from .assert_constraint_usage import AssertConstraintUsage
from .requirement_usage import RequirementUsage


class SatisfyRequirementUsage(RequirementUsage, AssertConstraintUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.SatisfyRequirementUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._satisfied_requirement = None
        self._satisfying_feature = None

    @property
    def satisfied_requirement(self) -> "RequirementUsage":  # noqa: F821
        """
        Get the satisfied requirement property.

        Returns
        -------
        "RequirementUsage"
            Value of property satisfied requirement.
        """
        return self._satisfied_requirement

    @satisfied_requirement.setter
    def satisfied_requirement(self, value: "RequirementUsage"):  # noqa: F821
        """
        Set the satisfied_requirement property.

        Parameters
        ----------
        value: "RequirementUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "satisfied_requirement", value)
        self._satisfied_requirement = value

    @property
    def satisfying_feature(self) -> "Feature":  # noqa: F821
        """
        Get the satisfying feature property.

        Returns
        -------
        "Feature"
            Value of property satisfying feature.
        """
        return self._satisfying_feature

    @satisfying_feature.setter
    def satisfying_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the satisfying_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "satisfying_feature", value)
        self._satisfying_feature = value
