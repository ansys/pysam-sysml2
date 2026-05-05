"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest


from ansys.sam.sysml2.meta_model.definition import Definition


class TestDefinition:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Definition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Definition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_directed_usage(self, element):
        """Test getter for directed usage property."""
        _ = element.directed_usage

    def test_owned_action(self, element):
        """Test getter for owned action property."""
        _ = element.owned_action

    def test_owned_allocation(self, element):
        """Test getter for owned allocation property."""
        _ = element.owned_allocation

    def test_owned_analysis_case(self, element):
        """Test getter for owned analysis case property."""
        _ = element.owned_analysis_case

    def test_owned_attribute(self, element):
        """Test getter for owned attribute property."""
        _ = element.owned_attribute

    def test_owned_calculation(self, element):
        """Test getter for owned calculation property."""
        _ = element.owned_calculation

    def test_owned_case(self, element):
        """Test getter for owned case property."""
        _ = element.owned_case

    def test_owned_concern(self, element):
        """Test getter for owned concern property."""
        _ = element.owned_concern

    def test_owned_connection(self, element):
        """Test getter for owned connection property."""
        _ = element.owned_connection

    def test_owned_constraint(self, element):
        """Test getter for owned constraint property."""
        _ = element.owned_constraint

    def test_owned_enumeration(self, element):
        """Test getter for owned enumeration property."""
        _ = element.owned_enumeration

    def test_owned_flow(self, element):
        """Test getter for owned flow property."""
        _ = element.owned_flow

    def test_owned_interface(self, element):
        """Test getter for owned interface property."""
        _ = element.owned_interface

    def test_owned_item(self, element):
        """Test getter for owned item property."""
        _ = element.owned_item

    def test_owned_metadata(self, element):
        """Test getter for owned metadata property."""
        _ = element.owned_metadata

    def test_owned_occurrence(self, element):
        """Test getter for owned occurrence property."""
        _ = element.owned_occurrence

    def test_owned_part(self, element):
        """Test getter for owned part property."""
        _ = element.owned_part

    def test_owned_port(self, element):
        """Test getter for owned port property."""
        _ = element.owned_port

    def test_owned_reference(self, element):
        """Test getter for owned reference property."""
        _ = element.owned_reference

    def test_owned_rendering(self, element):
        """Test getter for owned rendering property."""
        _ = element.owned_rendering

    def test_owned_requirement(self, element):
        """Test getter for owned requirement property."""
        _ = element.owned_requirement

    def test_owned_state(self, element):
        """Test getter for owned state property."""
        _ = element.owned_state

    def test_owned_transition(self, element):
        """Test getter for owned transition property."""
        _ = element.owned_transition

    def test_owned_usage(self, element):
        """Test getter for owned usage property."""
        _ = element.owned_usage

    def test_owned_use_case(self, element):
        """Test getter for owned use case property."""
        _ = element.owned_use_case

    def test_owned_verification_case(self, element):
        """Test getter for owned verification case property."""
        _ = element.owned_verification_case

    def test_owned_view(self, element):
        """Test getter for owned view property."""
        _ = element.owned_view

    def test_owned_viewpoint(self, element):
        """Test getter for owned viewpoint property."""
        _ = element.owned_viewpoint

    def test_usage(self, element):
        """Test getter for usage property."""
        _ = element.usage

    def test_variant(self, element):
        """Test getter for variant property."""
        _ = element.variant

    def test_variant_membership(self, element):
        """Test getter for variant membership property."""
        _ = element.variant_membership

    def test_is_variation(self, element):
        """Test getter and setter for is variation property."""
        value = False
        element.is_variation = value
        assert element.is_variation == value
