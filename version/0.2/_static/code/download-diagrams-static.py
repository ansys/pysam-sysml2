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
"""Download diagrams static example for PySAM SysML2."""

import requests
from urllib3.exceptions import InsecureRequestWarning

from ansys.sam.sysml2 import AnsysSysML2APIConnector, SysML2ProjectManager
from ansys.sam.sysml2.diagrams.api.sam_rest_api_connector import SamRestApiConnector
from ansys.sam.sysml2.diagrams.sam_diagram_manager import SAMDiagramManager
from ansys.sam.sysml2.diagrams.tools.sam_diagram_downloader import SamDiagramDownloader

# Used to disable warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ansyssysml2apiconnector = AnsysSysML2APIConnector(
    server_url="<SAM Server URL>",  # Your SAM server base URL
    organization_id="<Orga ID>",  # The organization ID
    token="<Token>",  # Your authorization token
    use_ssl=False,  # If the server hasn't a valid SSL
)

sam_rest_api_connector = SamRestApiConnector(
    server_url="<SAM Server URL>",  # Your SAM server base URL
    token="<Token>",  # Your authorization token
    use_ssl=False,  # If the server hasn't a valid SSL
)

project_manager = SysML2ProjectManager(connector=ansyssysml2apiconnector)

project = project_manager.get_sysml_project("<Bike Project ID>")

# -----------------------------------------
# Work with diagrams
# -----------------------------------------

with SAMDiagramManager(connector=sam_rest_api_connector) as diagrams:
    diagrams.load_diagrams(model=project)

print(f"Loaded {len(project.get_root_package().__diagram)} diagrams.")

downloader = SamDiagramDownloader(connector=sam_rest_api_connector, project_id=project._id)

# -----------------------------------------
# Download diagrams
# -----------------------------------------

SAVE_IMAGE_PATH = "The path of the directory you want to save your diagrams into"

### You can specify the file format and the filename.
### The defaults are file_format="svg" and filename="<PackageName>_<FileFormat>_diagrams.zip"
path = downloader.download_all_diagrams(
    path=SAVE_IMAGE_PATH,
    file_format="jpeg",
    filename="download_all_diagrams_with_args.zip",
)
print(f"ZIP saved at: {path}\n")


first_diagram = project.get_root_package().__diagram[0]
first_diagram_id = first_diagram._id

path = downloader.download_diagram(
    diagram_id=first_diagram_id,
    path=SAVE_IMAGE_PATH,
    file_format="svg",
)
print(f"Diagram saved at: {path}")


usage_diagrams = project.get_root_package().get("Usage").__diagram
for i, diagram in enumerate(usage_diagrams, 1):
    downloader.download_diagram(
        diagram_id=diagram._id, file_format="png", path=SAVE_IMAGE_PATH + "/Usage"
    )
    print(f"> Saved Usage diagram #{i}: {diagram._plane._model_element._name}")

# -----------------------------------------
# Navigate through diagrams
# -----------------------------------------

print(first_diagram._plane._model_element._name)

for diagram in usage_diagrams:
    print("Diagram name:", diagram._name)
