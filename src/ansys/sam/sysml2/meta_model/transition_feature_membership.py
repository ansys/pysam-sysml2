"""Generated transition feature membership class from metamodel."""

from __future__ import annotations

from .feature_membership import FeatureMembership


class TransitionFeatureMembership(FeatureMembership):
    """Java class 'com.ansys.medini.metamodel.sysml.TransitionFeatureMembership'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._transition_feature = None
        self._kind = None

    @property
    def transition_feature(self) -> None:  # noqa: F821
        """
        Get the transition feature property.

        Returns
        -------
        None
            Value of property transition feature.
        """
        return self._transition_feature

    @transition_feature.setter
    def transition_feature(self, value: None):  # noqa: F821
        """
        Set the transition_feature property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "transition_feature", value)
        self._transition_feature = value

    @property
    def kind(self) -> None:  # noqa: F821
        """
        Get the kind property.

        Returns
        -------
        None
            Value of property kind.
        """
        return self._kind

    @kind.setter
    def kind(self, value: None):  # noqa: F821
        """
        Set the kind property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "kind", value)
        self._kind = value
