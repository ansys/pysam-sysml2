"""Generated trigger invocation expression class from metamodel."""

from __future__ import annotations

from .invocation_expression import InvocationExpression


class TriggerInvocationExpression(InvocationExpression):
    """Java class 'com.ansys.metamodel.sysml2.TriggerInvocationExpression'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._kind = None

    @property
    def kind(self) -> "TriggerKind":  # noqa: F821
        """
        Get the kind property.

        Returns
        -------
        "TriggerKind"
            Value of property kind.
        """
        return self._kind

    @kind.setter
    def kind(self, value: "TriggerKind"):  # noqa: F821
        """
        Set the kind property.

        Parameters
        ----------
        value: "TriggerKind"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "kind", value)
        self._kind = value
