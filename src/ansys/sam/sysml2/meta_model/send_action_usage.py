"""Generated send action usage class from metamodel."""

from __future__ import annotations

from .action_usage import ActionUsage


class SendActionUsage(ActionUsage):
    """Java class 'com.ansys.metamodel.sysml2.SendActionUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

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

    @payload_argument.setter
    def payload_argument(self, value: "Expression"):  # noqa: F821
        """
        Set the payload_argument property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "payload_argument", value)
        self._payload_argument = value

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

    @receiver_argument.setter
    def receiver_argument(self, value: "Expression"):  # noqa: F821
        """
        Set the receiver_argument property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "receiver_argument", value)
        self._receiver_argument = value

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

    @sender_argument.setter
    def sender_argument(self, value: "Expression"):  # noqa: F821
        """
        Set the sender_argument property.

        Parameters
        ----------
        value: "Expression"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "sender_argument", value)
        self._sender_argument = value
