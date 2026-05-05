"""Generated  test class from metamodel."""

import pytest


from ansys.sam.sysml2.meta_model.action_definition import ActionDefinition


class TestActionDefinition:
    """Test class for Java class 'com.ansys.metamodel.sysml2.ActionDefinition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ActionDefinition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_action(self, element):
        """Test getter for action property."""
        _ = element.action
