"""Generated  test class from metamodel."""

import pytest

from ansys.sam.sysml2.meta_model.succession_item_flow import SuccessionItemFlow


class TestSuccessionItemFlow:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.SuccessionItemFlow'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return SuccessionItemFlow("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"
