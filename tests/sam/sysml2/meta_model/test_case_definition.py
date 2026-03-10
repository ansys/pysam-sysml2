"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.case_definition import CaseDefinition


class TestCaseDefinition:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.CaseDefinition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return CaseDefinition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_actor_parameter(self, element):
        """Test getter for actor parameter property."""
        _ = element.actor_parameter

    def test_objective_requirement(self, element):
        """Test getter and setter for objective requirement property."""
        value = None
        element.objective_requirement = value
        assert element.objective_requirement == value

    def test_subject_parameter(self, element):
        """Test getter and setter for subject parameter property."""
        value = "test_value"
        element.subject_parameter = value
        assert element.subject_parameter == value
