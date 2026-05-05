"""Generated rendering usage class from metamodel."""

from __future__ import annotations

from .part_usage import PartUsage


class RenderingUsage(PartUsage):
    """Java class 'com.ansys.metamodel.sysml2.RenderingUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._rendering_definition = None

    @property
    def rendering_definition(self) -> "RenderingDefinition":  # noqa: F821
        """
        Get the rendering definition property.

        Returns
        -------
        "RenderingDefinition"
            Value of property rendering definition.
        """
        return self._rendering_definition

    @rendering_definition.setter
    def rendering_definition(self, value: "RenderingDefinition"):  # noqa: F821
        """
        Set the rendering_definition property.

        Parameters
        ----------
        value: "RenderingDefinition"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "rendering_definition", value)
        self._rendering_definition = value
