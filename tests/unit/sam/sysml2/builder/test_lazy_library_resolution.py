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

"""POC tests for lazy library resolution.

The lean build (``resolve_libraries=False``, the default) prefetches only the
library referents used inside feature-value expressions and resolves any other
library element on demand at ``get_value``. The eager build
(``resolve_libraries=True``) keeps fetching every referenced library element.
"""

import json

from ansys.sam.sysml2.builder.classes.scripting_project_impl import ScriptingProjectImpl
from ansys.sam.sysml2.builder.sysml2_project_builder import SysML2ProjectBuilder
from ansys.sam.sysml2.builder.sysml2_project_manager import SysML2ProjectManager
from ansys.sam.sysml2.classes.unresolved_field import UnresolvedField
from tests.unit.const import PROJECT_ID_5

# The single library unit (kilogram) referenced by project_5's expressions.
KG_ID = "bb1d79c2-1306-5b35-a807-93e46fc3431c"
# The FeatureReferenceExpression operand that points at ``kg``.
KG_REFERENCE_EXPRESSION_ID = "51A10D91-15B0-4B1E-9639-36333238DD31"


class _Owner:
    """Minimal stand-in for an element owning an unresolved field."""


class TestExpressionReferentSelection:
    """The selector keeps only referent fields, so non-referent library refs are skipped."""

    def test_collects_only_referent_fields(self, connector):
        builder = SysML2ProjectBuilder(connector)
        project = ScriptingProjectImpl("5", "p5")
        owner = _Owner()
        project._unresolved_fields = [
            UnresolvedField(owner, "_referent", "lib-referent"),
            UnresolvedField(owner, "_type", "lib-type"),
            UnresolvedField(owner, "_member", "lib-member"),
        ]
        missing = {"lib-referent", "lib-type", "lib-member"}

        referents = builder._collect_expression_referents(project, missing)

        assert referents == {"lib-referent"}


class TestLeanBuildPrefetch:
    """The default build fetches only the expression referents, not the whole library."""

    def test_lean_build_queries_only_expression_referents(self, connector, mocker):
        spy = mocker.spy(connector, "execute_query")

        project = SysML2ProjectManager(connector).get_scripting_project(PROJECT_ID_5)

        assert spy.call_count == 1
        queried_ids = connector._extract_ids(json.loads(spy.call_args.args[1]))
        assert queried_ids == {KG_ID}
        assert project.find_element_by_id(KG_ID) is not None

    def test_lean_build_leaves_non_referent_library_refs_unresolved(self, connector):
        builder = SysML2ProjectBuilder(connector)
        project = ScriptingProjectImpl(PROJECT_ID_5, "p5")
        project._resolve_libraries = False
        elements = connector.get_all_elements(project_id=PROJECT_ID_5)
        builder._map_element_in_project(project, elements)
        missing = builder._resolve_fields(project)

        referents = builder._collect_expression_referents(project, missing)

        # The package references the full library, but only the kg referent is needed.
        assert len(missing) > len(referents)
        assert referents == {KG_ID}

    def test_lean_build_renders_unit_value(self, connector):
        project = SysML2ProjectManager(connector).get_scripting_project(PROJECT_ID_5)
        package = project.get_root_package()

        assert package.get("attribute1").get_value() == "5 [kg]"


class TestEagerMode:
    """resolve_libraries=True still resolves referenced library elements."""

    def test_eager_build_renders_unit_value(self, connector):
        project = SysML2ProjectManager(connector).get_scripting_project(
            PROJECT_ID_5, resolve_libraries=True
        )
        package = project.get_root_package()

        assert package.get("attribute1").get_value() == "5 [kg]"
        assert project.find_element_by_id(KG_ID) is not None


class TestOnDemandResolution:
    """A library element not prefetched is fetched and mapped into the env on access."""

    def test_resolve_element_on_demand_adds_to_env(self, connector):
        builder = SysML2ProjectBuilder(connector)
        project = SysML2ProjectManager(connector).get_scripting_project(PROJECT_ID_5)
        project._env.pop(KG_ID, None)
        before = len(project._env)

        resolved = builder.resolve_element_on_demand(project, KG_ID)

        assert resolved is not None
        assert project.find_element_by_id(KG_ID) is resolved
        assert len(project._env) == before + 1

    def test_resolve_element_on_demand_returns_cached_when_present(self, connector):
        builder = SysML2ProjectBuilder(connector)
        project = SysML2ProjectManager(connector).get_scripting_project(PROJECT_ID_5)

        cached = project.find_element_by_id(KG_ID)

        assert builder.resolve_element_on_demand(project, KG_ID) is cached

    def test_get_value_resolves_unresolved_referent_on_demand(self, connector, mocker):
        project = SysML2ProjectManager(connector).get_scripting_project(PROJECT_ID_5)
        package = project.get_root_package()
        attribute1 = package.get("attribute1")
        reference_expression = project.find_element_by_id(KG_REFERENCE_EXPRESSION_ID)
        # Simulate a referent that was never prefetched: raw id plus a missing env entry.
        object.__setattr__(reference_expression, "_referent", KG_ID)
        project._env.pop(KG_ID, None)
        spy = mocker.spy(connector, "get_element_by_id")

        value = attribute1.get_value()

        assert value == "5 [kg]"
        assert spy.called
        assert project.find_element_by_id(KG_ID) is not None
