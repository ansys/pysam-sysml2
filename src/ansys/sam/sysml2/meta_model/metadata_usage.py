"""Generated metadata usage class from metamodel."""

from __future__ import annotations

from .item_usage import ItemUsage
from .metadata_feature import MetadataFeature


class MetadataUsage(MetadataFeature, ItemUsage):
    """Java class 'com.ansys.metamodel.sysml2.MetadataUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._metadata_definition = None

    @property
    def metadata_definition(self) -> "Metaclass":  # noqa: F821
        """
        Get the metadata definition property.

        Returns
        -------
        "Metaclass"
            Value of property metadata definition.
        """
        return self._metadata_definition

    @metadata_definition.setter
    def metadata_definition(self, value: "Metaclass"):  # noqa: F821
        """
        Set the metadata_definition property.

        Parameters
        ----------
        value: "Metaclass"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "metadata_definition", value)
        self._metadata_definition = value
