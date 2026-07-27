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

"""Unit tests for SysMLTools helpers."""

import pytest

from ansys.sam.sysml2.classes.sysml_element import SysMLElement
from ansys.sam.sysml2.meta_model.element import Element
from ansys.sam.sysml2.meta_model.feature import Feature
from ansys.sam.sysml2.meta_model.feature_membership import FeatureMembership
from ansys.sam.sysml2.meta_model.owning_membership import OwningMembership
from ansys.sam.sysml2.meta_model.visibility_kind import VisibilityKind
from ansys.sam.sysml2.tools.sysmltools import SysMLTools


class TestGetElementVisibility:
    """Visibility is read from the element's owning membership, for both flavors."""

    def test_metamodel_reads_owning_membership_visibility(self):
        element = Element("element_id")
        membership = OwningMembership("membership_id")
        membership.visibility = VisibilityKind.PUBLIC
        element.owning_membership = membership

        assert SysMLTools.get_element_visibility(element) == VisibilityKind.PUBLIC

    def test_metamodel_falls_back_to_owning_feature_membership(self):
        feature = Feature("feature_id")
        membership = FeatureMembership("membership_id")
        membership.visibility = VisibilityKind.PUBLIC
        feature.owning_feature_membership = membership

        assert SysMLTools.get_element_visibility(feature) == VisibilityKind.PUBLIC

    def test_metamodel_without_owning_membership_returns_none(self):
        element = Element("element_id")

        assert SysMLTools.get_element_visibility(element) is None

    def test_scripting_reads_owning_membership_visibility(self):
        element = SysMLElement("element_id")
        membership = SysMLElement("membership_id")
        object.__setattr__(membership, "_visibility", VisibilityKind.PRIVATE)
        element._owningMembership = membership

        assert SysMLTools.get_element_visibility(element) == VisibilityKind.PRIVATE

    def test_scripting_falls_back_to_owning_feature_membership(self):
        element = SysMLElement("element_id")
        membership = SysMLElement("membership_id")
        object.__setattr__(membership, "_visibility", VisibilityKind.PUBLIC)
        element._owningFeatureMembership = membership

        assert SysMLTools.get_element_visibility(element) == VisibilityKind.PUBLIC

    def test_scripting_without_owning_membership_returns_none(self):
        element = SysMLElement("element_id")

        assert SysMLTools.get_element_visibility(element) is None


class TestSetElementVisibility:
    """Visibility is written on the element's owning membership, for both flavors."""

    def test_metamodel_sets_owning_membership_visibility(self):
        element = Element("element_id")
        membership = OwningMembership("membership_id")
        element.owning_membership = membership

        SysMLTools.set_element_visibility(element, VisibilityKind.PUBLIC)

        assert membership.visibility == VisibilityKind.PUBLIC

    def test_metamodel_sets_owning_feature_membership_visibility(self):
        feature = Feature("feature_id")
        membership = FeatureMembership("membership_id")
        feature.owning_feature_membership = membership

        SysMLTools.set_element_visibility(feature, VisibilityKind.PRIVATE)

        assert membership.visibility == VisibilityKind.PRIVATE

    def test_scripting_sets_owning_membership_visibility(self):
        element = SysMLElement("element_id")
        membership = SysMLElement("membership_id")
        element._owningMembership = membership

        SysMLTools.set_element_visibility(element, VisibilityKind.PROTECTED)

        assert membership._visibility == VisibilityKind.PROTECTED

    def test_scripting_sets_owning_feature_membership_visibility(self):
        element = SysMLElement("element_id")
        membership = SysMLElement("membership_id")
        element._owningFeatureMembership = membership

        SysMLTools.set_element_visibility(element, VisibilityKind.PUBLIC)

        assert membership._visibility == VisibilityKind.PUBLIC

    def test_without_owning_membership_raises(self):
        element = Element("element_id")

        with pytest.raises(AttributeError, match="owning membership"):
            SysMLTools.set_element_visibility(element, VisibilityKind.PUBLIC)
