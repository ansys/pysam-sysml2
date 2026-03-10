"""Generated visibility kind class from metamodel."""

from __future__ import annotations


class VisibilityKind:
    """Java class 'com.ansys.medini.metamodel.sysml.VisibilityKind'."""

    PUBLIC: "VisibilityKind"
    PRIVATE: "VisibilityKind"
    PROTECTED: "VisibilityKind"
    PACKAGE: "VisibilityKind"
    PUBLIC_VALUE: int
    PRIVATE_VALUE: int
    PROTECTED_VALUE: int
    PACKAGE_VALUE: int
    VALUES_ARRAY: "VisibilityKind"
    VALUES: list
    value: int
    name: str
    literal: str
    VALUES: "VisibilityKind"

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
    def by_name(self) -> "VisibilityKind":  # noqa: F821
        """
        Get the by name property.

        Returns
        -------
        "VisibilityKind"
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
