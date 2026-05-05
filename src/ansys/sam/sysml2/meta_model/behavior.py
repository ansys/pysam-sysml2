"""Generated behavior class from metamodel."""

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .class_ import Class


class Behavior(Class):
    """Java class 'com.ansys.metamodel.sysml2.Behavior'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._parameter = ObservedList(self, "parameter")
        self._step = ObservedList(self, "step")

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

    @property
    def step(self) -> list["Step"]:  # noqa: F821
        """
        Get the step property.

        Returns
        -------
        list["Step"]
            Value of property step.
        """
        return self._step
