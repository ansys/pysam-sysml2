"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest


from ansys.sam.sysml2.meta_model.case_usage import CaseUsage


class TestCaseUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.CaseUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return CaseUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_actor_parameter(self, element):
        """Test getter for actor parameter property."""
        _ = element.actor_parameter

    def test_case_definition(self, element):
        """Test getter and setter for case definition property."""
        value = "test_value"
        element.case_definition = value
        assert element.case_definition == value

    def test_objective_requirement(self, element):
        """Test getter and setter for objective requirement property."""
        value = "test_value"
        element.objective_requirement = value
        assert element.objective_requirement == value

    def test_subject_parameter(self, element):
        """Test getter and setter for subject parameter property."""
        value = "test_value"
        element.subject_parameter = value
        assert element.subject_parameter == value
