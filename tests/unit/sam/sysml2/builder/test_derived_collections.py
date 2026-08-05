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

"""Unit tests for client-side derived collection filling."""

from ansys.sam.sysml2.builder.classes.project_impl import ProjectImpl
from ansys.sam.sysml2.builder.classes.scripting_project_impl import ScriptingProjectImpl
from ansys.sam.sysml2.builder.derived_collections import fill_derived_collections
from ansys.sam.sysml2.builder.sysml2_project_builder import SysML2ProjectBuilder
from ansys.sam.sysml2.classes.sysml_element import SysMLElement
from ansys.sam.sysml2.meta_model.attribute_usage import AttributeUsage
from ansys.sam.sysml2.meta_model.feature_membership import FeatureMembership
from ansys.sam.sysml2.meta_model.owning_membership import OwningMembership
from ansys.sam.sysml2.meta_model.package import Package
from ansys.sam.sysml2.meta_model.part_definition import PartDefinition
from tests.unit.const import PROJECT_ID_1


class TestFillDerivedCollectionsSysML:

    def test_owned_element_and_owned_feature_from_relationships(self):
        project = ProjectImpl("p1", "project")
        project._includes_derived = False

        package = Package("pkg")
        definition = PartDefinition("def")
        attribute = AttributeUsage("attr")
        owning = OwningMembership("own")
        feature_membership = FeatureMembership("fm")

        owning.owned_member_element = definition
        feature_membership.owned_member_element = attribute
        feature_membership.owned_member_feature = attribute

        package.owned_relationship.append(owning)
        definition.owned_relationship.append(feature_membership)

        project._env = {
            package.id: package,
            definition.id: definition,
            attribute.id: attribute,
            owning.id: owning,
            feature_membership.id: feature_membership,
        }

        fill_derived_collections(project)

        assert package.owned_element == [definition]
        assert package.owned_membership == [owning]
        assert definition.owned_feature_membership == [feature_membership]
        assert definition.owned_feature == [attribute]

    def test_noop_when_includes_derived_true(self):
        project = ProjectImpl("p1", "project")
        project._includes_derived = True
        package = Package("pkg")
        package.owned_element.append(Package("child"))
        project._env = {package.id: package}

        fill_derived_collections(project)

        assert len(package.owned_element) == 1


class TestFillDerivedCollectionsScripting:

    def test_owned_element_from_owning_membership(self):
        project = ScriptingProjectImpl("p1", "project")
        project._includes_derived = False

        package = SysMLElement("pkg")
        package.__class__ = type("Package", (SysMLElement,), {})
        child = SysMLElement("child")
        child.__class__ = type("PartDefinition", (SysMLElement,), {})
        owning = SysMLElement("own")
        owning.__class__ = type("OwningMembership", (SysMLElement,), {})
        owning._ownedMemberElement = child
        package._ownedRelationship = [owning]

        project._env = {
            package._id: package,
            child._id: child,
            owning._id: owning,
        }

        fill_derived_collections(project)

        assert package._ownedElement == [child]


class TestSysML2ProjectBuilderDerivedCollections:

    def test_build_scripting_project_without_derived_fills_owned_element(self, connector):
        builder = SysML2ProjectBuilder(connector)

        project = builder.build_scripting_project(
            PROJECT_ID_1,
            includes_derived=False,
            includes_inherited=False,
        )

        root = project.get_root_package()
        assert root._ownedElement
        assert all(isinstance(child, SysMLElement) for child in root._ownedElement)

    def test_build_sysml_project_without_derived_fills_owned_element(self, connector):
        builder = SysML2ProjectBuilder(connector)

        project = builder.build_sysml_project(
            PROJECT_ID_1,
            includes_derived=False,
            includes_inherited=False,
        )

        root = project.get_root_package()
        assert root.owned_element
