"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.terminate_action_usage import TerminateActionUsage


class TestTerminateActionUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.TerminateActionUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return TerminateActionUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_terminated_occurrence_argument(self, element):
        """Test getter and setter for terminated occurrence argument property."""
        value = "test_value"
        element.terminated_occurrence_argument = value
        assert element.terminated_occurrence_argument == value
