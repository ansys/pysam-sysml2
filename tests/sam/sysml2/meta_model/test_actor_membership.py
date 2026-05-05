"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.actor_membership import ActorMembership


class TestActorMembership:
    """Test class for Java class 'com.ansys.metamodel.sysml2.ActorMembership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ActorMembership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_owned_actor_parameter(self, element):
        """Test getter and setter for owned actor parameter property."""
        value = "test_value"
        element.owned_actor_parameter = value
        assert element.owned_actor_parameter == value
