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

"""Tests for the metamodel-change deprecation shims (visibility redirect, read-only name)."""

import warnings

import pytest

from ansys.sam.sysml2.classes.sysml_element import SysMLElement
from ansys.sam.sysml2.meta_model.element import Element
from ansys.sam.sysml2.meta_model.owning_membership import OwningMembership


class TestMetamodelDeprecationShims:
    """Metamodel flavor: Element.visibility redirect and read-only name."""

    def test_visibility_redirects_to_owning_membership_with_warning(self):
        element = Element("element_id")
        membership = OwningMembership("membership_id")
        membership.visibility = "public"
        element.owning_membership = membership

        with pytest.warns(DeprecationWarning, match="owning_membership.visibility"):
            assert element.visibility == "public"

    def test_visibility_without_owning_membership_returns_none(self):
        element = Element("element_id")

        with pytest.warns(DeprecationWarning):
            assert element.visibility is None

    def test_setting_visibility_redirects_to_owning_membership_with_warning(self):
        element = Element("element_id")
        membership = OwningMembership("membership_id")
        element.owning_membership = membership

        with pytest.warns(DeprecationWarning, match="owning_membership.visibility"):
            element.visibility = "private"

        assert membership.visibility == "private"

    def test_setting_name_raises_pointing_to_declared_name(self):
        element = Element("element_id")

        with pytest.raises(AttributeError, match="declared_name"):
            element.name = "RenamedPart"

    def test_membership_keeps_its_own_visibility_without_warning(self):
        membership = OwningMembership("membership_id")
        membership.visibility = "private"

        with warnings.catch_warnings():
            warnings.simplefilter("error", DeprecationWarning)
            assert membership.visibility == "private"

    def test_visibility_listed_in_dir_when_owning_membership_set(self):
        element = Element("element_id")
        element.owning_membership = OwningMembership("membership_id")

        assert "visibility" in dir(element)

    def test_visibility_hidden_in_dir_on_bare_element(self):
        element = Element("element_id")

        assert "visibility" not in dir(element)

    def test_membership_always_lists_its_own_visibility_in_dir(self):
        membership = OwningMembership("membership_id")

        assert "visibility" in dir(membership)


class TestScriptingDeprecationShims:
    """Scripting flavor: SysMLElement._visibility redirect and read-only name."""

    def test_own_visibility_returned_without_warning(self):
        element = SysMLElement("element_id")
        object.__setattr__(element, "_visibility", "public")

        with warnings.catch_warnings():
            warnings.simplefilter("error", DeprecationWarning)
            assert element._visibility == "public"

    def test_visibility_redirects_to_owning_membership_with_warning(self):
        element = SysMLElement("element_id")
        membership = SysMLElement("membership_id")
        object.__setattr__(membership, "_visibility", "private")
        element._owningMembership = membership

        with pytest.warns(DeprecationWarning, match="_owningMembership._visibility"):
            assert element._visibility == "private"

    def test_visibility_without_owning_membership_returns_none(self):
        element = SysMLElement("element_id")

        assert element._visibility is None

    def test_setting_visibility_redirects_to_owning_membership_with_warning(self):
        element = SysMLElement("element_id")
        membership = SysMLElement("membership_id")
        element._owningMembership = membership

        with pytest.warns(DeprecationWarning, match="_owningMembership._visibility"):
            element._visibility = "private"

        assert membership.__dict__["_visibility"] == "private"

    def test_setting_name_raises_pointing_to_declared_name(self):
        element = SysMLElement("element_id")

        with pytest.raises(AttributeError, match="_declaredName"):
            element.name = "RenamedPart"

    def test_setting_underscore_name_raises_pointing_to_declared_name(self):
        element = SysMLElement("element_id")

        with pytest.raises(AttributeError, match="_declaredName"):
            element._name = "RenamedPart"

    def test_visibility_listed_in_dir_when_owning_membership_set(self):
        element = SysMLElement("element_id")
        element._owningMembership = SysMLElement("membership_id")

        assert "_visibility" in dir(element)

    def test_visibility_listed_in_dir_when_own_visibility_set(self):
        element = SysMLElement("element_id")
        object.__setattr__(element, "_visibility", "public")

        assert "_visibility" in dir(element)

    def test_visibility_hidden_in_dir_when_no_visibility(self):
        element = SysMLElement("element_id")

        assert "_visibility" not in dir(element)
