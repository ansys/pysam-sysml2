# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
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

"""File  created on Mon Dec 16 2024."""

from dataclasses import dataclass, field
from typing import List

from overrides import overrides

from ansys.sam.sysml2.exception.query_exception import InvalidCompositeConstraint

from .query_enum import JoinOperator, Operator


class Constraint:
    """Constraint Interface."""

    def to_json(self) -> dict:
        """
        to_json convert the class to JSON format.

        Returns
        -------
        dict
            The class adapted to JSON Format
        """
        data = {"@type": self.__class__.__name__}
        data.update(dict((k, v) for k, v in self.__dict__.items() if not k.startswith("_")))
        return data


@dataclass
class PrimitiveConstraint(Constraint):
    """PrimitiveConstraint for simple Query constraint."""

    property: str
    value: str
    inverse: bool = field(default=False)
    operator: Operator = field(default=Operator.EQUALS)


@dataclass
class CompositeConstraint(Constraint):
    """CompositeConstraint for multiple Query constraint."""

    operator: JoinOperator = field(default=JoinOperator.AND)
    constraint: List[Constraint] = field(default_factory=list)

    @overrides
    def to_json(self) -> dict:
        """
        to_json convert the class to JSON format.

        Returns
        -------
        dict
            The class adapted to JSON Format
        """
        data = super().to_json()
        end_data = data.copy()
        end_data["constraint"] = list()
        for c in data["constraint"]:
            end_data["constraint"].append(c.to_json())
        if len(end_data["constraint"]) < 2:
            raise InvalidCompositeConstraint("Not enough constraint")
        return end_data
