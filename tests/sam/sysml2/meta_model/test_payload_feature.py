"""Generated  test class from metamodel."""

import pytest

from ansys.sam.sysml2.meta_model.payload_feature import PayloadFeature


class TestPayloadFeature:
    """Test class for Java class 'com.ansys.metamodel.sysml2.PayloadFeature'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return PayloadFeature("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"
