"""Generated  test class from metamodel."""

import pytest

from ansys.sam.sysml2.meta_model.constraint_definition import ConstraintDefinition


class TestConstraintDefinition:
    """Test class for Java class 'com.ansys.metamodel.sysml2.ConstraintDefinition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ConstraintDefinition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"
