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

"""E2E tests for query execution against a real SAM product instance."""

import pytest

from ansys.sam.sysml2.dto.query.constraints_classes import (
    CompositeConstraint,
    PrimitiveConstraint,
)
from ansys.sam.sysml2.dto.query.query_class import Query
from ansys.sam.sysml2.dto.query.query_enum import JoinOperator
from ansys.sam.sysml2.exception.connector_exception import BadRequestConnectionException
from ansys.sam.sysml2.exception.query_exception import InvalidQuery

from .conftest import load_scripting_project, load_sysml_project


@pytest.mark.e2e
class TestQueriesScripting:

    def test_query_primitive_constraint_by_id(self, connector, project_manager):
        """Query with PrimitiveConstraint on @id returns exactly one matching element."""
        project = load_scripting_project(connector, project_manager, "bike")
        elements = connector.get_all_elements(project._id)
        target_id = elements[0]["@id"]

        query = Query()
        query.where = PrimitiveConstraint("@id", target_id)
        result = connector.execute_query(project._id, query.to_json())

        assert len(result) == 1
        assert result[0]["@id"] == target_id

        connector.delete_project(project._id)

    def test_query_composite_or(self, connector, project_manager):
        """Composite OR constraint returns elements matching either condition."""
        project = load_scripting_project(connector, project_manager, "bike")
        elements = connector.get_all_elements(project._id)
        id_a = elements[0]["@id"]
        id_b = elements[1]["@id"]

        query = Query()
        cc = CompositeConstraint(operator=JoinOperator.OR)
        cc.constraint = [
            PrimitiveConstraint("@id", id_a),
            PrimitiveConstraint("@id", id_b),
        ]
        query.where = cc
        result = connector.execute_query(project._id, query.to_json())

        assert len(result) == 2
        result_ids = {r["@id"] for r in result}
        assert id_a in result_ids
        assert id_b in result_ids

        connector.delete_project(project._id)

    def test_query_invalid_property(self, connector, project_manager):
        """Query on non-existent property raises BadRequestConnectionException."""
        project = load_scripting_project(connector, project_manager, "bike")

        query = Query()
        query.where = PrimitiveConstraint("nonExistentProperty", "value")

        with pytest.raises(BadRequestConnectionException):
            connector.execute_query(project._id, query.to_json())

        connector.delete_project(project._id)

    def test_query_invalid_composite_constraint(self):
        """Composite constraint with fewer than 2 children raises InvalidQuery client-side."""
        pc = PrimitiveConstraint("@id", "some-id")
        cc = CompositeConstraint(operator=JoinOperator.OR)
        cc.constraint = [pc]

        query = Query()
        query.where = cc

        with pytest.raises((InvalidQuery, Exception)):
            query.to_json()


@pytest.mark.e2e
class TestQueriesSysML:

    def test_query_primitive_constraint_by_id(self, connector, project_manager):
        """Query with PrimitiveConstraint on @id via sysml project."""
        project = load_sysml_project(connector, project_manager, "bike")
        elements = connector.get_all_elements(project._id)
        target_id = elements[0]["@id"]

        query = Query()
        query.where = PrimitiveConstraint("@id", target_id)
        result = connector.execute_query(project._id, query.to_json())

        assert len(result) == 1
        assert result[0]["@id"] == target_id

        connector.delete_project(project._id)

    def test_query_composite_or_sysml(self, connector, project_manager):
        """Composite OR constraint via sysml project."""
        project = load_sysml_project(connector, project_manager, "bike")
        elements = connector.get_all_elements(project._id)
        id_a = elements[0]["@id"]
        id_b = elements[1]["@id"]

        query = Query()
        cc = CompositeConstraint(operator=JoinOperator.OR)
        cc.constraint = [
            PrimitiveConstraint("@id", id_a),
            PrimitiveConstraint("@id", id_b),
        ]
        query.where = cc
        result = connector.execute_query(project._id, query.to_json())

        assert len(result) == 2
        result_ids = {r["@id"] for r in result}
        assert id_a in result_ids
        assert id_b in result_ids

        connector.delete_project(project._id)
