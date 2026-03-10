"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.verification_case_usage import VerificationCaseUsage


class TestVerificationCaseUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.VerificationCaseUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return VerificationCaseUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_verification_case_definition(self, element):
        """Test getter and setter for verification case definition property."""
        value = "test_value"
        element.verification_case_definition = value
        assert element.verification_case_definition == value

    def test_verified_requirement(self, element):
        """Test getter for verified requirement property."""
        _ = element.verified_requirement
