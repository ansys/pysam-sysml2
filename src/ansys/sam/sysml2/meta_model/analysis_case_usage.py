"""Generated analysis case usage class from metamodel."""

from __future__ import annotations

from .case_usage import CaseUsage


class AnalysisCaseUsage(CaseUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.AnalysisCaseUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._analysis_case_definition = None
        self._result_expression = None

    @property
    def analysis_case_definition(self) -> "AnalysisCaseDefinition":  # noqa: F821
        """
        Get the analysis case definition property.

        Returns
        -------
        "AnalysisCaseDefinition"
            Value of property analysis case definition.
        """
        return self._analysis_case_definition

    @analysis_case_definition.setter
    def analysis_case_definition(self, value: "AnalysisCaseDefinition"):  # noqa: F821
        """
        Set the analysis_case_definition property.

        Parameters
        ----------
        value: "AnalysisCaseDefinition"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "analysis_case_definition", value)
        self._analysis_case_definition = value

    @property
    def result_expression(self) -> "Expression":  # noqa: F821
        """
        Get the result expression property.

        Returns
        -------
        "Expression"
            Value of property result expression.
        """
        return self._result_expression

    @result_expression.setter
    def result_expression(self, value: "Expression"):  # noqa: F821
        """
        Set the result_expression property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "result_expression", value)
        self._result_expression = value
