"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.event_occurrence_usage import EventOccurrenceUsage


class TestEventOccurrenceUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.EventOccurrenceUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return EventOccurrenceUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_event_occurrence(self, element):
        """Test getter and setter for event occurrence property."""
        value = "test_value"
        element.event_occurrence = value
        assert element.event_occurrence == value

    def test_is_reference(self, element):
        """Test getter and setter for is reference property."""
        value = False
        element.is_reference = value
        assert element.is_reference == value
