"""Generated view rendering membership class from metamodel."""

from __future__ import annotations

from .feature_membership import FeatureMembership


class ViewRenderingMembership(FeatureMembership):
    """Java class 'com.ansys.metamodel.sysml2.ViewRenderingMembership'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._owned_rendering = None
        self._referenced_rendering = None

    @property
    def owned_rendering(self) -> "RenderingUsage":  # noqa: F821
        """
        Get the owned rendering property.

        Returns
        -------
        "RenderingUsage"
            Value of property owned rendering.
        """
        return self._owned_rendering

    @owned_rendering.setter
    def owned_rendering(self, value: "RenderingUsage"):  # noqa: F821
        """
        Set the owned_rendering property.

        Parameters
        ----------
        value: "RenderingUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_rendering", value)
        self._owned_rendering = value

    @property
    def referenced_rendering(self) -> "RenderingUsage":  # noqa: F821
        """
        Get the referenced rendering property.

        Returns
        -------
        "RenderingUsage"
            Value of property referenced rendering.
        """
        return self._referenced_rendering

    @referenced_rendering.setter
    def referenced_rendering(self, value: "RenderingUsage"):  # noqa: F821
        """
        Set the referenced_rendering property.

        Parameters
        ----------
        value: "RenderingUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "referenced_rendering", value)
        self._referenced_rendering = value
