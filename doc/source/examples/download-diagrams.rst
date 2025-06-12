.. _Download_Example:

Download diagrams and create new elements
#########################################

This example demonstrates how to work with the `Bike` model in a SysML v2 project using the Ansys SAM API. It covers:

- Loading and downloading diagrams.
- Navigating and saving diagram content.

.. note::

    If you have never used the PySAM library before, it is recommended to begin with a simpler example to understand how the library works (:ref:`bike_weight<Bike_Example>`, :ref:`computer_cost<Computer_Example>`).

Prerequisites
=============

Ensure you have:

1. A running SAM server instance.
2. A valid **Organization ID**, **Project ID**, and **Token**.
3. The `bike.xmi` model imported into your project.

Python example
==============

.. code-block:: python

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
    print(f"Diagram saved as PNG at: C:/Diagrams/Images/")

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

.. note::

    - Replace placeholder values with your actual SAM configuration.
    - Always use ``DiagramManager`` within a context manager (``with`` statement).
    - Diagram content can be retrieved in various formats: ``png``, ``svg``, etc.

