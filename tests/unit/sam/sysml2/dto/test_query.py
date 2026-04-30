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

"""Pure unit tests for Query, PrimitiveConstraint, and CompositeConstraint serialization."""

import json

import pytest

from ansys.sam.sysml2.dto.query.constraints_classes import (
    CompositeConstraint,
    PrimitiveConstraint,
)
from ansys.sam.sysml2.dto.query.query_class import Query
from ansys.sam.sysml2.dto.query.query_enum import JoinOperator, Operator
from ansys.sam.sysml2.exception.query_exception import InvalidCompositeConstraint


class TestPrimitiveConstraint:

    def test_primitive_constraint_structure(self):
        pc = PrimitiveConstraint(property_name="@id", value="elem-1")
        result = pc.to_json()
        assert result["@type"] == "PrimitiveConstraint"
        assert result["property"] == "@id"
        assert result["value"] == "elem-1"
        assert result["operator"] == Operator.EQUALS
        assert result["inverse"] is False

    def test_inverse_serializes_as_boolean(self):
        pc = PrimitiveConstraint(
            property_name="@type", value="PartUsage", inverse=False
        )
        result = pc.to_json()
        assert result["inverse"] is False
        assert not isinstance(result["inverse"], str)

    def test_primitive_with_operator(self):
        pc = PrimitiveConstraint(
            property_name="count", value="5", operator=Operator.UPPER
        )
        result = pc.to_json()
        assert result["operator"] == ">"


class TestCompositeConstraint:

    def test_composite_constraint_structure(self):
        pc1 = PrimitiveConstraint("@id", "a")
        pc2 = PrimitiveConstraint("@id", "b")
        cc = CompositeConstraint(operator=JoinOperator.OR)
        cc.constraint = [pc1, pc2]
        result = cc.to_json()
        assert result["@type"] == "CompositeConstraint"
        assert result["operator"] == "or"
        assert len(result["constraint"]) == 2
        assert result["constraint"][0]["@type"] == "PrimitiveConstraint"

    def test_composite_constraint_fewer_than_two(self):
        pc1 = PrimitiveConstraint("@id", "a")
        cc = CompositeConstraint(operator=JoinOperator.OR)
        cc.constraint = [pc1]
        with pytest.raises(InvalidCompositeConstraint):
            cc.to_json()


class TestQuery:

    def test_query_to_json(self):
        query = Query()
        query.where = PrimitiveConstraint("@id", "elem-1")
        result = json.loads(query.to_json())
        assert result["@type"] == "Query"
        assert "where" in result
        assert result["where"]["property"] == "@id"

    def test_query_with_composite(self):
        query = Query()
        cc = CompositeConstraint(operator=JoinOperator.AND)
        cc.constraint = [
            PrimitiveConstraint("@id", "a"),
            PrimitiveConstraint("@id", "b"),
        ]
        query.where = cc
        result = json.loads(query.to_json())
        assert result["where"]["@type"] == "CompositeConstraint"
        assert len(result["where"]["constraint"]) == 2


class TestOperatorEnums:

    def test_operator_enum_completeness(self):
        assert Operator.EQUALS == "="
        assert Operator.INSTANCE_OF == "instanceOf"
        assert Operator.IN == "in"
        assert Operator.LOWER == "<"
        assert Operator.UPPER == ">"
        assert Operator.EQUALS_OR_LOWER == "<="
        assert Operator.EQUALS_OR_UPPER == ">="

    def test_join_operator_values(self):
        assert JoinOperator.AND == "and"
        assert JoinOperator.OR == "or"
