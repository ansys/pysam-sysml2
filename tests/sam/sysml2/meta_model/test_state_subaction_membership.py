"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.state_subaction_membership import StateSubactionMembership


class TestStateSubactionMembership:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.StateSubactionMembership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return StateSubactionMembership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_kind(self, element):
        """Test getter and setter for kind property."""
        value = None
        element.kind = value
        assert element.kind == value

    def test_action(self, element):
        """Test getter and setter for action property."""
        value = "test_value"
        element.action = value
        assert element.action == value
