"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.assignment_action_usage import AssignmentActionUsage


class TestAssignmentActionUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.AssignmentActionUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return AssignmentActionUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_referent(self, element):
        """Test getter and setter for referent property."""
        value = "test_value"
        element.referent = value
        assert element.referent == value

    def test_target_argument(self, element):
        """Test getter and setter for target argument property."""
        value = "test_value"
        element.target_argument = value
        assert element.target_argument == value

    def test_value_expression(self, element):
        """Test getter and setter for value expression property."""
        value = "test_value"
        element.value_expression = value
        assert element.value_expression == value
