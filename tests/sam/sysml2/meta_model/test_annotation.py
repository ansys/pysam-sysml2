"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.annotation import Annotation


class TestAnnotation:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Annotation'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Annotation("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_annotated_element(self, element):
        """Test getter and setter for annotated element property."""
        value = "test_value"
        element.annotated_element = value
        assert element.annotated_element == value

    def test_annotating_element(self, element):
        """Test getter and setter for annotating element property."""
        value = "test_value"
        element.annotating_element = value
        assert element.annotating_element == value

    def test_owned_annotating_element(self, element):
        """Test getter and setter for owned annotating element property."""
        value = "test_value"
        element.owned_annotating_element = value
        assert element.owned_annotating_element == value

    def test_owning_annotated_element(self, element):
        """Test getter and setter for owning annotated element property."""
        value = "test_value"
        element.owning_annotated_element = value
        assert element.owning_annotated_element == value

    def test_owning_annotating_element(self, element):
        """Test getter and setter for owning annotating element property."""
        value = "test_value"
        element.owning_annotating_element = value
        assert element.owning_annotating_element == value
