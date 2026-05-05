"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest


from ansys.sam.sysml2.meta_model.type_ import Type


class TestType:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Type'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Type("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_differencing_type(self, element):
        """Test getter for differencing type property."""
        _ = element.differencing_type

    def test_directed_feature(self, element):
        """Test getter for directed feature property."""
        _ = element.directed_feature

    def test_end_feature(self, element):
        """Test getter for end feature property."""
        _ = element.end_feature

    def test_feature(self, element):
        """Test getter for feature property."""
        _ = element.feature

    def test_feature_membership(self, element):
        """Test getter for feature membership property."""
        _ = element.feature_membership

    def test_inherited_feature(self, element):
        """Test getter for inherited feature property."""
        _ = element.inherited_feature

    def test_inherited_membership(self, element):
        """Test getter for inherited membership property."""
        _ = element.inherited_membership

    def test_input(self, element):
        """Test getter for input property."""
        _ = element.input

    def test_intersecting_type(self, element):
        """Test getter for intersecting type property."""
        _ = element.intersecting_type

    def test_multiplicity(self, element):
        """Test getter and setter for multiplicity property."""
        value = "test_value"
        element.multiplicity = value
        assert element.multiplicity == value

    def test_output(self, element):
        """Test getter for output property."""
        _ = element.output

    def test_owned_conjugator(self, element):
        """Test getter and setter for owned conjugator property."""
        value = "test_value"
        element.owned_conjugator = value
        assert element.owned_conjugator == value

    def test_owned_differencing(self, element):
        """Test getter for owned differencing property."""
        _ = element.owned_differencing

    def test_owned_disjoining(self, element):
        """Test getter for owned disjoining property."""
        _ = element.owned_disjoining

    def test_owned_end_feature(self, element):
        """Test getter for owned end feature property."""
        _ = element.owned_end_feature

    def test_owned_feature(self, element):
        """Test getter for owned feature property."""
        _ = element.owned_feature

    def test_owned_feature_membership(self, element):
        """Test getter for owned feature membership property."""
        _ = element.owned_feature_membership

    def test_owned_intersecting(self, element):
        """Test getter for owned intersecting property."""
        _ = element.owned_intersecting

    def test_owned_specialization(self, element):
        """Test getter for owned specialization property."""
        _ = element.owned_specialization

    def test_owned_unioning(self, element):
        """Test getter for owned unioning property."""
        _ = element.owned_unioning

    def test_unioning_type(self, element):
        """Test getter for unioning type property."""
        _ = element.unioning_type

    def test_compatible_with(self, element):
        """Test getter for compatible with property."""
        _ = element.compatible_with

    def test_is_abstract(self, element):
        """Test getter and setter for is abstract property."""
        value = False
        element.is_abstract = value
        assert element.is_abstract == value

    def test_is_conjugated(self, element):
        """Test getter for is conjugated property."""
        _ = element.is_conjugated

    def test_is_sufficient(self, element):
        """Test getter and setter for is sufficient property."""
        value = False
        element.is_sufficient = value
        assert element.is_sufficient == value

    def test_set_is_abstract(self, element):
        """Test getter for set is abstract property."""
        _ = element.set_is_abstract

    def test_set_is_sufficient(self, element):
        """Test getter for set is sufficient property."""
        _ = element.set_is_sufficient
