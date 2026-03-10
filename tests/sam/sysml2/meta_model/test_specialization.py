"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.specialization import Specialization


class TestSpecialization:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.Specialization'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Specialization("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_owning_type(self, element):
        """Test getter and setter for owning type property."""
        value = "test_value"
        element.owning_type = value
        assert element.owning_type == value

    def test_specific(self, element):
        """Test getter and setter for specific property."""
        value = None
        element.specific = value
        assert element.specific == value

    def test_general(self, element):
        """Test getter and setter for general property."""
        value = None
        element.general = value
        assert element.general == value
