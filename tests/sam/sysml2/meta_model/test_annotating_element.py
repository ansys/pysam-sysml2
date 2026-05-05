"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest


from ansys.sam.sysml2.meta_model.annotating_element import AnnotatingElement


class TestAnnotatingElement:
    """Test class for Java class 'com.ansys.metamodel.sysml2.AnnotatingElement'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return AnnotatingElement("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_annotated_element(self, element):
        """Test getter for annotated element property."""
        _ = element.annotated_element

    def test_annotation(self, element):
        """Test getter for annotation property."""
        _ = element.annotation

    def test_owned_annotating_relationship(self, element):
        """Test getter for owned annotating relationship property."""
        _ = element.owned_annotating_relationship

    def test_owning_annotating_relationship(self, element):
        """Test getter and setter for owning annotating relationship property."""
        value = "test_value"
        element.owning_annotating_relationship = value
        assert element.owning_annotating_relationship == value
