"""Generated rendering definition class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .part_definition import PartDefinition


class RenderingDefinition(PartDefinition):
    """Java class 'com.ansys.metamodel.sysml2.RenderingDefinition'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._rendering = ObservedList(self, "rendering")

    @property
    def rendering(self) -> list["RenderingUsage"]:  # noqa: F821
        """
        Get the rendering property.

        Returns
        -------
        list["RenderingUsage"]
            Value of property rendering.
        """
        return self._rendering
