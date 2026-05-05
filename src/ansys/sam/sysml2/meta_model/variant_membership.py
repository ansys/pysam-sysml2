"""Generated variant membership class from metamodel."""

from __future__ import annotations

from .owning_membership import OwningMembership


class VariantMembership(OwningMembership):
    """Java class 'com.ansys.metamodel.sysml2.VariantMembership'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._owned_variant_usage = None

    @property
    def owned_variant_usage(self) -> "Usage":  # noqa: F821
        """
        Get the owned variant usage property.

        Returns
        -------
        "Usage"
            Value of property owned variant usage.
        """
        return self._owned_variant_usage

    @owned_variant_usage.setter
    def owned_variant_usage(self, value: "Usage"):  # noqa: F821
        """
        Set the owned_variant_usage property.

        Parameters
        ----------
        value: "Usage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_variant_usage", value)
        self._owned_variant_usage = value
