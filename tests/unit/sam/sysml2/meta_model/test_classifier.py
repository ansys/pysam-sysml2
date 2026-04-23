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


import pytest

from ansys.sam.sysml2.meta_model.classifier import Classifier


class TestClassifier:
    """Test class for Java class 'com.ansys.medini.metamodel.sysml.Classifier'."""

    @pytest.fixture
    def element(self):
        """Create test element with ID."""
        return Classifier("element_id")

    def test_id_set(self, element):
        """Test element ID is correctly set."""
        assert element.id == "element_id"

    def test_super_classifier(self, element):
        """Test getter for super classifier property."""
        _ = element.super_classifier

    def test_owned_subclassification(self, element):
        """Test getter for owned subclassification property."""
        _ = element.owned_subclassification
