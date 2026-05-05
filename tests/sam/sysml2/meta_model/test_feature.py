"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest


from ansys.sam.sysml2.meta_model.feature import Feature


class TestFeature:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Feature'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Feature("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_chaining_feature(self, element):
        """Test getter for chaining feature property."""
        _ = element.chaining_feature

    def test_cross_feature(self, element):
        """Test getter and setter for cross feature property."""
        value = "test_value"
        element.cross_feature = value
        assert element.cross_feature == value

    def test_direction(self, element):
        """Test getter and setter for direction property."""
        value = "test_value"
        element.direction = value
        assert element.direction == value

    def test_endfeaturemembership(self, element):
        """Test getter and setter for endfeaturemembership property."""
        value = "test_value"
        element.endfeaturemembership = value
        assert element.endfeaturemembership == value

    def test_feature_target(self, element):
        """Test getter and setter for feature target property."""
        value = "test_value"
        element.feature_target = value
        assert element.feature_target == value

    def test_featuring_type(self, element):
        """Test getter for featuring type property."""
        _ = element.featuring_type

    def test_owned_cross_subsetting(self, element):
        """Test getter and setter for owned cross subsetting property."""
        value = "test_value"
        element.owned_cross_subsetting = value
        assert element.owned_cross_subsetting == value

    def test_owned_feature_chaining(self, element):
        """Test getter for owned feature chaining property."""
        _ = element.owned_feature_chaining

    def test_owned_feature_inverting(self, element):
        """Test getter for owned feature inverting property."""
        _ = element.owned_feature_inverting

    def test_owned_redefinition(self, element):
        """Test getter for owned redefinition property."""
        _ = element.owned_redefinition

    def test_owned_reference_subsetting(self, element):
        """Test getter and setter for owned reference subsetting property."""
        value = "test_value"
        element.owned_reference_subsetting = value
        assert element.owned_reference_subsetting == value

    def test_owned_subsetting(self, element):
        """Test getter for owned subsetting property."""
        _ = element.owned_subsetting

    def test_owned_type_featuring(self, element):
        """Test getter for owned type featuring property."""
        _ = element.owned_type_featuring

    def test_owned_typing(self, element):
        """Test getter for owned typing property."""
        _ = element.owned_typing

    def test_owning_feature_membership(self, element):
        """Test getter and setter for owning feature membership property."""
        value = "test_value"
        element.owning_feature_membership = value
        assert element.owning_feature_membership == value

    def test_owning_type(self, element):
        """Test getter and setter for owning type property."""
        value = "test_value"
        element.owning_type = value
        assert element.owning_type == value

    def test_type_(self, element):
        """Test getter for type property."""
        _ = element.type_

    def test_valuation(self, element):
        """Test getter and setter for valuation property."""
        value = "test_value"
        element.valuation = value
        assert element.valuation == value

    def test_cartesian_product(self, element):
        """Test getter for cartesian product property."""
        _ = element.cartesian_product

    def test_compatible_with(self, element):
        """Test getter for compatible with property."""
        _ = element.compatible_with

    def test_featured_within(self, element):
        """Test getter for featured within property."""
        _ = element.featured_within

    def test_is_composite(self, element):
        """Test getter and setter for is composite property."""
        value = False
        element.is_composite = value
        assert element.is_composite == value

    def test_is_constant(self, element):
        """Test getter and setter for is constant property."""
        value = False
        element.is_constant = value
        assert element.is_constant == value

    def test_is_derived(self, element):
        """Test getter and setter for is derived property."""
        value = False
        element.is_derived = value
        assert element.is_derived == value

    def test_is_end(self, element):
        """Test getter and setter for is end property."""
        value = False
        element.is_end = value
        assert element.is_end == value

    def test_is_ordered(self, element):
        """Test getter and setter for is ordered property."""
        value = False
        element.is_ordered = value
        assert element.is_ordered == value

    def test_is_portion(self, element):
        """Test getter and setter for is portion property."""
        value = False
        element.is_portion = value
        assert element.is_portion == value

    def test_is_unique(self, element):
        """Test getter and setter for is unique property."""
        value = False
        element.is_unique = value
        assert element.is_unique == value

    def test_is_variable(self, element):
        """Test getter and setter for is variable property."""
        value = False
        element.is_variable = value
        assert element.is_variable == value

    def test_owned_cross_feature(self, element):
        """Test getter for owned cross feature property."""
        _ = element.owned_cross_feature

    def test_set_direction(self, element):
        """Test getter for set direction property."""
        _ = element.set_direction
