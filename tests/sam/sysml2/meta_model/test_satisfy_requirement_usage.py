"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.satisfy_requirement_usage import SatisfyRequirementUsage


class TestSatisfyRequirementUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.SatisfyRequirementUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return SatisfyRequirementUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_satisfied_requirement(self, element):
        """Test getter and setter for satisfied requirement property."""
        value = "test_value"
        element.satisfied_requirement = value
        assert element.satisfied_requirement == value

    def test_satisfying_feature(self, element):
        """Test getter and setter for satisfying feature property."""
        value = "test_value"
        element.satisfying_feature = value
        assert element.satisfying_feature == value
