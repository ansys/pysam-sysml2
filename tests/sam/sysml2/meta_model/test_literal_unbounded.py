"""Generated  test class from metamodel."""

import pytest

from ansys.sam.sysml2.meta_model.literal_unbounded import LiteralUnbounded


class TestLiteralUnbounded:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.LiteralUnbounded'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return LiteralUnbounded("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"
