"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.conjugation import Conjugation


class TestConjugation:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Conjugation'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Conjugation("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_conjugated_type(self, element):
        """Test getter and setter for conjugated type property."""
        value = "test_value"
        element.conjugated_type = value
        assert element.conjugated_type == value

    def test_original_type(self, element):
        """Test getter and setter for original type property."""
        value = "test_value"
        element.original_type = value
        assert element.original_type == value

    def test_owning_type(self, element):
        """Test getter and setter for owning type property."""
        value = "test_value"
        element.owning_type = value
        assert element.owning_type == value
