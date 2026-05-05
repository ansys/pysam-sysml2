"""Generated actor membership class from metamodel."""

from __future__ import annotations

from .parameter_membership import ParameterMembership


class ActorMembership(ParameterMembership):
    """Java class 'com.ansys.metamodel.sysml2.ActorMembership'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._owned_actor_parameter = None

    @property
    def owned_actor_parameter(self) -> "PartUsage":  # noqa: F821
        """
        Get the owned actor parameter property.

        Returns
        -------
        "PartUsage"
            Value of property owned actor parameter.
        """
        return self._owned_actor_parameter

    @owned_actor_parameter.setter
    def owned_actor_parameter(self, value: "PartUsage"):  # noqa: F821
        """
        Set the owned_actor_parameter property.

        Parameters
        ----------
        value: "PartUsage"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owned_actor_parameter", value)
        self._owned_actor_parameter = value
