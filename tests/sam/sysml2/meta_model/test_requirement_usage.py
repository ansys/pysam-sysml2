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

from ansys.sam.sysml2.meta_model.requirement_usage import RequirementUsage


class TestRequirementUsage:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.RequirementUsage'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return RequirementUsage("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_text(self, element):
        """Test getter for text property."""
        _ = element.text

    def test_actor_parameter(self, element):
        """Test getter for actor parameter property."""
        _ = element.actor_parameter

    def test_framed_concern(self, element):
        """Test getter for framed concern property."""
        _ = element.framed_concern

    def test_is_objective(self, element):
        """Test getter and setter for is objective property."""
        value = False
        element.is_objective = value
        assert element.is_objective == value

    def test_all_text(self, element):
        """Test getter for all text property."""
        _ = element.all_text

    def test_req_id(self, element):
        """Test getter and setter for req id property."""
        value = ""
        element.req_id = value
        assert element.req_id == value

    def test_assumed_constraint(self, element):
        """Test getter for assumed constraint property."""
        _ = element.assumed_constraint

    def test_required_constraint(self, element):
        """Test getter for required constraint property."""
        _ = element.required_constraint

    def test_subject_parameter(self, element):
        """Test getter and setter for subject parameter property."""
        value = "test_value"
        element.subject_parameter = value
        assert element.subject_parameter == value

    def test_stakeholder_parameter(self, element):
        """Test getter for stakeholder parameter property."""
        _ = element.stakeholder_parameter

    def test_a_verify_requirement(self, element):
        """Test getter for a verify requirement property."""
        _ = element.a_verify_requirement

    def test_requirement_definition(self, element):
        """Test getter and setter for requirement definition property."""
        value = "test_value"
        element.requirement_definition = value
        assert element.requirement_definition == value
