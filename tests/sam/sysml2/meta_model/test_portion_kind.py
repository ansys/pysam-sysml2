"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.portion_kind import PortionKind


class TestPortionKind:
    """Test class for Java class 'com.ansys.metamodel.sysml2.PortionKind'."""

    @pytest.fixture
    def element(self):
        """Create test element."""
        return PortionKind()

    def test_by_name(self, element):
        """Test getter for by name property."""
        _ = element.by_name

    def test_literal(self, element):
        """Test getter for literal property."""
        _ = element.literal

    def test_name(self, element):
        """Test getter for name property."""
        _ = element.name

    def test_value(self, element):
        """Test getter for value property."""
        _ = element.value
