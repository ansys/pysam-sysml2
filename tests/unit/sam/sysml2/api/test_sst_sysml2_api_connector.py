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

"""Unit tests for SstSysML2APIConnector."""

import json

import pytest

from ansys.sam.sysml2.api.sst_sysml2_api_connector import SstSysML2APIConnector
from ansys.sam.sysml2.classes.http_request import HttpRequest


@pytest.fixture
def connector():
    return SstSysML2APIConnector(server_url="http://localhost:9001", use_ssl=False)


class TestSstSysML2APIConnector:

    def test_build_endpoint_root_url(self, connector):
        url = connector._build_endpoint("/projects")
        assert url == "http://localhost:9001/projects"
        assert "/api/spaces" not in url

    def test_add_authentication_field_no_bearer(self, connector):
        http_request = HttpRequest(url="http://test")
        result = connector._add_authentication_field(http_request)
        assert "Authorization" not in result.headers

    def test_commit_ref_resolves_head_uuid(self, connector, mocker):
        project_id = "proj-1"
        branch_id = "branch-1"
        commit_id = "commit-abc"

        mocker.patch(
            "requests.get",
            side_effect=[
                mocker.Mock(
                    status_code=200,
                    content=json.dumps(
                        {
                            "@id": project_id,
                            "defaultBranch": {"@id": branch_id},
                        }
                    ).encode(),
                ),
                mocker.Mock(
                    status_code=200,
                    content=json.dumps({"head": {"@id": commit_id}}).encode(),
                ),
            ],
        )

        assert connector._commit_ref(project_id) == commit_id

    def test_create_commit_rewrites_previous_head(self, connector, mocker):
        project_id = "proj-1"
        head_id = "commit-head"
        connector._head_cache[project_id] = head_id

        mock_post = mocker.patch(
            "requests.post",
            return_value=mocker.Mock(
                status_code=200,
                content=json.dumps({"@id": "commit-new", "@type": "Commit"}).encode(),
            ),
        )

        body = {
            "@type": "Commit",
            "change": [],
            "previousCommit": {"@id": "head"},
        }
        connector.create_commit(project_id, json.dumps(body))

        sent = mock_post.call_args.kwargs.get("json") or mock_post.call_args[1].get("json")
        assert sent["previousCommit"]["@id"] == head_id
        url = mock_post.call_args.kwargs.get("url") or mock_post.call_args[0][0]
        assert url.endswith(f"/projects/{project_id}/commits")

    def test_get_all_elements_empty_when_no_head(self, connector, mocker):
        mocker.patch.object(connector, "_commit_ref", return_value=None)
        assert connector.get_all_elements("proj-1") == []

    def test_default_includes_derived_false(self, connector):
        assert connector.default_includes_derived() is False
