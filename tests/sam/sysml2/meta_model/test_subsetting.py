"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.subsetting import Subsetting


class TestSubsetting:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Subsetting'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Subsetting("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_owning_feature(self, element):
        """Test getter and setter for owning feature property."""
        value = "test_value"
        element.owning_feature = value
        assert element.owning_feature == value

    def test_subsetted_feature(self, element):
        """Test getter and setter for subsetted feature property."""
        value = "test_value"
        element.subsetted_feature = value
        assert element.subsetted_feature == value

    def test_subsetting_feature(self, element):
        """Test getter and setter for subsetting feature property."""
        value = "test_value"
        element.subsetting_feature = value
        assert element.subsetting_feature == value
