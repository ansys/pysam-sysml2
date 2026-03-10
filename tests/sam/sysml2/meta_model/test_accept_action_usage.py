"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.accept_action_usage import AcceptActionUsage


class TestAcceptActionUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.AcceptActionUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return AcceptActionUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_payload_argument(self, element):
        """Test getter for payload argument property."""
        _ = element.payload_argument

    def test_receiver_argument(self, element):
        """Test getter for receiver argument property."""
        _ = element.receiver_argument

    def test_payload_parameter(self, element):
        """Test getter for payload parameter property."""
        _ = element.payload_parameter
