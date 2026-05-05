"""Generated  test class from metamodel."""

import pytest

from ansys.sam.sysml2.meta_model.literal_infinity import LiteralInfinity


class TestLiteralInfinity:
    """Test class for Java class 'com.ansys.metamodel.sysml2.LiteralInfinity'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return LiteralInfinity("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"
