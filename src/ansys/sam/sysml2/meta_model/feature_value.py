"""Generated feature value class from metamodel."""

from __future__ import annotations

from .owning_membership import OwningMembership


class FeatureValue(OwningMembership):
    """Java class 'com.ansys.metamodel.sysml2.FeatureValue'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._feature_with_value = None
        self._value = None
        self._is_default = False
        self._is_initial = False

    @property
    def feature_with_value(self) -> "Feature":  # noqa: F821
        """
        Get the feature with value property.

        Returns
        -------
        "Feature"
            Value of property feature with value.
        """
        return self._feature_with_value

    @feature_with_value.setter
    def feature_with_value(self, value: "Feature"):  # noqa: F821
        """
        Set the feature_with_value property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "feature_with_value", value)
        self._feature_with_value = value

    @property
    def value(self) -> "Expression":  # noqa: F821
        """
        Get the value property.

        Returns
        -------
        "Expression"
            Value of property value.
        """
        return self._value

    @value.setter
    def value(self, value: "Expression"):  # noqa: F821
        """
        Set the value property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "value", value)
        self._value = value

    @property
    def is_default(self) -> bool:  # noqa: F821
        """
        Get the is default property.

        Returns
        -------
        bool
            Value of property is default.
        """
        return self._is_default

    @is_default.setter
    def is_default(self, value: bool):  # noqa: F821
        """
        Set the is_default property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_default", value)
        self._is_default = value

    @property
    def is_initial(self) -> bool:  # noqa: F821
        """
        Get the is initial property.

        Returns
        -------
        bool
            Value of property is initial.
        """
        return self._is_initial

    @is_initial.setter
    def is_initial(self, value: bool):  # noqa: F821
        """
        Set the is_initial property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_initial", value)
        self._is_initial = value
