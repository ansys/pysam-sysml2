"""Generated behavior class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .class_ import Class


class Behavior(Class):
    """Java class 'com.ansys.medini.metamodel.sysml.Behavior'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._parameter = ObservedList(self, "parameter")
        self._step = ObservedList(self, "step")
        self._general_parameter = ObservedList(self, "general_parameter")

    @property
    def parameter(self) -> List["Feature"]:  # noqa: F821
        """
        Get the parameter property.

        Returns
        -------
        List["Feature"]
            Value of property parameter.
        """
        return self._parameter

    @property
    def step(self) -> List["Step"]:  # noqa: F821
        """
        Get the step property.

        Returns
        -------
        List["Step"]
            Value of property step.
        """
        return self._step

    @property
    def general_parameter(self) -> List["Feature"]:  # noqa: F821
        """
        Get the general parameter property.

        Returns
        -------
        List["Feature"]
            Value of property general parameter.
        """
        return self._general_parameter
