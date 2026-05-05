"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.accept_action_usage import AcceptActionUsage


class TestAcceptActionUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.AcceptActionUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return AcceptActionUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_payload_argument(self, element):
        """Test getter and setter for payload argument property."""
        value = "test_value"
        element.payload_argument = value
        assert element.payload_argument == value

    def test_payload_parameter(self, element):
        """Test getter and setter for payload parameter property."""
        value = "test_value"
        element.payload_parameter = value
        assert element.payload_parameter == value

    def test_receiver_argument(self, element):
        """Test getter and setter for receiver argument property."""
        value = "test_value"
        element.receiver_argument = value
        assert element.receiver_argument == value

    def test_trigger_action(self, element):
        """Test getter for trigger action property."""
        _ = element.trigger_action
