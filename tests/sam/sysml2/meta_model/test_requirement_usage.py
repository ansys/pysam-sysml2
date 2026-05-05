"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest


from ansys.sam.sysml2.meta_model.requirement_usage import RequirementUsage


class TestRequirementUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.RequirementUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return RequirementUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_actor_parameter(self, element):
        """Test getter for actor parameter property."""
        _ = element.actor_parameter

    def test_assumed_constraint(self, element):
        """Test getter for assumed constraint property."""
        _ = element.assumed_constraint

    def test_framed_concern(self, element):
        """Test getter for framed concern property."""
        _ = element.framed_concern

    def test_req_id(self, element):
        """Test getter and setter for req id property."""
        value = ""
        element.req_id = value
        assert element.req_id == value

    def test_required_constraint(self, element):
        """Test getter for required constraint property."""
        _ = element.required_constraint

    def test_requirement_definition(self, element):
        """Test getter and setter for requirement definition property."""
        value = "test_value"
        element.requirement_definition = value
        assert element.requirement_definition == value

    def test_stakeholder_parameter(self, element):
        """Test getter for stakeholder parameter property."""
        _ = element.stakeholder_parameter

    def test_subject_parameter(self, element):
        """Test getter and setter for subject parameter property."""
        value = "test_value"
        element.subject_parameter = value
        assert element.subject_parameter == value

    def test_text(self, element):
        """Test getter for text property."""
        _ = element.text
