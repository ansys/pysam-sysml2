"""Generated send action usage class from metamodel."""

from __future__ import annotations

from .action_usage import ActionUsage


class SendActionUsage(ActionUsage):
    """Java class 'com.ansys.medini.metamodel.sysml.SendActionUsage'."""

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
        self._sender_argument = None

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
    def sender_argument(self) -> "Expression":  # noqa: F821
        """
        Get the sender argument property.

        Returns
        -------
        "Expression"
            Value of property sender argument.
        """
        return self._sender_argument
