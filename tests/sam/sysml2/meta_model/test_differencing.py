"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.differencing import Differencing


class TestDifferencing:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Differencing'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Differencing("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_differencing_type(self, element):
        """Test getter and setter for differencing type property."""
        value = "test_value"
        element.differencing_type = value
        assert element.differencing_type == value

    def test_type_differenced(self, element):
        """Test getter and setter for type differenced property."""
        value = "test_value"
        element.type_differenced = value
        assert element.type_differenced == value
