"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.parameter_membership import ParameterMembership


class TestParameterMembership:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.ParameterMembership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return ParameterMembership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_owned_member_parameter(self, element):
        """Test getter and setter for owned member parameter property."""
        value = "test_value"
        element.owned_member_parameter = value
        assert element.owned_member_parameter == value

    def test_member_parameter(self, element):
        """Test getter and setter for member parameter property."""
        value = None
        element.member_parameter = value
        assert element.member_parameter == value
