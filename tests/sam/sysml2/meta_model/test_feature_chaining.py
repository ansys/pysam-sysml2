"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.feature_chaining import FeatureChaining


class TestFeatureChaining:
    """Test class for Java class 'com.ansys.metamodel.sysml2.FeatureChaining'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return FeatureChaining("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_chaining_feature(self, element):
        """Test getter and setter for chaining feature property."""
        value = "test_value"
        element.chaining_feature = value
        assert element.chaining_feature == value

    def test_feature_chained(self, element):
        """Test getter and setter for feature chained property."""
        value = "test_value"
        element.feature_chained = value
        assert element.feature_chained == value
