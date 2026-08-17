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

"""Unit tests for TemplateSysML2APIConnector commit paths."""

import json

import pytest

from ansys.sam.sysml2.api.ansys_sysml2_api_connector import AnsysSysML2APIConnector
from tests.unit.const import VALID_ORGANIZATION, VALID_TOKEN


@pytest.fixture
def connector():
    return AnsysSysML2APIConnector(
        server_url="http://fake-server",
        organization_id=VALID_ORGANIZATION,
        token=VALID_TOKEN,
        use_ssl=False,
    )


class TestTemplateSysML2APIConnector:

    def test_create_commit_uses_plural_path(self, connector, mocker):
        mock_post = mocker.patch(
            "requests.post",
            return_value=mocker.Mock(
                status_code=200,
                content=json.dumps({"@id": "commit-1", "@type": "Commit"}).encode(),
            ),
        )
        connector.create_commit("proj-1", '{"@type": "Commit", "change": []}')

        assert mock_post.called
        url = mock_post.call_args.kwargs.get("url") or mock_post.call_args[0][0]
        assert url.endswith("/projects/proj-1/commits")
        assert "/commit" not in url.replace("/commits", "")

    def test_get_all_elements_uses_head_alias(self, connector, mocker):
        mock_get = mocker.patch(
            "requests.get",
            return_value=mocker.Mock(status_code=200, content=b"[]"),
        )
        connector.get_all_elements("proj-1")

        url = mock_get.call_args.kwargs.get("url") or mock_get.call_args[0][0]
        assert "/commits/head/elements" in url
