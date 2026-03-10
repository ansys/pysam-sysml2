"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.succession import Succession


class TestSuccession:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.Succession'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Succession("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_guard_expression(self, element):
        """Test getter for guard expression property."""
        _ = element.guard_expression

    def test_transition_step(self, element):
        """Test getter and setter for transition step property."""
        value = "test_value"
        element.transition_step = value
        assert element.transition_step == value

    def test_trigger_step(self, element):
        """Test getter for trigger step property."""
        _ = element.trigger_step

    def test_effect_step(self, element):
        """Test getter for effect step property."""
        _ = element.effect_step
