"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest


from ansys.sam.sysml2.meta_model.usage import Usage


class TestUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Usage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Usage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_definition(self, element):
        """Test getter for definition property."""
        _ = element.definition

    def test_directed_usage(self, element):
        """Test getter for directed usage property."""
        _ = element.directed_usage

    def test_nested_action(self, element):
        """Test getter for nested action property."""
        _ = element.nested_action

    def test_nested_allocation(self, element):
        """Test getter for nested allocation property."""
        _ = element.nested_allocation

    def test_nested_analysis_case(self, element):
        """Test getter for nested analysis case property."""
        _ = element.nested_analysis_case

    def test_nested_attribute(self, element):
        """Test getter for nested attribute property."""
        _ = element.nested_attribute

    def test_nested_calculation(self, element):
        """Test getter for nested calculation property."""
        _ = element.nested_calculation

    def test_nested_case(self, element):
        """Test getter for nested case property."""
        _ = element.nested_case

    def test_nested_concern(self, element):
        """Test getter for nested concern property."""
        _ = element.nested_concern

    def test_nested_connection(self, element):
        """Test getter for nested connection property."""
        _ = element.nested_connection

    def test_nested_constraint(self, element):
        """Test getter for nested constraint property."""
        _ = element.nested_constraint

    def test_nested_enumeration(self, element):
        """Test getter for nested enumeration property."""
        _ = element.nested_enumeration

    def test_nested_flow(self, element):
        """Test getter for nested flow property."""
        _ = element.nested_flow

    def test_nested_interface(self, element):
        """Test getter for nested interface property."""
        _ = element.nested_interface

    def test_nested_item(self, element):
        """Test getter for nested item property."""
        _ = element.nested_item

    def test_nested_metadata(self, element):
        """Test getter for nested metadata property."""
        _ = element.nested_metadata

    def test_nested_occurrence(self, element):
        """Test getter for nested occurrence property."""
        _ = element.nested_occurrence

    def test_nested_part(self, element):
        """Test getter for nested part property."""
        _ = element.nested_part

    def test_nested_port(self, element):
        """Test getter for nested port property."""
        _ = element.nested_port

    def test_nested_reference(self, element):
        """Test getter for nested reference property."""
        _ = element.nested_reference

    def test_nested_rendering(self, element):
        """Test getter for nested rendering property."""
        _ = element.nested_rendering

    def test_nested_requirement(self, element):
        """Test getter for nested requirement property."""
        _ = element.nested_requirement

    def test_nested_state(self, element):
        """Test getter for nested state property."""
        _ = element.nested_state

    def test_nested_transition(self, element):
        """Test getter for nested transition property."""
        _ = element.nested_transition

    def test_nested_usage(self, element):
        """Test getter for nested usage property."""
        _ = element.nested_usage

    def test_nested_use_case(self, element):
        """Test getter for nested use case property."""
        _ = element.nested_use_case

    def test_nested_verification_case(self, element):
        """Test getter for nested verification case property."""
        _ = element.nested_verification_case

    def test_nested_view(self, element):
        """Test getter for nested view property."""
        _ = element.nested_view

    def test_nested_viewpoint(self, element):
        """Test getter for nested viewpoint property."""
        _ = element.nested_viewpoint

    def test_owning_definition(self, element):
        """Test getter and setter for owning definition property."""
        value = "test_value"
        element.owning_definition = value
        assert element.owning_definition == value

    def test_owning_usage(self, element):
        """Test getter and setter for owning usage property."""
        value = "test_value"
        element.owning_usage = value
        assert element.owning_usage == value

    def test_usage(self, element):
        """Test getter for usage property."""
        _ = element.usage

    def test_variant(self, element):
        """Test getter for variant property."""
        _ = element.variant

    def test_variant_membership(self, element):
        """Test getter for variant membership property."""
        _ = element.variant_membership

    def test_is_reference(self, element):
        """Test getter and setter for is reference property."""
        value = False
        element.is_reference = value
        assert element.is_reference == value

    def test_is_variation(self, element):
        """Test getter and setter for is variation property."""
        value = False
        element.is_variation = value
        assert element.is_variation == value

    def test_may_time_vary(self, element):
        """Test getter and setter for may time vary property."""
        value = False
        element.may_time_vary = value
        assert element.may_time_vary == value
