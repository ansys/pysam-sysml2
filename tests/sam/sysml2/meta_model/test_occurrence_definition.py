"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.occurrence_definition import OccurrenceDefinition


class TestOccurrenceDefinition:
    """Test class for Java class 'com.ansys.metamodel.sysml2.OccurrenceDefinition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return OccurrenceDefinition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_is_individual(self, element):
        """Test getter and setter for is individual property."""
        value = False
        element.is_individual = value
        assert element.is_individual == value
