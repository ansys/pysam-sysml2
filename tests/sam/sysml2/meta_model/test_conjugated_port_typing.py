"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.conjugated_port_typing import ConjugatedPortTyping


class TestConjugatedPortTyping:
    """Test class for Java class 'com.ansys.metamodel.sysml2.ConjugatedPortTyping'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ConjugatedPortTyping("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_conjugated_port_definition(self, element):
        """Test getter and setter for conjugated port definition property."""
        value = "test_value"
        element.conjugated_port_definition = value
        assert element.conjugated_port_definition == value
