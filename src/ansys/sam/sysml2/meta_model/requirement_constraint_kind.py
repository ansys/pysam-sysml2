"""Generated requirement constraint kind class from metamodel."""

from __future__ import annotations


class RequirementConstraintKind:
    """Java class 'com.ansys.metamodel.sysml2.RequirementConstraintKind'."""

    ASSUMPTION: "RequirementConstraintKind"
    ASSUMPTION_VALUE: int
    REQUIREMENT: "RequirementConstraintKind"
    REQUIREMENT_VALUE: int
    VALUES: list
    VALUES_ARRAY: "RequirementConstraintKind"
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
    def by_name(self) -> "RequirementConstraintKind":  # noqa: F821
        """
        Get the by name property.

        Returns
        -------
        "RequirementConstraintKind"
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
