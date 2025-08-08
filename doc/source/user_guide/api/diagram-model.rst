Working with diagrams
#####################

.. warning::

    The functionalities described in this section (loading, downloading, and navigating diagrams) are **only available for projects of type SAM**.


This section describes how to **load**, **download**, and **navigate** diagrams from your SysML v2 project using the SAM REST API.

Load diagrams
=============

Before interacting with diagrams, they must be loaded using the :ref:`SAMDiagramManager <D_M_Section>` context manager which needs a :ref:`SamRestApiConnector <C_I_Section>`.

Basic usage
-----------

First, create a SAM REST API Connector:

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 21-25
    :language: python
    :caption: Create SAM REST API Connector


To load diagrams from a project and make them available for further operations like downloading:

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 35-36
    :language: python
    :caption: Load diagrams using SAMDiagramManager

Outside the ``with`` block, the ``diagram`` manager is no longer active.
This ensures proper setup and cleanup of resources when working with diagrams.

Download diagrams
=================

Diagrams must be loaded inside a :ref:`SAMDiagramManager <D_M_Section>` context before they can be downloaded.

Also, instantiate a :ref:`SamDiagramDownloader <D_U_Section>`:

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 40
    :language: python
    :caption: Create a SamDiagramDownloader

Download all diagrams
---------------------

Once the diagrams are loaded, you can download **all diagrams** and save them into a zip archive:

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 48-53
    :language: python
    :caption: Download all diagrams with custom parameters

**Default Parameters:**

- ``file_format``: "SVG"
- ``filename``: "<PackageName>_<FileFormat>_diagrams.zip"

If not specified, these defaults are used to name and format your download archive.

Download a single diagram
-------------------------

You can also download a specific diagram in a given format:

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 56-57
    :language: python
    :caption: Get desired Diagram

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 59-64
    :language: python
    :caption: Download a single diagram

Download diagrams in a loop
---------------------------

You can iterate through diagrams inside a specific section of your model, for example, `Usage`:

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 67
    :language: python
    :caption: Get desired Diagrams

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 68-72
    :language: python
    :caption: Download diagrams from Usage section in a loop

Navigate model from diagrams
============================

Each diagram object links to a model element, and you can access its name or other metadata:

Get diagram metadata
--------------------

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 67
    :language: python
    :caption: Get desired Diagram

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 78
    :language: python
    :caption: Get diagram metadata from model element

This returns the name of the associated model element the diagram represents.

Loop through diagrams
---------------------

To print out names of diagrams from a section of the model:

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 67
    :language: python
    :caption: Get desired Diagrams

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 80-81
    :language: python
    :caption: Loop through diagrams and print names

.. note::

    Navigating through ``_plane`` and ``_model_element`` and ``_owned_diagram_elements`` allows you to discover the logical elements the diagram is tied to.


.. only:: html

    .. grid:: 2

        .. grid-item-card:: :fa:`arrow-left` Previous step
            :link: write-model
            :link-type: doc

            Write in your model

        .. grid-item-card:: Next step :fa:`arrow-right`
            :link: information
            :link-type: doc

            How to get some information
