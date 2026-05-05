"""Generated membership import class from metamodel."""

from __future__ import annotations

from .import_ import Import


class MembershipImport(Import):
    """Java class 'com.ansys.metamodel.sysml2.MembershipImport'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._imported_membership = None

    @property
    def imported_membership(self) -> "Membership":  # noqa: F821
        """
        Get the imported membership property.

        Returns
        -------
        "Membership"
            Value of property imported membership.
        """
        return self._imported_membership

    @imported_membership.setter
    def imported_membership(self, value: "Membership"):  # noqa: F821
        """
        Set the imported_membership property.

        Parameters
        ----------
        value: "Membership"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "imported_membership", value)
        self._imported_membership = value
