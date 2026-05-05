"""Generated subject membership class from metamodel."""

from __future__ import annotations

from .parameter_membership import ParameterMembership


class SubjectMembership(ParameterMembership):
    """Java class 'com.ansys.metamodel.sysml2.SubjectMembership'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._owned_subject_parameter = None

    @property
    def owned_subject_parameter(self) -> "Usage":  # noqa: F821
        """
        Get the owned subject parameter property.

        Returns
        -------
        "Usage"
            Value of property owned subject parameter.
        """
        return self._owned_subject_parameter

    @owned_subject_parameter.setter
    def owned_subject_parameter(self, value: "Usage"):  # noqa: F821
        """
        Set the owned_subject_parameter property.

        Parameters
        ----------
        value: "Usage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_subject_parameter", value)
        self._owned_subject_parameter = value
