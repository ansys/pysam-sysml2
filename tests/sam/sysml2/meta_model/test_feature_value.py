"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.feature_value import FeatureValue


class TestFeatureValue:
    """Test class for Java class 'com.ansys.metamodel.sysml2.FeatureValue'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return FeatureValue("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_feature_with_value(self, element):
        """Test getter and setter for feature with value property."""
        value = "test_value"
        element.feature_with_value = value
        assert element.feature_with_value == value

    def test_value(self, element):
        """Test getter and setter for value property."""
        value = "test_value"
        element.value = value
        assert element.value == value

    def test_is_default(self, element):
        """Test getter and setter for is default property."""
        value = False
        element.is_default = value
        assert element.is_default == value

    def test_is_initial(self, element):
        """Test getter and setter for is initial property."""
        value = False
        element.is_initial = value
        assert element.is_initial == value
