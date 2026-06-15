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

from ansys.sam.sysml2.meta_model.membership import Membership


class TestMembership:
    """Test class for Java class 'com.ansys.metamodel.sysml2.Membership'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Membership("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_member_element(self, element):
        """Test getter and setter for member element property."""
        value = "test_value"
        element.member_element = value
        assert element.member_element == value

    def test_member_element_id(self, element):
        """Test getter and setter for member element id property."""
        value = ""
        element.member_element_id = value
        assert element.member_element_id == value

    def test_member_name(self, element):
        """Test getter and setter for member name property."""
        value = ""
        element.member_name = value
        assert element.member_name == value

    def test_member_short_name(self, element):
        """Test getter and setter for member short name property."""
        value = ""
        element.member_short_name = value
        assert element.member_short_name == value

    def test_membership_owning_namespace(self, element):
        """Test getter and setter for membership owning namespace property."""
        value = "test_value"
        element.membership_owning_namespace = value
        assert element.membership_owning_namespace == value

    def test_visibility(self, element):
        """Test getter and setter for visibility property."""
        value = "test_value"
        element.visibility = value
        assert element.visibility == value

    def test_distinguishable_from(self, element):
        """Test getter for distinguishable from property."""
        _ = element.distinguishable_from
