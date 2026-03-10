"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.state_usage import StateUsage


class TestStateUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.StateUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return StateUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_set_exit_action(self, element):
        """Test getter for set exit action property."""
        _ = element.set_exit_action

    def test_exit_action(self, element):
        """Test getter and setter for exit action property."""
        value = None
        element.exit_action = value
        assert element.exit_action == value

    def test_state_definition(self, element):
        """Test getter for state definition property."""
        _ = element.state_definition

    def test_do_action(self, element):
        """Test getter and setter for do action property."""
        value = "test_value"
        element.do_action = value
        assert element.do_action == value

    def test_set_is_parallel(self, element):
        """Test getter for set is parallel property."""
        _ = element.set_is_parallel

    def test_set_do_action(self, element):
        """Test getter for set do action property."""
        _ = element.set_do_action

    def test_entry_action(self, element):
        """Test getter and setter for entry action property."""
        value = "test_value"
        element.entry_action = value
        assert element.entry_action == value

    def test_is_parallel(self, element):
        """Test getter and setter for is parallel property."""
        value = False
        element.is_parallel = value
        assert element.is_parallel == value

    def test_set_entry_action(self, element):
        """Test getter for set entry action property."""
        _ = element.set_entry_action
