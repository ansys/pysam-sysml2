"""Generated  test class from metamodel."""

import pytest

from ansys.sam.sysml2.meta_model.concern_usage import ConcernUsage


class TestConcernUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.ConcernUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ConcernUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"
