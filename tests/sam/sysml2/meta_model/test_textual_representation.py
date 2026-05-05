"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.textual_representation import TextualRepresentation


class TestTextualRepresentation:
    """Test class for Java class 'com.ansys.metamodel.sysml2.TextualRepresentation'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return TextualRepresentation("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_body(self, element):
        """Test getter and setter for body property."""
        value = ""
        element.body = value
        assert element.body == value

    def test_language(self, element):
        """Test getter and setter for language property."""
        value = ""
        element.language = value
        assert element.language == value

    def test_represented_element(self, element):
        """Test getter and setter for represented element property."""
        value = "test_value"
        element.represented_element = value
        assert element.represented_element == value
