"""Generated  test class from metamodel."""

import pytest

from ansys.sam.sysml2.meta_model.predicate import Predicate


class TestPredicate:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.Predicate'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Predicate("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"
