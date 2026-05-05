"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.conjugated_port_definition import ConjugatedPortDefinition


class TestConjugatedPortDefinition:
    """Test class for Java class 'com.ansys.metamodel.sysml2.ConjugatedPortDefinition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ConjugatedPortDefinition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_original_port_definition(self, element):
        """Test getter and setter for original port definition property."""
        value = "test_value"
        element.original_port_definition = value
        assert element.original_port_definition == value

    def test_owned_port_conjugator(self, element):
        """Test getter and setter for owned port conjugator property."""
        value = "test_value"
        element.owned_port_conjugator = value
        assert element.owned_port_conjugator == value
