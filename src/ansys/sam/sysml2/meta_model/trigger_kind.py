"""Generated trigger kind class from metamodel."""

from __future__ import annotations


class TriggerKind:
    """Java class 'com.ansys.metamodel.sysml2.TriggerKind'."""

    AFTER: "TriggerKind"
    AFTER_VALUE: int
    AT: "TriggerKind"
    AT_VALUE: int
    VALUES: list
    VALUES_ARRAY: "TriggerKind"
    WHEN: "TriggerKind"
    WHEN_VALUE: int
    literal: str
    name: str
    value: int

    def __init__(self):
        """Construct new instance."""
        self._by_name = None
        self._literal = ""
        self._name = ""
        self._value = 0

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
