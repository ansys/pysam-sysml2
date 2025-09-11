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

"""DataVersion Module."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class DataVersion:
    """Class to edit or create a SysML Element."""

    payload: dict = field(default_factory=dict)
    identity: str = field(default=None)

    def identify(self, element_id: str):
        """Set the identity with the given element id of the DataVersion."""
        self.identity = element_id

    def add_change(self, key: str, value: Any):
        """Add the change into the DataVersion. Also serialize the data if it's needed."""
        from ansys.sam.sysml2.classes.sysml_element import SysMLElement
        from ansys.sam.sysml2.data_structures.observed_list import ObservedList

        if isinstance(value, SysMLElement):
            self.payload[key] = {"@id": value._id}
        elif isinstance(value, (ObservedList, list)):
            self.payload[key] = [
                {"@id": x._id} if isinstance(x, SysMLElement) else x for x in value
            ]
        else:
            self.payload[key] = value

    def to_json(self) -> dict:
        """Serialize the data into a json dict."""
        data = {
            "@type": "DataVersion",
            "payload": self.payload,
        }
        if self.identity is not None:
            data["identity"] = {"@id": self.identity, "@type": "DataIdentity"}
        return data
