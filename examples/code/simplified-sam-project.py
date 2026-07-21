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

"""Ansys SysML2 project example for PySAM SysML2."""

import requests
from urllib3.exceptions import InsecureRequestWarning

from ansys.sam.sysml2.tools.ansys_scripting_project import AnsysScriptingProject

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

project = AnsysScriptingProject(
    server_url="<SAM Server URL>",
    organization_id="<Orga ID>",  # The organization ID
    token="<Token>",  # Your authorization token
    use_ssl=False,  # If the server hasn't a valid SSL
    project_id="<Bike Project ID>",  # The project ID
)

diagrams_status = project.is_diagrams_available()
print(f"Diagrams Status : {'Available' if diagrams_status else 'Unavailable'}", end="\n\n")

SAVE_IMAGE_PATH = "The path of the directory you want to save your diagrams into"
diagrams_info = project.get_project_diagrams_info()
first_diagram_id = diagrams_info[0]["diagramId"]

# -----------------------------------------
# Download ZIP file containing diagrams
# -----------------------------------------

response = project.download_all_diagrams(path=SAVE_IMAGE_PATH, file_format="png", filename="png")
print(f"> ZIP saved at: {response}\n")

# -----------------------------------------
# Download single diagram
# -----------------------------------------

path = project.download_diagram(
    diagram_id=first_diagram_id,
    filename="CUSTOM_FILENAME",
    file_format="png",
    path=SAVE_IMAGE_PATH,
)
print(f"> Diagram saved at: {path}\n")

for i, diagram in enumerate(diagrams_info, 1):
    project.download_diagram(
        diagram_id=diagram["diagramId"], file_format="png", path=SAVE_IMAGE_PATH + "/all"
    )
    print(f"> Saved diagram #{i}: {diagram['name']}\n")

# -----------------------------------------
# Create element
# -----------------------------------------

project.factory.create_attribute_usage(declared_name="NewAttr")

# -----------------------------------------
# Get diagrams information
# -----------------------------------------

print(project.get_project_diagrams_info(), end="\n\n")

print(project.get_single_diagram_info(first_diagram_id))
