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
from ansys.sam.sysml2.meta_model.annotation import Annotation
from ansys.sam.sysml2.meta_model.attribute_usage import AttributeUsage
from ansys.sam.sysml2.meta_model.documentation import Documentation
from ansys.sam.sysml2.meta_model.feature_membership import FeatureMembership
from ansys.sam.sysml2.meta_model.membership import Membership
from ansys.sam.sysml2.meta_model.namespace_import import NamespaceImport
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
        assert package.owned_member == [definition]
        assert definition.owned_feature_membership == [feature_membership]
        assert definition.owned_feature == [attribute]
        assert definition.feature_membership == [feature_membership]
        assert definition.feature == [attribute]

    def test_owned_annotation_documentation_and_import(self):
        project = ProjectImpl("p1", "project")
        project._includes_derived = False

        package = Package("pkg")
        documentation = Documentation("doc")
        owning = OwningMembership("own")
        annotation = Annotation("ann")
        namespace_import = NamespaceImport("imp")

        owning.owned_member_element = documentation
        package.owned_relationship.extend([owning, annotation, namespace_import])

        project._env = {
            package.id: package,
            documentation.id: documentation,
            owning.id: owning,
            annotation.id: annotation,
            namespace_import.id: namespace_import,
        }

        fill_derived_collections(project)

        assert package.owned_element == [documentation]
        assert package.documentation == [documentation]
        assert package.owned_annotation == [annotation]
        assert package.owned_import == [namespace_import]
        assert package.owned_member == [documentation]

    def test_owned_member_ignores_plain_membership(self):
        project = ProjectImpl("p1", "project")
        project._includes_derived = False

        package = Package("pkg")
        owned = PartDefinition("owned")
        referenced = PartDefinition("ref")
        owning = OwningMembership("own")
        plain = Membership("mem")

        owning.owned_member_element = owned
        plain.member_element = referenced
        package.owned_relationship.extend([owning, plain])

        project._env = {
            package.id: package,
            owned.id: owned,
            referenced.id: referenced,
            owning.id: owning,
            plain.id: plain,
        }

        fill_derived_collections(project)

        assert package.owned_element == [owned]
        assert package.owned_member == [owned]
        assert package.owned_membership == [owning, plain]

    def test_feature_includes_inherited(self):
        project = ProjectImpl("p1", "project")
        project._includes_derived = False

        definition = PartDefinition("def")
        owned_attribute = AttributeUsage("owned")
        inherited_attribute = AttributeUsage("inherited")
        feature_via_plain_membership = AttributeUsage("via_plain")
        feature_membership = FeatureMembership("fm")
        inherited_feature_membership = FeatureMembership("ihm")
        inherited_plain_membership = Membership("im")

        feature_membership.owned_member_feature = owned_attribute
        feature_membership.owned_member_element = owned_attribute
        inherited_feature_membership.member_element = inherited_attribute
        inherited_plain_membership.member_element = feature_via_plain_membership

        definition.owned_relationship.append(feature_membership)
        definition.inherited_membership.extend(
            [inherited_feature_membership, inherited_plain_membership]
        )

        project._env = {
            definition.id: definition,
            owned_attribute.id: owned_attribute,
            inherited_attribute.id: inherited_attribute,
            feature_via_plain_membership.id: feature_via_plain_membership,
            feature_membership.id: feature_membership,
            inherited_feature_membership.id: inherited_feature_membership,
            inherited_plain_membership.id: inherited_plain_membership,
        }

        fill_derived_collections(project)

        assert definition.owned_feature == [owned_attribute]
        assert definition.inherited_feature == [inherited_attribute]
        assert definition.feature == [owned_attribute, inherited_attribute]
        assert definition.feature_membership == [
            feature_membership,
            inherited_feature_membership,
        ]

    def test_noop_when_includes_derived_true(self):
        project = ProjectImpl("p1", "project")
        project._includes_derived = True
        package = Package("pkg")
        package.owned_element.append(Package("child"))
        project._env = {package.id: package}

        fill_derived_collections(project)

        assert len(package.owned_element) == 1


class TestFillDerivedCollectionsScripting:

    def test_owned_element_and_owned_member_from_owning_membership(self):
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
        assert package._ownedMembership == [owning]
        assert package._ownedMember == [child]


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
        assert root._ownedMember
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
        assert root.owned_member
