"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.subclassification import Subclassification


class TestSubclassification:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.Subclassification'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Subclassification("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_subclassifier(self, element):
        """Test getter and setter for subclassifier property."""
        value = None
        element.subclassifier = value
        assert element.subclassifier == value

    def test_superclassifier(self, element):
        """Test getter and setter for superclassifier property."""
        value = None
        element.superclassifier = value
        assert element.superclassifier == value

    def test_owning_classifier(self, element):
        """Test getter and setter for owning classifier property."""
        value = "test_value"
        element.owning_classifier = value
        assert element.owning_classifier == value
