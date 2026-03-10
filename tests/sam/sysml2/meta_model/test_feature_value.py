"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.feature_value import FeatureValue


class TestFeatureValue:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.FeatureValue'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return FeatureValue("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_value(self, element):
        """Test getter and setter for value property."""
        value = "test_value"
        element.value = value
        assert element.value == value

    def test_set_is_initial(self, element):
        """Test getter for set is initial property."""
        _ = element.set_is_initial

    def test_is_default(self, element):
        """Test getter and setter for is default property."""
        value = False
        element.is_default = value
        assert element.is_default == value

    def test_set_is_default(self, element):
        """Test getter for set is default property."""
        _ = element.set_is_default

    def test_is_initial(self, element):
        """Test getter and setter for is initial property."""
        value = False
        element.is_initial = value
        assert element.is_initial == value
