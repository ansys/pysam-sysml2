"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.requirement_verification_membership import RequirementVerificationMembership


class TestRequirementVerificationMembership:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.RequirementVerificationMembership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return RequirementVerificationMembership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_verified_requirement(self, element):
        """Test getter and setter for verified requirement property."""
        value = None
        element.verified_requirement = value
        assert element.verified_requirement == value
