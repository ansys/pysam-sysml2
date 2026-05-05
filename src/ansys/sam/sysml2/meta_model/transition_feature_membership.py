"""Generated transition feature membership class from metamodel."""

from __future__ import annotations

from .feature_membership import FeatureMembership


class TransitionFeatureMembership(FeatureMembership):
    """Java class 'com.ansys.metamodel.sysml2.TransitionFeatureMembership'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._kind = None
        self._transition_feature = None

    @property
    def kind(self) -> "TransitionFeatureKind":  # noqa: F821
        """
        Get the kind property.

        Returns
        -------
        "TransitionFeatureKind"
            Value of property kind.
        """
        return self._kind

    @kind.setter
    def kind(self, value: "TransitionFeatureKind"):  # noqa: F821
        """
        Set the kind property.

        Parameters
        ----------
        value: "TransitionFeatureKind"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "kind", value)
        self._kind = value

    @property
    def transition_feature(self) -> "Step":  # noqa: F821
        """
        Get the transition feature property.

        Returns
        -------
        "Step"
            Value of property transition feature.
        """
        return self._transition_feature

    @transition_feature.setter
    def transition_feature(self, value: "Step"):  # noqa: F821
        """
        Set the transition_feature property.

        Parameters
        ----------
        value: "Step"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "transition_feature", value)
        self._transition_feature = value
