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

from ansys.sam.sysml2.meta_model.feature_value import FeatureValue


class TestFeatureValue:
    """Test class for Java class 'com.ansys.metamodel.sysml2.FeatureValue'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return FeatureValue("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_feature_with_value(self, element):
        """Test getter and setter for feature with value property."""
        value = "test_value"
        element.feature_with_value = value
        assert element.feature_with_value == value

    def test_value(self, element):
        """Test getter and setter for value property."""
        value = "test_value"
        element.value = value
        assert element.value == value

    def test_is_default(self, element):
        """Test getter and setter for is default property."""
        value = False
        element.is_default = value
        assert element.is_default == value

    def test_is_initial(self, element):
        """Test getter and setter for is initial property."""
        value = False
        element.is_initial = value
        assert element.is_initial == value
