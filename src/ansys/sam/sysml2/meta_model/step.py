"""Generated step class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .feature import Feature


class Step(Feature):
    """Java class 'com.ansys.metamodel.sysml2.Step'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._behavior = ObservedList(self, "behavior")
        self._parameter = ObservedList(self, "parameter")

    @property
    def behavior(self) -> list["Behavior"]:  # noqa: F821
        """
        Get the behavior property.

        Returns
        -------
        list["Behavior"]
            Value of property behavior.
        """
        return self._behavior

    @property
    def parameter(self) -> list["Feature"]:  # noqa: F821
        """
        Get the parameter property.

        Returns
        -------
        list["Feature"]
            Value of property parameter.
        """
        return self._parameter
