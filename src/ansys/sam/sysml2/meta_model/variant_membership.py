"""Generated variant membership class from metamodel."""

from __future__ import annotations

from .membership import Membership


class VariantMembership(Membership):
    """Java class 'com.ansys.medini.metamodel.sysml.VariantMembership'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._owned_variant_usage = None

    @property
    def owned_variant_usage(self) -> None:  # noqa: F821
        """
        Get the owned variant usage property.

        Returns
        -------
        None
            Value of property owned variant usage.
        """
        return self._owned_variant_usage

    @owned_variant_usage.setter
    def owned_variant_usage(self, value: None):  # noqa: F821
        """
        Set the owned_variant_usage property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_variant_usage", value)
        self._owned_variant_usage = value
