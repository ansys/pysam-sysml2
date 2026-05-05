"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.cross_subsetting import CrossSubsetting


class TestCrossSubsetting:
    """Test class for Java class 'com.ansys.metamodel.sysml2.CrossSubsetting'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return CrossSubsetting("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_crossed_feature(self, element):
        """Test getter and setter for crossed feature property."""
        value = "test_value"
        element.crossed_feature = value
        assert element.crossed_feature == value

    def test_crossing_feature(self, element):
        """Test getter and setter for crossing feature property."""
        value = "test_value"
        element.crossing_feature = value
        assert element.crossing_feature == value
