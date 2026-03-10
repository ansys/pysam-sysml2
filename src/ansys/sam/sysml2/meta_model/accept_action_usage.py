"""Generated accept action usage class from metamodel."""

from __future__ import annotations

from .action_usage import ActionUsage


class AcceptActionUsage(ActionUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.AcceptActionUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._payload_argument = None
        self._receiver_argument = None
        self._payload_parameter = None

    @property
    def payload_argument(self) -> "Expression":  # noqa: F821
        """
        Get the payload argument property.

        Returns
        -------
        "Expression"
            Value of property payload argument.
        """
        return self._payload_argument

    @property
    def receiver_argument(self) -> "Expression":  # noqa: F821
        """
        Get the receiver argument property.

        Returns
        -------
        "Expression"
            Value of property receiver argument.
        """
        return self._receiver_argument

    @property
    def payload_parameter(self) -> "ReferenceUsage":  # noqa: F821
        """
        Get the payload parameter property.

        Returns
        -------
        "ReferenceUsage"
            Value of property payload parameter.
        """
        return self._payload_parameter
