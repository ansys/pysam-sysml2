"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.perform_action_usage import PerformActionUsage


class TestPerformActionUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.PerformActionUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return PerformActionUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_performed_action(self, element):
        """Test getter and setter for performed action property."""
        value = "test_value"
        element.performed_action = value
        assert element.performed_action == value
