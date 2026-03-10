"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.occurrence_definition import OccurrenceDefinition


class TestOccurrenceDefinition:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.OccurrenceDefinition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return OccurrenceDefinition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_set_is_individual(self, element):
        """Test getter for set is individual property."""
        _ = element.set_is_individual

    def test_is_individual(self, element):
        """Test getter and setter for is individual property."""
        value = None
        element.is_individual = value
        assert element.is_individual == value

    def test_lifeclass(self, element):
        """Test getter and setter for lifeclass property."""
        value = "test_value"
        element.lifeclass = value
        assert element.lifeclass == value
