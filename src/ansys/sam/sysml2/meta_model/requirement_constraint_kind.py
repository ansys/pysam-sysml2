"""Generated requirement constraint kind class from metamodel."""

from __future__ import annotations


class RequirementConstraintKind:
    """Java class 'com.ansys.medini.metamodel.sysml.RequirementConstraintKind'."""

    NOT_AREQUIREMENT_CONSTRAINT: "RequirementConstraintKind"
    ASSUMPTION: "RequirementConstraintKind"
    REQUIREMENT: "RequirementConstraintKind"
    NOT_AREQUIREMENT_CONSTRAINT_VALUE: int
    ASSUMPTION_VALUE: int
    REQUIREMENT_VALUE: int
    VALUES_ARRAY: "RequirementConstraintKind"
    VALUES: list
    value: int
    name: str
    literal: str
    VALUES: "RequirementConstraintKind"

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
