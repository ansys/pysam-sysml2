"""Generated annotating element class from metamodel."""

from typing import List

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .element import Element


class AnnotatingElement(Element):
    """Java class 'com.ansys.medini.metamodel.sysml.AnnotatingElement'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._annotation = ObservedList(self, "annotation")
        self._annotated_element = ObservedList(self, "annotated_element")

    @property
    def annotation(self) -> List["Annotation"]:  # noqa: F821
        """
        Get the annotation property.

        Returns
        -------
        List["Annotation"]
            Value of property annotation.
        """
        return self._annotation

    @property
    def annotated_element(self) -> List["Element"]:  # noqa: F821
        """
        Get the annotated element property.

        Returns
        -------
        List["Element"]
            Value of property annotated element.
        """
        return self._annotated_element
