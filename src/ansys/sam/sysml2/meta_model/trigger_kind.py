"""Generated trigger kind class from metamodel."""

from __future__ import annotations


class TriggerKind:
    """Java class 'com.ansys.medini.metamodel.sysml.TriggerKind'."""

    WHEN: "TriggerKind"
    AT: "TriggerKind"
    AFTER: "TriggerKind"
    WHEN_VALUE: int
    AT_VALUE: int
    AFTER_VALUE: int
    VALUES_ARRAY: "TriggerKind"
    VALUES: list
    value: int
    name: str
    literal: str
    VALUES: "TriggerKind"

    def __init__(self):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        self._name = ""
        self._value = 0
        self._by_name = None
        self._literal = ""

    @property
    def name(self) -> str:  # noqa: F821
        """
        Get the name property.

        Returns
        -------
        str
            Value of property name.
        """
        return self._name

    @property
    def value(self) -> int:
        """
        Get the value property.

        Returns
        -------
        int
            Value of property value.
        """
        return self._value

    @property
    def by_name(self) -> "TriggerKind":  # noqa: F821
        """
        Get the by name property.

        Returns
        -------
        "TriggerKind"
            Value of property by name.
        """
        return self._by_name

    @property
    def literal(self) -> str:  # noqa: F821
        """
        Get the literal property.

        Returns
        -------
        str
            Value of property literal.
        """
        return self._literal
