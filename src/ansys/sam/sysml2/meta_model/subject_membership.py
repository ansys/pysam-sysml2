"""Generated subject membership class from metamodel."""

from __future__ import annotations

from .parameter_membership import ParameterMembership


class SubjectMembership(ParameterMembership):
    """Java class 'com.ansys.medini.metamodel.sysml.SubjectMembership'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._owned_subject_parameter = None

    @property
    def owned_subject_parameter(self) -> None:  # noqa: F821
        """
        Get the owned subject parameter property.

        Returns
        -------
        None
            Value of property owned subject parameter.
        """
        return self._owned_subject_parameter

    @owned_subject_parameter.setter
    def owned_subject_parameter(self, value: None):  # noqa: F821
        """
        Set the owned_subject_parameter property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_subject_parameter", value)
        self._owned_subject_parameter = value
