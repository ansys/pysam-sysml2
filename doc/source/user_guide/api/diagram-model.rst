Work with diagrams
##################

.. warning::

    Functionalities for loading, downloading, and navigating diagrams are available only for projects of type ``SAM``.

This page explains how to load, download, and navigate diagrams from your SysML v2 project using the SAM REST API.

Load diagrams
=============

Before interacting with diagrams, load them using the
:class:`ansys.sam.sysml2.diagrams.tools.sam_diagram_downloader.SamDiagramDownloader` context manager, which requires an :mod:`ansys.sam.sysml2.api` connector.

Create a SAM REST API connector:

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 21-25
    :language: python
    :caption: Create SAM REST API connector

Load diagrams from a project and make them available for further operations like downloading:

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 35-36
    :language: python
    :caption: Load diagrams using SAM diagram manager

Outside the ``with`` block, the ``SamDiagramDownloader`` context manager is no longer active. This ensures proper setup and cleanup of resources when working with diagrams.

Download diagrams
=================

Load diagrams inside an
:class:`ansys.sam.sysml2.diagrams.sam_diagram_manager.SAMDiagramManager` context before downloading them.

Also, instantiate an
:class:`ansys.sam.sysml2.diagrams.tools.sam_diagram_downloader.SamDiagramDownloader` object:

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 40
    :language: python
    :caption: Create a SAM diagram downloader

Download all diagrams
---------------------

After loading diagrams, download all diagrams and save them into a ZIP archive:

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 48-53
    :language: python
    :caption: Download all diagrams with custom parameters

**Default parameters**

If you do not specify parameters, these defaults are used to format and name your download archive:

- ``file_format``: ``"SVG"``
- ``filename``: ``"<PackageName>_<FileFormat>_diagrams.zip"``

Get and download a single diagram
---------------------------------

Get a single diagram and download it in a given format:

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 56-57
    :language: python
    :caption: Get a single diagram

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 59-64
    :language: python
    :caption: Download this single diagram

Download diagrams in a loop
---------------------------

Iterate through diagrams inside a specific section of your model, such as the `Usage` section:

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 67
    :language: python
    :caption: Get desired diagrams

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 68-72
    :language: python
    :caption: Download diagrams from Usage section in a loop

Navigate the model from diagrams
================================

Each diagram object links to a model element. You can access its name or other metadata.

Get diagram metadata
--------------------

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 67
    :language: python
    :caption: Get desired diagram

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 78
    :language: python
    :caption: Get diagram metadata from the model element

Getting the diagram metadata returns the name of the associated model element that the diagram represents.

Loop through diagrams
---------------------

Print the names of diagrams from a section of the model:

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 67
    :language: python
    :caption: Get desired diagrams

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 80-81
    :language: python
    :caption: Loop through diagrams and print names

.. note::

    Navigate through ``_plane``, ``_model_element``, and ``_owned_diagram_elements`` to
    discover the logical elements that the diagram ties to.

.. only:: html

    .. grid:: 2

        .. grid-item-card:: :fa:`arrow-left` Previous step
            :link: write-model
            :link-type: doc

            Write in your model

        .. grid-item-card:: Next step :fa:`arrow-right`
            :link: information
            :link-type: doc

            Find information
