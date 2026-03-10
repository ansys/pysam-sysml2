"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.for_loop_action_usage import ForLoopActionUsage


class TestForLoopActionUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.ForLoopActionUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ForLoopActionUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_loop_variable(self, element):
        """Test getter and setter for loop variable property."""
        value = None
        element.loop_variable = value
        assert element.loop_variable == value
