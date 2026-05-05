"""Generated differencing class from metamodel."""

from __future__ import annotations

from .relationship import Relationship


class Differencing(Relationship):
    """Java class 'com.ansys.metamodel.sysml2.Differencing'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._differencing_type = None
        self._type_differenced = None

    @property
    def differencing_type(self) -> "Type":  # noqa: F821
        """
        Get the differencing type property.

        Returns
        -------
        "Type"
            Value of property differencing type.
        """
        return self._differencing_type

    @differencing_type.setter
    def differencing_type(self, value: "Type"):  # noqa: F821
        """
        Set the differencing_type property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "differencing_type", value)
        self._differencing_type = value

    @property
    def type_differenced(self) -> "Type":  # noqa: F821
        """
        Get the type differenced property.

        Returns
        -------
        "Type"
            Value of property type differenced.
        """
        return self._type_differenced

    @type_differenced.setter
    def type_differenced(self, value: "Type"):  # noqa: F821
        """
        Set the type_differenced property.

        Parameters
        ----------
        value: "Type"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "type_differenced", value)
        self._type_differenced = value
