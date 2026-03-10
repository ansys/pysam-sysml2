"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.if_action_usage import IfActionUsage


class TestIfActionUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.IfActionUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return IfActionUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_if_argument(self, element):
        """Test getter and setter for if argument property."""
        value = None
        element.if_argument = value
        assert element.if_argument == value

    def test_then_action(self, element):
        """Test getter and setter for then action property."""
        value = "test_value"
        element.then_action = value
        assert element.then_action == value

    def test_else_action(self, element):
        """Test getter and setter for else action property."""
        value = "test_value"
        element.else_action = value
        assert element.else_action == value
