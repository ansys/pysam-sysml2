"""Generated feature typing class from metamodel."""

from __future__ import annotations

from .specialization import Specialization


class FeatureTyping(Specialization):
    """Java class 'com.ansys.medini.metamodel.sysml.FeatureTyping'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._type_ = None
        self._typed_feature = None
        self._owning_feature = None

    @property
    def type_(self) -> "Type":  # noqa: F821
        """
        Get the ``type_`` property.

        Returns
        -------
        Type
            Value of property ``type_``.
        """
        return self._type_

    @type_.setter
    def type_(self, value: "Type"):  # noqa: F821
        """
        Set the ``type_`` property.

        Parameters
        ----------
        value: Type
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "type_", value)
        self._type_ = value

    @property
    def typed_feature(self) -> "Feature":  # noqa: F821
        """
        Get the typed feature property.

        Returns
        -------
        "Feature"
            Value of property typed feature.
        """
        return self._typed_feature

    @typed_feature.setter
    def typed_feature(self, value: "Feature"):  # noqa: F821
        """
        Set the typed_feature property.

        Parameters
        ----------
        value: "Feature"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "typed_feature", value)
        self._typed_feature = value

    @property
    def owning_feature(self) -> None:  # noqa: F821
        """
        Get the owning feature property.

        Returns
        -------
        None
            Value of property owning feature.
        """
        return self._owning_feature

    @owning_feature.setter
    def owning_feature(self, value: None):  # noqa: F821
        """
        Set the owning_feature property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_feature", value)
        self._owning_feature = value
