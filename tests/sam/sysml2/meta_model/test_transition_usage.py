"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest


from ansys.sam.sysml2.meta_model.transition_usage import TransitionUsage


class TestTransitionUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.TransitionUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return TransitionUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_effect_action(self, element):
        """Test getter for effect action property."""
        _ = element.effect_action

    def test_guard_expression(self, element):
        """Test getter for guard expression property."""
        _ = element.guard_expression

    def test_source(self, element):
        """Test getter and setter for source property."""
        value = "test_value"
        element.source = value
        assert element.source == value

    def test_succession(self, element):
        """Test getter and setter for succession property."""
        value = "test_value"
        element.succession = value
        assert element.succession == value

    def test_target(self, element):
        """Test getter and setter for target property."""
        value = "test_value"
        element.target = value
        assert element.target == value

    def test_trigger_action(self, element):
        """Test getter for trigger action property."""
        _ = element.trigger_action
