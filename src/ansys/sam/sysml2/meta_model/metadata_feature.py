"""Generated metadata feature class from metamodel."""

from __future__ import annotations

from .annotating_element import AnnotatingElement
from .feature import Feature


class MetadataFeature(AnnotatingElement, Feature):
    """Java class 'com.ansys.metamodel.sysml2.MetadataFeature'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._metaclass = None
        self._semantic = False
        self._syntactic = False

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

    @property
    def semantic(self) -> bool:  # noqa: F821
        """
        Get the semantic property.

        Returns
        -------
        bool
            Value of property semantic.
        """
        return self._semantic

    @property
    def syntactic(self) -> bool:  # noqa: F821
        """
        Get the syntactic property.

        Returns
        -------
        bool
            Value of property syntactic.
        """
        return self._syntactic
