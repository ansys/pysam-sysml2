"""Generated documentation class from metamodel."""

from __future__ import annotations

from .comment import Comment


class Documentation(Comment):
    """Java class 'com.ansys.metamodel.sysml2.Documentation'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._documented_element = None

    @property
    def documented_element(self) -> "Element":  # noqa: F821
        """
        Get the documented element property.

        Returns
        -------
        "Element"
            Value of property documented element.
        """
        return self._documented_element

    @documented_element.setter
    def documented_element(self, value: "Element"):  # noqa: F821
        """
        Set the documented_element property.

        Parameters
        ----------
        value: "Element"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "documented_element", value)
        self._documented_element = value
