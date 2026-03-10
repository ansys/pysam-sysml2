"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.while_loop_action_usage import WhileLoopActionUsage


class TestWhileLoopActionUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.WhileLoopActionUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return WhileLoopActionUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_while_argument(self, element):
        """Test getter and setter for while argument property."""
        value = None
        element.while_argument = value
        assert element.while_argument == value

    def test_until_argument(self, element):
        """Test getter and setter for until argument property."""
        value = "test_value"
        element.until_argument = value
        assert element.until_argument == value
