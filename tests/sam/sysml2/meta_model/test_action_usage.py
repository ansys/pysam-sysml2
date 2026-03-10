"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.action_usage import ActionUsage


class TestActionUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.ActionUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ActionUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_action_definition(self, element):
        """Test getter for action definition property."""
        _ = element.action_definition
