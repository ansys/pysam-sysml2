"""Generated  test class from metamodel."""


import pytest

from ansys.sam.sysml2.meta_model.annotating_element import AnnotatingElement


class TestAnnotatingElement:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.AnnotatingElement'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return AnnotatingElement("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_annotation(self, element):
        """Test getter for annotation property."""
        _ = element.annotation

    def test_annotated_element(self, element):
        """Test getter for annotated element property."""
        _ = element.annotated_element
