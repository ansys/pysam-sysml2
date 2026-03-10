"""Generated  test class from metamodel."""

import pytest

from ansys.sam.sysml2.meta_model.return_parameter_membership import ReturnParameterMembership


class TestReturnParameterMembership:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.ReturnParameterMembership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ReturnParameterMembership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"
