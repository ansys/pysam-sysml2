"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.documentation import Documentation


class TestDocumentation:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Documentation'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Documentation("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_documented_element(self, element):
        """Test getter and setter for documented element property."""
        value = "test_value"
        element.documented_element = value
        assert element.documented_element == value
