"""Generated  test class from metamodel."""


import pytest

from ansys.sam.sysml2.meta_model.behavior import Behavior


class TestBehavior:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.Behavior'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Behavior("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_parameter(self, element):
        """Test getter for parameter property."""
        _ = element.parameter

    def test_step(self, element):
        """Test getter for step property."""
        _ = element.step

    def test_general_parameter(self, element):
        """Test getter for general parameter property."""
        _ = element.general_parameter
