Working with Diagrams
#####################

This section describes how to **load**, **download**, and **navigate** diagrams from your SysML v2 project using the Ansys SAM API.

Load Diagrams
=============

Before interacting with diagrams, they must be loaded using the `SysML2DiagramManager` context manager.

Basic Usage
-----------

To load diagrams from a project and make them available for further operations like downloading:

.. code-block:: python

    with SysML2DiagramManager(connector=connector) as diagrams:
        diagrams.load_diagrams(model=myBikeProject)

Outside the ``with`` block, the ``diagrams`` manager is no longer active, and diagram-related operations such as ``download_all_diagrams()`` will **not work**.

This ensures proper setup and teardown of resources when working with diagrams.

Download Diagrams
=================

Diagrams must be loaded inside a `SysML2DiagramManager` context before they can be downloaded.

Download All Diagrams
---------------------

Once the diagrams are loaded, you can download **all diagrams** and save them into a zip archive:

.. code-block:: python

    with SysML2DiagramManager(connector=connector) as diagrams:
        diagrams.load_diagrams(model=myBikeProject)

        print(
            diagrams.download_all_diagrams(
                project=myBikeProject
                path="C:/Diagrams/Images/",
                file_format="jpeg",
                filename="download_all_diagrams_with_args.zip"
            )
        )

**Default Parameters:**

- ``file_format``: "svg"
- ``filename``: "<PackageName>_<FileFormat>_diagrams.zip"

If not specified, these defaults will be used to name and format your download archive.

``download_all_diagrams()`` will raise an error if used outside the `with` context where diagrams are not loaded.

Download a Single Diagram
-------------------------

You can also download a specific diagram in a given format:

.. code-block:: python

    first_diagram = myBikeProject.get_root_package().__diagram[0]
    first_diagram.download_diagram(file_format="svg", path="C:/Diagrams/Images/")
    print("🖼️ Diagram saved as SVG at: C:/Diagrams/Images/")

Save Diagram from Content Bytes
-------------------------------

Diagram content can be extracted and saved using `DiagramDownloader`:

.. code-block:: python

    from ansys.sam.sysml2.diagrams.utils import DiagramDownloader

    first_diagram = myBikeProject.get_root_package().__diagram[0]
    png_content = first_diagram.get_content(file_format="png")
    saved_path = DiagramDownloader.save_content(content=png_content, path="C:/Diagrams/Images/", filename="first_diagram", file_format="png")
    print(f"🖼️ Diagram saved as PNG at: C:/Diagrams/Images/")

Download Diagrams in a Loop
---------------------------

You can iterate through diagrams inside a specific section of your model, for example, `Usage`:

.. code-block:: python

    usage_diagrams = myBikeProject.get_root_package().Usage.__diagram
    for i, diagram in enumerate(usage_diagrams, 1):
        diagram.download_diagram(file_format="svg", path="C:/Diagrams/Images/")
        print(f"🔽 Saved Usage diagram #{i}: {diagram._plane._model_element._name}")


Navigate Model from Diagrams
============================

Each diagram object links to a model element, and you can access its name or other metadata:

Get Diagram Metadata
--------------------

.. code-block:: python

    first_diagram = myBikeProject.get_root_package().__diagram[0]
    print(first_diagram._plane._model_element._name)

This returns the name of the associated model element the diagram represents.

Loop Through Diagrams
---------------------

To print out names of diagrams from a section of the model:

.. code-block:: python

    for diagram in myBikeProject.get_root_package().__diagram:
        print("Diagram name:", diagram._plane._model_element._name)

.. note::

    Navigating through `_plane` and `_model_element` and `_owned_diagram_elements` allows you to discover the logical elements the diagram is tied to.


.. only:: html

    .. grid:: 2

        .. grid-item-card:: :fa:`arrow-left` Previous step
            :link: write_model
            :link-type: doc

            Write in your model

        .. grid-item-card:: Next step :fa:`arrow-right`
            :link: information
            :link-type: doc

            How to get some information
