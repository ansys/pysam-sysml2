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

from ansys.sam.sysml2 import SysML2ProjectManager, AnsysSysML2APIConnector
from ansys.sam.sysml2.diagrams.SysML2DiagramManager import SysML2DiagramManager
from ansys.sam.sysml2.diagrams.utils import DiagramDownloader

conn = AnsysSysML2APIConnector(
    server_url="https://127.0.0.1:8443/",  # Your Sam server base URL
    organization_id="<Orga ID>",  # The Organization ID
    token="<Token>",  # Your Auth Token (See section below)
    use_ssl=False,  # If the server has a valid SSL
)

model_manager = SysML2ProjectManager(connector=conn)

project = model_manager.get_project("<Bike Project ID>")

# -----------------------------------------
# Work with Diagrams
# -----------------------------------------

with SysML2DiagramManager(connector=conn) as diagrams:
    diagrams.load_diagrams(model=project)
    ### You can specify the file_format and the filename,
    ### But as default: file_format="svg", filename="<PackageName>_<FileFormat>_diagrams.zip"
    ### Also, download_all_diagrams will only work in the `with` context
    print(
        diagrams.download_all_diagrams(
            project=project,
            path="C:/Diagrams/Images/",
            file_format="jpeg",
            filename="download_all_diagrams_with_args.zip",
        )
    )

print(f"Loaded {len(project.get_root_package().__diagram)} diagrams.")

first_diagram = project.get_root_package().__diagram[0]
first_diagram.download_diagram(file_format="svg", path="C:/Diagrams/Images/")
print("Diagram saved as SVG at: C:/Diagrams/Images/")

png_content = first_diagram.get_content(file_format="png")
saved_path = DiagramDownloader.save_content(
    content=png_content,
    path="C:/Diagrams/Images/",
    filename="first_diagram",
    file_format="png",
)
print("Diagram saved as PNG at: C:/Diagrams/Images/")

usage_diagrams = project.get_root_package().Usage.__diagram
for i, diagram in enumerate(usage_diagrams, 1):
    diagram.download_diagram(file_format="svg", path="C:/Diagrams/Images/Usage")
    print(f"Saved Usage diagram #{i}: {diagram._plane._model_element._name}")

# -----------------------------------------
# Navigate through Diagrams
# -----------------------------------------

first_diagram = project.get_root_package().__diagram[0]
print(first_diagram._plane._model_element._name)

for diagram in project.get_root_package().Usage.__diagram:
    print("Diagram name:", diagram._name)
