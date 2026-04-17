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

from ansys.sam.sysml2.meta_model.feature_membership import FeatureMembership


class TestFeatureMembership:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.FeatureMembership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return FeatureMembership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_owning_type(self, element):
        """Test getter and setter for owning type property."""
        value = "test_value"
        element.owning_type = value
        assert element.owning_type == value

    def test_member_feature(self, element):
        """Test getter and setter for member feature property."""
        value = "test_value"
        element.member_feature = value
        assert element.member_feature == value

    def test_owned_member_feature(self, element):
        """Test getter and setter for owned member feature property."""
        value = "test_value"
        element.owned_member_feature = value
        assert element.owned_member_feature == value

    def test_direction(self, element):
        """Test getter and setter for direction property."""
        value = "test_value"
        element.direction = value
        assert element.direction == value

    def test_is_composite(self, element):
        """Test getter and setter for is composite property."""
        value = False
        element.is_composite = value
        assert element.is_composite == value
