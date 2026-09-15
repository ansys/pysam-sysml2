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

"""Example showing project management: create, list, update, and delete projects."""

import requests
from urllib3.exceptions import InsecureRequestWarning

from ansys.sam.sysml2 import AnsysSysML2APIConnector, SysML2ProjectManager

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Create your connector for the SAM Server
connector = AnsysSysML2APIConnector(
    server_url="<SAM Server URL>",  # Your SAM server base URL
    organization_id="<Orga ID>",  # The organization ID
    token="<Token>",  # Your authorization token
    use_ssl=False,  # If the server hasn't a valid SSL
)

project_manager = SysML2ProjectManager(connector=connector)

# --- List all existing projects ---
projects = project_manager.get_projects()
print(f"Found {len(projects)} project(s):")
for p in projects:
    print(f"  - {p['name']} (id: {p['@id']})")

# --- Create a new project ---
my_project = project_manager.create_scripting_project(
    name="My New Project",
    description="A project created via PySAM SysML2",
)
project_id = my_project.get_id()
print(f"\nCreated project: {my_project.get_name()} (id: {project_id})")

# --- Update the project ---
updated = project_manager.update_project(
    project_id=project_id,
    name="My Renamed Project",
    description="Updated description",
)
print(f"\nUpdated project: {updated['name']} - {updated['description']}")

# --- Delete the project ---
deleted = project_manager.delete_project(project_id=project_id)
print(f"\nDeleted project with id: {deleted['@id']}")
