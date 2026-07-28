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

"""Unit tests for Factory using MockedConnector + mocker for error propagation."""

import json

import pytest

from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.exception.connector_exception import BadRequestConnectionException
from ansys.sam.sysml2.tools.factory import Factory
from tests.unit.const import PROJECT_ID_2

ELEMENT_TYPES = [
    ("create_attribute_usage", "AttributeUsage"),
    ("create_part_definition", "PartDefinition"),
    ("create_part_usage", "PartUsage"),
    ("create_package", "Package"),
    ("create_action_usage", "ActionUsage"),
    ("create_constraint_usage", "ConstraintUsage"),
    ("create_port_usage", "PortUsage"),
    ("create_connection_usage", "ConnectionUsage"),
    ("create_requirement_usage", "RequirementUsage"),
    ("create_state_usage", "StateUsage"),
]

# add_* method, expected element type, expected owning membership type
ADD_METHODS = [
    ("add_attribute", "AttributeUsage", "FeatureMembership"),
    ("add_actor", "PartUsage", "ActorMembership"),
    ("add_stakeholder", "PartUsage", "StakeholderMembership"),
    ("add_subject", "PartUsage", "SubjectMembership"),
    ("add_objective", "RequirementUsage", "ObjectiveMembership"),
    ("add_requirement_constraint", "ConstraintUsage", "RequirementConstraintMembership"),
    ("add_requirement_verification", "RequirementUsage", "RequirementVerificationMembership"),
    ("add_framed_concern", "ConcernUsage", "FramedConcernMembership"),
    ("add_variant", "PartUsage", "VariantMembership"),
    ("add_view_rendering", "RenderingUsage", "ViewRenderingMembership"),
    ("add_result_expression", "LiteralInteger", "ResultExpressionMembership"),
    ("add_return_parameter", "ReferenceUsage", "ReturnParameterMembership"),
]


def _owner_id(element):
    """Return the identifier of an element regardless of the (scripting/sysml) flavor."""
    return getattr(element, "_id", None) or element.id


def _changes_by_type(commit_spy):
    """Parse the single emitted commit into a mapping of element ``@type`` to its change."""
    assert commit_spy.call_count == 1
    commit = json.loads(commit_spy.call_args.args[1])
    return {change["payload"]["@type"]: change for change in commit["change"]}

class TestFactory:

    @pytest.fixture
    def project_manager(self, connector):
        return SysML2ProjectManager(connector)

    @pytest.mark.parametrize("factory_method,element_type", ELEMENT_TYPES)
    def test_create_element_transactional_scripting(
        self, project_manager, factory_method, element_type, mocker
    ):
        project = project_manager.get_scripting_project(PROJECT_ID_2)
        factory = Factory(project, project_manager._connector)
        root = project.get_root_package()
        commit_spy = mocker.spy(project_manager._connector, "create_commit")
        project.start_transactional_mode()
        create_fn = getattr(factory, factory_method)

        elem = create_fn(declared_name="test_elem", owner=root)

        assert elem.__class__.__name__ == element_type
        assert elem._declared_name == "test_elem"

        project.stop_transactional_mode()

        assert commit_spy.call_count == 1

    @pytest.mark.parametrize("factory_method,element_type", ELEMENT_TYPES)
    def test_create_element_transactional_sysml(
        self, connector, factory_method, element_type, mocker
    ):
        manager = SysML2ProjectManager(connector)
        project = manager.get_sysml_project(PROJECT_ID_2)
        factory = Factory(project, manager._connector)
        root = project.get_root_package()
        commit_spy = mocker.spy(manager._connector, "create_commit")
        project.start_transactional_mode()
        create_fn = getattr(factory, factory_method)

        elem = create_fn(declared_name="test_elem", owner=root)

        assert elem.__class__.__name__ == element_type
        assert elem.declared_name == "test_elem"

        project.stop_transactional_mode()

        assert commit_spy.call_count == 1

    def test_create_part_definition_with_owned_elements(
        self, project_manager, mocker
    ):
        project = project_manager.get_scripting_project(PROJECT_ID_2)
        factory = Factory(project, project_manager._connector)
        root = project.get_root_package()
        commit_spy = mocker.spy(project_manager._connector, "create_commit")
        project.start_transactional_mode()
        new_attr = factory.create_attribute_usage(declared_name="new_attribute", owner=root)

        new_part = factory.create_part_definition(
            declared_name="new_part_def", owner=root, owned_elements=[new_attr]
        )

        assert new_part.__class__.__name__ == "PartDefinition"
        assert new_part._declared_name == "new_part_def"
        assert len(new_part._owned_elements) == 1

        project.stop_transactional_mode()

        assert commit_spy.call_count == 1

    def test_create_element_commit_rejected(self, project_manager, mocker):
        project = project_manager.get_scripting_project(PROJECT_ID_2)
        factory = Factory(project, project_manager._connector)
        mocker.patch.object(
            project_manager._connector,
            "create_commit",
            side_effect=BadRequestConnectionException("No Type for New Element"),
        )

        with pytest.raises(BadRequestConnectionException) as exc:
            factory._create_element(element_type=None, declared_name="test")

    def test_create_element_owner_invalid(self, project_manager, mocker):
        project = project_manager.get_scripting_project(PROJECT_ID_2)
        factory = Factory(project, project_manager._connector)
        mocker.patch.object(
            project_manager._connector,
            "create_commit",
            side_effect=BadRequestConnectionException("No Valid Owner Specified"),
        )

        with pytest.raises(BadRequestConnectionException):
            factory.create_attribute_usage(declared_name="new_attribute")

    def test_create_element_with_invalid_owner_attr(self, project_manager):
        project = project_manager.get_scripting_project(PROJECT_ID_2)
        factory = Factory(project, project_manager._connector)
        root = project.get_root_package()

        with pytest.raises(AttributeError):
            factory.create_attribute_usage(
                declared_name="new_attribute", owner=root.UNDEFINED_ELEMENT
            )

    @pytest.mark.parametrize("factory_method,element_type,membership_type", ADD_METHODS)
    def test_add_element_with_membership_scripting(
        self, project_manager, factory_method, element_type, membership_type, mocker
    ):
        project = project_manager.get_scripting_project(PROJECT_ID_2)
        factory = Factory(project, project_manager._connector)
        root = project.get_root_package()
        commit_spy = mocker.spy(project_manager._connector, "create_commit")

        element = getattr(factory, factory_method)(declared_name="test_elem", owner=root)

        assert element.__class__.__name__ == element_type

        changes = _changes_by_type(commit_spy)
        element_change = changes[element_type]
        membership_change = changes[membership_type]
        element_id = element_change["identity"]["@id"]
        assert element_change["payload"]["declaredName"] == "test_elem"
        assert element_change["payload"]["owner"] == {"@id": _owner_id(root)}
        assert membership_change["payload"]["owner"] == {"@id": _owner_id(root)}
        assert membership_change["payload"]["ownedRelatedElement"] == [{"@id": element_id}]

    @pytest.mark.parametrize("factory_method,element_type,membership_type", ADD_METHODS)
    def test_add_element_with_membership_sysml(
        self, connector, factory_method, element_type, membership_type, mocker
    ):
        manager = SysML2ProjectManager(connector)
        project = manager.get_sysml_project(PROJECT_ID_2)
        factory = Factory(project, manager._connector)
        root = project.get_root_package()
        commit_spy = mocker.spy(manager._connector, "create_commit")

        element = getattr(factory, factory_method)(declared_name="test_elem", owner=root)

        assert element.__class__.__name__ == element_type

        changes = _changes_by_type(commit_spy)
        element_change = changes[element_type]
        element_id = element_change["identity"]["@id"]
        assert element_change["payload"]["declaredName"] == "test_elem"
        assert changes[membership_type]["payload"]["ownedRelatedElement"] == [{"@id": element_id}]

    def test_add_element_with_membership_type_override(self, project_manager, mocker):
        project = project_manager.get_scripting_project(PROJECT_ID_2)
        factory = Factory(project, project_manager._connector)
        root = project.get_root_package()
        commit_spy = mocker.spy(project_manager._connector, "create_commit")

        element = factory.add_attribute(
            declared_name="test_elem", owner=root, element_type="ReferenceUsage"
        )

        assert element.__class__.__name__ == "ReferenceUsage"
        changes = _changes_by_type(commit_spy)
        assert "ReferenceUsage" in changes
        assert "FeatureMembership" in changes

    def test_add_element_with_membership_joins_open_transaction(self, project_manager, mocker):
        project = project_manager.get_scripting_project(PROJECT_ID_2)
        factory = Factory(project, project_manager._connector)
        root = project.get_root_package()
        commit_spy = mocker.spy(project_manager._connector, "create_commit")

        project.start_transactional_mode()
        factory.add_actor(declared_name="test_elem", owner=root)

        assert commit_spy.call_count == 0

        project.stop_transactional_mode()

        assert commit_spy.call_count == 1
