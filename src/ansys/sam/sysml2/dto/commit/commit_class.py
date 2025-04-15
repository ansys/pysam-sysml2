# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
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

"""Commit Class module."""

import json
from typing import List

from ansys.sam.sysml2.dto.commit.data_version import DataVersion


class Commit:
    """Commit Class module."""

    project_id: str = None
    changes: List[DataVersion]
    previous_commit_id: str = "head"

    def __init__(self, project_id: str):
        """
        Construct new instance.

        Parameters
        ----------
        project_id : str
            The context project id
        """
        self.project_id = project_id
        self.changes = list()

    def add_change(self, change: DataVersion):
        """
        Add a change into the commit.

        Parameters
        ----------
        change : DataVersion
            The data version of the change.
        """
        self.changes.append(change)

    def to_json(self):
        """
        Serialize the commit data into json.

        Returns
        -------
        Str
            Json data
        """
        return json.dumps(
            {
                "@type": "Commit",
                "change": [x.to_json() for x in self.changes],
                "owningProject": {"@id": self.project_id},
                "previousCommit": {"@id": self.previous_commit_id},
            }
        )
