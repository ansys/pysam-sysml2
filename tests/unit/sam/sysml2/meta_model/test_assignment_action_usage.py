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

from ansys.sam.sysml2.meta_model.assignment_action_usage import AssignmentActionUsage


class TestAssignmentActionUsage:
    """Test class for Java class 'com.ansys.metamodel.sysml2.AssignmentActionUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return AssignmentActionUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_referent(self, element):
        """Test getter and setter for referent property."""
        value = "test_value"
        element.referent = value
        assert element.referent == value

    def test_target_argument(self, element):
        """Test getter and setter for target argument property."""
        value = "test_value"
        element.target_argument = value
        assert element.target_argument == value

    def test_value_expression(self, element):
        """Test getter and setter for value expression property."""
        value = "test_value"
        element.value_expression = value
        assert element.value_expression == value
