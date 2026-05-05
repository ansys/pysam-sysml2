"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.exhibit_state_usage import ExhibitStateUsage


class TestExhibitStateUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.ExhibitStateUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ExhibitStateUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_exhibited_state(self, element):
        """Test getter and setter for exhibited state property."""
        value = "test_value"
        element.exhibited_state = value
        assert element.exhibited_state == value
