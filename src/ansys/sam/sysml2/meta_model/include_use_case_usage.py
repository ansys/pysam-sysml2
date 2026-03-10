"""Generated include use case usage class from metamodel."""

from __future__ import annotations

from .perform_action_usage import PerformActionUsage
from .use_case_usage import UseCaseUsage


class IncludeUseCaseUsage(UseCaseUsage, PerformActionUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.IncludeUseCaseUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._use_case_included = None

    @property
    def use_case_included(self) -> "UseCaseUsage":  # noqa: F821
        """
        Get the use case included property.

        Returns
        -------
        "UseCaseUsage"
            Value of property use case included.
        """
        return self._use_case_included

    @use_case_included.setter
    def use_case_included(self, value: "UseCaseUsage"):  # noqa: F821
        """
        Set the use_case_included property.

        Parameters
        ----------
        value: "UseCaseUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "use_case_included", value)
        self._use_case_included = value
