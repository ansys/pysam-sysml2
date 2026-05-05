"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest


from ansys.sam.sysml2.meta_model.occurrence_usage import OccurrenceUsage


class TestOccurrenceUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.OccurrenceUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return OccurrenceUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_individual_definition(self, element):
        """Test getter and setter for individual definition property."""
        value = "test_value"
        element.individual_definition = value
        assert element.individual_definition == value

    def test_occurrence_definition(self, element):
        """Test getter for occurrence definition property."""
        _ = element.occurrence_definition

    def test_portion_kind(self, element):
        """Test getter and setter for portion kind property."""
        value = "test_value"
        element.portion_kind = value
        assert element.portion_kind == value

    def test_is_individual(self, element):
        """Test getter and setter for is individual property."""
        value = False
        element.is_individual = value
        assert element.is_individual == value
