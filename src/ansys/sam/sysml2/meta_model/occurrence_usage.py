"""Generated occurrence usage class from metamodel."""

from __future__ import annotations

from ansys.sam.sysml2.data_structures.observed_list import ObservedList

from .usage import Usage


class OccurrenceUsage(Usage):
    """Java class 'com.ansys.metamodel.sysml2.OccurrenceUsage'."""

    def __init__(self, element_id: str):
        """Construct new instance.

        Parameters
        ----------
        element_id : str
            Element ID.

        """
        super().__init__(element_id)

        self._individual_definition = None
        self._occurrence_definition = ObservedList(self, "occurrence_definition")
        self._portion_kind = None
        self._is_individual = False

    @property
    def individual_definition(self) -> "OccurrenceDefinition":  # noqa: F821
        """
        Get the individual definition property.

        Returns
        -------
        "OccurrenceDefinition"
            Value of property individual definition.
        """
        return self._individual_definition

    @individual_definition.setter
    def individual_definition(self, value: "OccurrenceDefinition"):  # noqa: F821
        """
        Set the individual_definition property.

        Parameters
        ----------
        value: "OccurrenceDefinition"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "individual_definition", value)
        self._individual_definition = value

    @property
    def occurrence_definition(self) -> list["Class"]:  # noqa: F821
        """
        Get the occurrence definition property.

        Returns
        -------
        list["Class"]
            Value of property occurrence definition.
        """
        return self._occurrence_definition

    @property
    def portion_kind(self) -> "PortionKind":  # noqa: F821
        """
        Get the portion kind property.

        Returns
        -------
        "PortionKind"
            Value of property portion kind.
        """
        return self._portion_kind

    @portion_kind.setter
    def portion_kind(self, value: "PortionKind"):  # noqa: F821
        """
        Set the portion_kind property.

        Parameters
        ----------
        value: "PortionKind"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "portion_kind", value)
        self._portion_kind = value

    @property
    def is_individual(self) -> bool:  # noqa: F821
        """
        Get the is individual property.

        Returns
        -------
        bool
            Value of property is individual.
        """
        return self._is_individual

    @is_individual.setter
    def is_individual(self, value: bool):  # noqa: F821
        """
        Set the is_individual property.

        Parameters
        ----------
        value: bool
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "is_individual", value)
        self._is_individual = value
