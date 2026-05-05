"""Generated metadata access expression class from metamodel."""

from __future__ import annotations

from .expression import Expression


class MetadataAccessExpression(Expression):
    """Java class 'com.ansys.metamodel.sysml2.MetadataAccessExpression'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._referenced_element = None

    @property
    def referenced_element(self) -> "Element":  # noqa: F821
        """
        Get the referenced element property.

        Returns
        -------
        "Element"
            Value of property referenced element.
        """
        return self._referenced_element

    @referenced_element.setter
    def referenced_element(self, value: "Element"):  # noqa: F821
        """
        Set the referenced_element property.

        Parameters
        ----------
        value: "Element"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "referenced_element", value)
        self._referenced_element = value
