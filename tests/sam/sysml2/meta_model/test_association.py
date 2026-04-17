# Copyright (C) 2024 - 2026 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Generated  test class from metamodel."""

from __future__ import annotations

import pytest

from ansys.sam.sysml2.meta_model.association import Association


class TestAssociation:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.Association'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Association("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_source_type(self, element):
        """Test getter and setter for source type property."""
        value = "test_value"
        element.source_type = value
        assert element.source_type == value

    def test_related_type(self, element):
        """Test getter for related type property."""
        _ = element.related_type

    def test_association_end(self, element):
        """Test getter for association end property."""
        _ = element.association_end

    def test_target_type(self, element):
        """Test getter for target type property."""
        _ = element.target_type
