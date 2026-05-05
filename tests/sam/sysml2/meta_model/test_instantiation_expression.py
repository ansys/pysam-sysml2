"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest


from ansys.sam.sysml2.meta_model.instantiation_expression import InstantiationExpression


class TestInstantiationExpression:
    """Test class for Java class 'com.ansys.metamodel.sysml2.InstantiationExpression'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return InstantiationExpression("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_argument(self, element):
        """Test getter for argument property."""
        _ = element.argument

    def test_instantiated_type(self, element):
        """Test getter and setter for instantiated type property."""
        value = "test_value"
        element.instantiated_type = value
        assert element.instantiated_type == value
