"""Generated  test class from metamodel."""


import pytest

from ansys.sam.sysml2.meta_model.verification_case_definition import VerificationCaseDefinition


class TestVerificationCaseDefinition:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.VerificationCaseDefinition'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return VerificationCaseDefinition("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_verified_requirement(self, element):
        """Test getter for verified requirement property."""
        _ = element.verified_requirement
