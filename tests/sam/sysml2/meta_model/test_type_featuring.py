"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.type_featuring import TypeFeaturing


class TestTypeFeaturing:
    """Test class for Java class 'com.ansys.metamodel.sysml2.TypeFeaturing'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return TypeFeaturing("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_feature_of_type(self, element):
        """Test getter and setter for feature of type property."""
        value = "test_value"
        element.feature_of_type = value
        assert element.feature_of_type == value

    def test_featuring_type(self, element):
        """Test getter and setter for featuring type property."""
        value = "test_value"
        element.featuring_type = value
        assert element.featuring_type == value

    def test_owning_feature_of_type(self, element):
        """Test getter and setter for owning feature of type property."""
        value = "test_value"
        element.owning_feature_of_type = value
        assert element.owning_feature_of_type == value
