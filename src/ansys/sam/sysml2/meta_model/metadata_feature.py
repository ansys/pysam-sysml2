"""Generated metadata feature class from metamodel."""

from __future__ import annotations

from .annotating_element import AnnotatingElement
from .feature import Feature


class MetadataFeature(Feature, AnnotatingElement):
    """Java class 'com.ansys.medini.metamodel.sysml.MetadataFeature'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._metaclass = None

    @property
    def metaclass(self) -> "Metaclass":  # noqa: F821
        """
        Get the metaclass property.

        Returns
        -------
        "Metaclass"
            Value of property metaclass.
        """
        return self._metaclass

    @metaclass.setter
    def metaclass(self, value: "Metaclass"):  # noqa: F821
        """
        Set the metaclass property.

        Parameters
        ----------
        value: "Metaclass"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "metaclass", value)
        self._metaclass = value
