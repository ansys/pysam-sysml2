"""Generated analysis case definition class from metamodel."""

from __future__ import annotations

from .case_definition import CaseDefinition


class AnalysisCaseDefinition(CaseDefinition):
    """Java class 'com.ansys.metamodel.sysml2.AnalysisCaseDefinition'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._result_expression = None

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
