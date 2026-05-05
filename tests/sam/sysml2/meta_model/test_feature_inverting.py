"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.feature_inverting import FeatureInverting


class TestFeatureInverting:
    """Test class for Java class 'com.ansys.metamodel.sysml2.FeatureInverting'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return FeatureInverting("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_feature_inverted(self, element):
        """Test getter and setter for feature inverted property."""
        value = "test_value"
        element.feature_inverted = value
        assert element.feature_inverted == value

    def test_inverting_feature(self, element):
        """Test getter and setter for inverting feature property."""
        value = "test_value"
        element.inverting_feature = value
        assert element.inverting_feature == value

    def test_owning_feature(self, element):
        """Test getter and setter for owning feature property."""
        value = "test_value"
        element.owning_feature = value
        assert element.owning_feature == value
