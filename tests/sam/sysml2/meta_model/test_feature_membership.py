"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.feature_membership import FeatureMembership


class TestFeatureMembership:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.FeatureMembership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return FeatureMembership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_member_feature(self, element):
        """Test getter and setter for member feature property."""
        value = "test_value"
        element.member_feature = value
        assert element.member_feature == value

    def test_owning_type(self, element):
        """Test getter and setter for owning type property."""
        value = "test_value"
        element.owning_type = value
        assert element.owning_type == value

    def test_is_composite(self, element):
        """Test getter and setter for is composite property."""
        value = False
        element.is_composite = value
        assert element.is_composite == value

    def test_direction(self, element):
        """Test getter and setter for direction property."""
        value = "test_value"
        element.direction = value
        assert element.direction == value

    def test_owned_member_feature(self, element):
        """Test getter and setter for owned member feature property."""
        value = "test_value"
        element.owned_member_feature = value
        assert element.owned_member_feature == value
