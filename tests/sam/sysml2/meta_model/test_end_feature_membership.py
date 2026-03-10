"""Generated  test class from metamodel."""

import pytest

from ansys.sam.sysml2.meta_model.end_feature_membership import EndFeatureMembership


class TestEndFeatureMembership:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.EndFeatureMembership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return EndFeatureMembership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"
