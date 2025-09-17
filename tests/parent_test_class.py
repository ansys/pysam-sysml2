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
"""Base Metaclass for Tests"""

import json
from pathlib import Path

import pytest

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from mocked_server.mocked_server import MockedServer
from mocked_server.routes.const import VALID_ORGANIZATION, VALID_TOKEN

TESTS = Path(__file__).resolve().parent
MOCKED_SERVER = TESTS / "mocked_server" / "commit_json"


class ParentTestClass:
    @pytest.fixture()
    def valid_source(self) -> AnsysSysML2APIConnector:
        return AnsysSysML2APIConnector(
            server_url=MockedServer.get_url(),
            organization_id=VALID_ORGANIZATION,
            token=VALID_TOKEN,
        )

    def load_json_from_file(self, path: Path):
        with path.open(encoding="utf-8") as f:
            return json.load(f)

    def load_json_from_case(self, case_name: str, filename: str = "request.json"):
        return self.load_json_from_file(MOCKED_SERVER / case_name / filename)
