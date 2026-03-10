"""Generated metadata usage class from metamodel."""

from __future__ import annotations

from .item_usage import ItemUsage
from .metadata_feature import MetadataFeature


class MetadataUsage(ItemUsage, MetadataFeature):
    """Java class 'com.ansys.medini.metamodel.sysml.MetadataUsage'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._metadata_definition = None

    @property
    def metadata_definition(self) -> None:  # noqa: F821
        """
        Get the metadata definition property.

        Returns
        -------
        None
            Value of property metadata definition.
        """
        return self._metadata_definition

    @metadata_definition.setter
    def metadata_definition(self, value: None):  # noqa: F821
        """
        Set the metadata_definition property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "metadata_definition", value)
        self._metadata_definition = value
