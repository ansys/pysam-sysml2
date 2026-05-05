"""Generated viewpoint definition class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .requirement_definition import RequirementDefinition


class ViewpointDefinition(RequirementDefinition):
    """Java class 'com.ansys.metamodel.sysml2.ViewpointDefinition'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._viewpoint_stakeholder = ObservedList(self, "viewpoint_stakeholder")

    @property
    def viewpoint_stakeholder(self) -> list["PartUsage"]:  # noqa: F821
        """
        Get the viewpoint stakeholder property.

        Returns
        -------
        list["PartUsage"]
            Value of property viewpoint stakeholder.
        """
        return self._viewpoint_stakeholder
