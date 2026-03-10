"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.loop_action_usage import LoopActionUsage


class TestLoopActionUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.LoopActionUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return LoopActionUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_body_action(self, element):
        """Test getter and setter for body action property."""
        value = "test_value"
        element.body_action = value
        assert element.body_action == value
