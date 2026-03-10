"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.interface_usage import InterfaceUsage


class TestInterfaceUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.InterfaceUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return InterfaceUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_interface_definition(self, element):
        """Test getter and setter for interface definition property."""
        value = None
        element.interface_definition = value
        assert element.interface_definition == value
