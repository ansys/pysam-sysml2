"""Generated  test class from metamodel."""

import pytest

from ansys.sam.sysml2.meta_model.association_structure import AssociationStructure


class TestAssociationStructure:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.AssociationStructure'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return AssociationStructure("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"
