"""Generated viewpoint usage class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .requirement_usage import RequirementUsage


class ViewpointUsage(RequirementUsage):
    """Java class 'com.ansys.metamodel.sysml2.ViewpointUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._viewpoint_definition = None
        self._viewpoint_stakeholder = ObservedList(self, "viewpoint_stakeholder")

    @property
    def viewpoint_definition(self) -> "ViewpointDefinition":  # noqa: F821
        """
        Get the viewpoint definition property.

        Returns
        -------
        "ViewpointDefinition"
            Value of property viewpoint definition.
        """
        return self._viewpoint_definition

    @viewpoint_definition.setter
    def viewpoint_definition(self, value: "ViewpointDefinition"):  # noqa: F821
        """
        Set the viewpoint_definition property.

        Parameters
        ----------
        value: "ViewpointDefinition"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "viewpoint_definition", value)
        self._viewpoint_definition = value

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
