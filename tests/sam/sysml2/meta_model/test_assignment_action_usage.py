"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.assignment_action_usage import AssignmentActionUsage


class TestAssignmentActionUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.AssignmentActionUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return AssignmentActionUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_value_expression(self, element):
        """Test getter for value expression property."""
        _ = element.value_expression

    def test_target_argument(self, element):
        """Test getter for target argument property."""
        _ = element.target_argument

    def test_referent(self, element):
        """Test getter for referent property."""
        _ = element.referent
