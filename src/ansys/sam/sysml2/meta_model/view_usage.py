"""Generated view usage class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .part_usage import PartUsage


class ViewUsage(PartUsage):
    """Java class 'com.ansys.metamodel.sysml2.ViewUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._exposed_element = ObservedList(self, "exposed_element")
        self._satisfied_viewpoint = ObservedList(self, "satisfied_viewpoint")
        self._view_condition = ObservedList(self, "view_condition")
        self._view_definition = None
        self._view_rendering = None

    @property
    def exposed_element(self) -> list["Element"]:  # noqa: F821
        """
        Get the exposed element property.

        Returns
        -------
        list["Element"]
            Value of property exposed element.
        """
        return self._exposed_element

    @property
    def satisfied_viewpoint(self) -> list["ViewpointUsage"]:  # noqa: F821
        """
        Get the satisfied viewpoint property.

        Returns
        -------
        list["ViewpointUsage"]
            Value of property satisfied viewpoint.
        """
        return self._satisfied_viewpoint

    @property
    def view_condition(self) -> list["Expression"]:  # noqa: F821
        """
        Get the view condition property.

        Returns
        -------
        list["Expression"]
            Value of property view condition.
        """
        return self._view_condition

    @property
    def view_definition(self) -> "ViewDefinition":  # noqa: F821
        """
        Get the view definition property.

        Returns
        -------
        "ViewDefinition"
            Value of property view definition.
        """
        return self._view_definition

    @view_definition.setter
    def view_definition(self, value: "ViewDefinition"):  # noqa: F821
        """
        Set the view_definition property.

        Parameters
        ----------
        value: "ViewDefinition"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "view_definition", value)
        self._view_definition = value

    @property
    def view_rendering(self) -> "RenderingUsage":  # noqa: F821
        """
        Get the view rendering property.

        Returns
        -------
        "RenderingUsage"
            Value of property view rendering.
        """
        return self._view_rendering

    @view_rendering.setter
    def view_rendering(self, value: "RenderingUsage"):  # noqa: F821
        """
        Set the view_rendering property.

        Parameters
        ----------
        value: "RenderingUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "view_rendering", value)
        self._view_rendering = value
