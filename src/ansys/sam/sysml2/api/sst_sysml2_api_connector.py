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

"""OMG SST / SysML-v2-API-Services connector."""

from __future__ import annotations

import json
from typing import Any
from uuid import uuid4

import requests

from ansys.sam.sysml2.api.template_sysml2_api_connector import (
    TemplateSysML2APIConnector,
)
from ansys.sam.sysml2.classes.http_request import HttpRequest
from ansys.sam.sysml2.exception.connector_exception import (
    BadRequestConnectionException,
    ConnectorConnectionException,
    ElementNotFoundException,
    HTTPResponseException,
    InvalidElementJsonFoundException,
    ProjectNotFoundException,
    UnauthorizedConnectionException,
)


class SstSysML2APIConnector(TemplateSysML2APIConnector):
    """
    SysML v2 connector for the OMG SST Pilot API (SysML-v2-API-Services).

    Compared to ``AnsysSysML2APIConnector`` (SAM):
    - no authentication
    - base URL is the server root (no ``/api/spaces/{org}/sysml2``)
    - branch head is a commit UUID (no ``commits/head`` alias)
    - new projects are seeded with Namespace + Root Package + OwningMembership
    - derived collections are rebuilt client-side (``default_includes_derived()`` is ``False``)
    """

    _server_url: str
    _head_cache: dict[str, str | None]

    def __init__(self, server_url: str = "http://localhost:9001", use_ssl: bool = False):
        """
        Construct a new SST connector.

        Parameters
        ----------
        server_url : str, default: ``http://localhost:9001``
            SST API base URL.
        use_ssl : bool, default: False
            Whether ``requests`` should verify TLS certificates.
        """
        super().__init__(use_ssl=use_ssl)
        if server_url.endswith("/"):
            server_url = server_url[:-1]
        self._server_url = server_url
        self._head_cache = {}

    def default_includes_derived(self) -> bool:
        """SST omits derived collections; PySAM rebuilds them from ``ownedRelationship``."""
        return False

    def _build_endpoint(self, endpoint: str) -> str:
        """Build the full URL from the API endpoint."""
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
        return f"{self._server_url}{endpoint}"

    def _add_authentication_field(self, http_request: HttpRequest) -> HttpRequest:
        """Leave the request unauthenticated (SST has no auth)."""
        return http_request

    def _commit_ref(self, project_id: str) -> str | None:
        """Resolve the default branch head commit UUID."""
        return self._resolve_head_commit_id(project_id)

    def create_project(
        self,
        project_name: str,
        project_description: str = "Project description",
    ) -> dict:
        """
        Create a project and seed a Namespace / Root Package structure.

        Parameters
        ----------
        project_name : str
            Name of the project.
        project_description : str, default: ``Project description``
            Description of the project.

        Returns
        -------
        dict
            Project record from the API.
        """
        project = super().create_project(project_name, project_description)
        project_id = project["@id"]
        self._seed_root_namespace(project_id)
        return project

    def create_commit(self, project_id: str, commit: str) -> dict:
        """
        Post a commit and refresh the cached head.

        PySAM's ``Commit.to_json`` sends ``previousCommit: {"@id": "head"}``, which
        SAM accepts. SST requires a real UUID or omits the field on the first commit.
        """
        body = json.loads(commit)
        previous = body.get("previousCommit")
        previous_id = None
        if isinstance(previous, dict):
            previous_id = previous.get("@id")
        elif isinstance(previous, str):
            previous_id = previous

        if previous_id in (None, "head"):
            head_id = self._resolve_head_commit_id(project_id)
            if head_id:
                body["previousCommit"] = {"@id": head_id}
            else:
                body.pop("previousCommit", None)

        http_request = self._build_http_request(endpoint=f"/projects/{project_id}/commits")
        http_request.json_body = body
        result = self._send_request(http_request=http_request, call=requests.post)
        if isinstance(result, dict) and "@id" in result:
            self._head_cache[project_id] = result["@id"]
        else:
            self._head_cache.pop(project_id, None)
        return result

    def invalidate_head(self, project_id: str) -> None:
        """Drop a cached head commit id for the project."""
        self._head_cache.pop(project_id, None)

    def link_owned_member(
        self,
        project_id: str,
        owner_id: str,
        member_id: str,
        existing_owned_relationship_ids: list[str] | None = None,
    ) -> dict:
        """
        Create an OwningMembership and attach it to the owner.

        SST does not auto-create memberships when Factory sets ``owner``.
        """
        membership_id = str(uuid4())
        owned_relationships = list(existing_owned_relationship_ids or [])
        owned_relationships.append(membership_id)

        owner = self.get_element_by_id(project_id, owner_id)
        owner_payload = self._writable_element_payload(owner)
        owner_payload["ownedRelationship"] = [{"@id": rid} for rid in owned_relationships]

        commit = {
            "@type": "Commit",
            "change": [
                {
                    "@type": "DataVersion",
                    "identity": {"@id": membership_id, "@type": "DataIdentity"},
                    "payload": {
                        "@type": "OwningMembership",
                        "owningRelatedElement": {"@id": owner_id},
                        "ownedRelatedElement": [{"@id": member_id}],
                        "memberElement": {"@id": member_id},
                        "ownedMemberElement": {"@id": member_id},
                    },
                },
                {
                    "@type": "DataVersion",
                    "identity": {"@id": owner_id, "@type": "DataIdentity"},
                    "payload": owner_payload,
                },
            ],
        }
        return self.create_commit(project_id, json.dumps(commit))

    @staticmethod
    def _writable_element_payload(element: dict) -> dict:
        """Build a commit payload from a GET element."""
        payload: dict[str, Any] = {"@type": element.get("@type")}
        for key in (
            "declaredName",
            "declaredShortName",
            "owner",
            "owningNamespace",
            "owningMembership",
            "owningRelationship",
        ):
            value = element.get(key)
            if value is not None:
                payload[key] = value
        return payload

    def _seed_root_namespace(self, project_id: str) -> dict:
        """Create Namespace + Root Package + OwningMembership (SST has no initial commit)."""
        namespace_id = str(uuid4())
        package_id = str(uuid4())
        membership_id = str(uuid4())
        commit = {
            "@type": "Commit",
            "change": [
                {
                    "@type": "DataVersion",
                    "identity": {"@id": namespace_id, "@type": "DataIdentity"},
                    "payload": {
                        "@type": "Namespace",
                        "ownedRelationship": [{"@id": membership_id}],
                    },
                },
                {
                    "@type": "DataVersion",
                    "identity": {"@id": package_id, "@type": "DataIdentity"},
                    "payload": {
                        "@type": "Package",
                        "declaredName": "Root",
                        "owner": {"@id": namespace_id},
                        "owningNamespace": {"@id": namespace_id},
                        "owningMembership": {"@id": membership_id},
                    },
                },
                {
                    "@type": "DataVersion",
                    "identity": {"@id": membership_id, "@type": "DataIdentity"},
                    "payload": {
                        "@type": "OwningMembership",
                        "owningRelatedElement": {"@id": namespace_id},
                        "ownedRelatedElement": [{"@id": package_id}],
                        "memberElement": {"@id": package_id},
                        "ownedMemberElement": {"@id": package_id},
                    },
                },
            ],
        }
        return self.create_commit(project_id, json.dumps(commit))

    def _resolve_head_commit_id(self, project_id: str) -> str | None:
        """Resolve the default branch head commit UUID, with a small cache."""
        if project_id in self._head_cache:
            return self._head_cache[project_id]

        project = self.get_project_by_id(project_id)
        default_branch = project.get("defaultBranch") or {}
        branch_id = (
            default_branch.get("@id") if isinstance(default_branch, dict) else default_branch
        )
        if not branch_id:
            self._head_cache[project_id] = None
            return None

        http_request = self._build_http_request(
            endpoint=f"/projects/{project_id}/branches/{branch_id}"
        )
        branch = self._send_request(http_request=http_request, call=requests.get)
        head = branch.get("head") if isinstance(branch, dict) else None
        commit_id = None
        if isinstance(head, dict):
            commit_id = head.get("@id")
        elif isinstance(head, str):
            commit_id = head

        self._head_cache[project_id] = commit_id
        return commit_id

    def get_all_elements(self, project_id: str, **kwargs) -> list:
        """Get all elements at the project head commit."""
        filtered_kwargs = {
            key: value
            for key, value in kwargs.items()
            if key not in ("includes_derived", "includes_inherited")
        }
        return super().get_all_elements(project_id, **filtered_kwargs)

    def _send_request(self, http_request: HttpRequest, call) -> object:
        """Send the HTTP request (SST may return 201 and sparse error bodies)."""
        response = None
        try:
            response = call(**http_request.to_dict(), verify=self._use_ssl)
        except Exception as e:
            raise ConnectorConnectionException(e)

        if response.status_code in (200, 201):
            try:
                if not response.content:
                    return {}
                return json.loads(response.content)
            except Exception as e:
                raise InvalidElementJsonFoundException(f"Invalid JSON received : {e}")
        self._handle_http_error(response)

    def _handle_http_error(self, response: requests.Response) -> None:
        """Raise connector exceptions from SST / Play error payloads."""
        payload = self._safe_json(response)
        message = self._extract_error_message(payload, response)

        match response.status_code:
            case 500:
                raise ConnectorConnectionException(message or "Internal Server Error")
            case 409:
                raise ConnectorConnectionException(message or "Resource conflict")
            case 404:
                self._handle_404_message(message, response)
            case 403:
                raise ConnectorConnectionException(message or "Forbidden")
            case 401:
                raise UnauthorizedConnectionException("Authentication failed")
            case 400:
                raise BadRequestConnectionException(f"Bad Request : {message}")
            case _:
                raise HTTPResponseException(response.content)

    def _handle_404_message(self, message: str, response: requests.Response) -> None:
        """Map 404 bodies to the closest PySAM exception."""
        text = message or ""
        if "Organization" in text:
            raise ConnectorConnectionException(text)
        if "Element" in text:
            raise ElementNotFoundException(text)
        if "Project" in text:
            raise ProjectNotFoundException(text)
        raise HTTPResponseException(response.content)

    @staticmethod
    def _safe_json(response: requests.Response) -> Any:
        """Parse JSON body or return ``None``."""
        try:
            return response.json()
        except Exception:
            return None

    @staticmethod
    def _extract_error_message(payload: Any, response: requests.Response) -> str:
        """Pull a human-readable message from SST or SAM-shaped errors."""
        if isinstance(payload, dict):
            if isinstance(payload.get("message"), str) and payload["message"]:
                return payload["message"]
            error = payload.get("error")
            if isinstance(error, dict) and isinstance(error.get("message"), str):
                return error["message"]
            if isinstance(error, str) and error:
                return error
        text = (response.text or "").strip()
        return text or f"HTTP {response.status_code}"
