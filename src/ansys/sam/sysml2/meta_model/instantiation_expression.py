"""Generated instantiation expression class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .expression import Expression


class InstantiationExpression(Expression):
    """Java class 'com.ansys.metamodel.sysml2.InstantiationExpression'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._argument = ObservedList(self, "argument")
        self._instantiated_type = None

    @property
    def argument(self) -> list["Expression"]:  # noqa: F821
        """
        Get the argument property.

        Returns
        -------
        list["Expression"]
            Value of property argument.
        """
        return self._argument

    @property
    def instantiated_type(self) -> "Type":  # noqa: F821
        """
        Get the instantiated type property.

        Returns
        -------
        "Type"
            Value of property instantiated type.
        """
        return self._instantiated_type

    @instantiated_type.setter
    def instantiated_type(self, value: "Type"):  # noqa: F821
        """
        Set the instantiated_type property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "instantiated_type", value)
        self._instantiated_type = value
