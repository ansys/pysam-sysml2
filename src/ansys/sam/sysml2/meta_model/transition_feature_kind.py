"""Generated transition feature kind class from metamodel."""

from __future__ import annotations


class TransitionFeatureKind:
    """Java class 'com.ansys.medini.metamodel.sysml.TransitionFeatureKind'."""

    TRIGGER: "TransitionFeatureKind"
    GUARD: "TransitionFeatureKind"
    EFFECT: "TransitionFeatureKind"
    UNDEFINED: "TransitionFeatureKind"
    TRIGGER_VALUE: int
    GUARD_VALUE: int
    EFFECT_VALUE: int
    UNDEFINED_VALUE: int
    VALUES_ARRAY: "TransitionFeatureKind"
    VALUES: list
    value: int
    name: str
    literal: str
    VALUES: "TransitionFeatureKind"

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
    def by_name(self) -> "TransitionFeatureKind":  # noqa: F821
        """
        Get the by name property.

        Returns
        -------
        "TransitionFeatureKind"
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
