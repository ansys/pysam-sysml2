"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest


from ansys.sam.sysml2.meta_model.state_definition import StateDefinition


class TestStateDefinition:
    """Test class for Java class 'com.ansys.metamodel.sysml2.StateDefinition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return StateDefinition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_do_action(self, element):
        """Test getter and setter for do action property."""
        value = "test_value"
        element.do_action = value
        assert element.do_action == value

    def test_entry_action(self, element):
        """Test getter and setter for entry action property."""
        value = "test_value"
        element.entry_action = value
        assert element.entry_action == value

    def test_exit_action(self, element):
        """Test getter and setter for exit action property."""
        value = "test_value"
        element.exit_action = value
        assert element.exit_action == value

    def test_state(self, element):
        """Test getter for state property."""
        _ = element.state

    def test_is_parallel(self, element):
        """Test getter and setter for is parallel property."""
        value = False
        element.is_parallel = value
        assert element.is_parallel == value
