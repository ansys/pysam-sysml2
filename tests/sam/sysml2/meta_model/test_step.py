"""Generated  test class from metamodel."""

import pytest


from ansys.sam.sysml2.meta_model.step import Step


class TestStep:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Step'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Step("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_behavior(self, element):
        """Test getter for behavior property."""
        _ = element.behavior

    def test_parameter(self, element):
        """Test getter for parameter property."""
        _ = element.parameter
