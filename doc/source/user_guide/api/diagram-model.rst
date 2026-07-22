Work with diagrams
##################

.. warning::

    Functionalities for downloading diagrams are available only for
    projects of type ``SAM``.

This page explains how to download diagrams from your SysML v2 project using
the SAM API.

Download diagrams
=================

Before downloading diagrams, create a
:class:`SamApiConnector <ansys.sam.sysml2.diagrams.api.sam_api_connector.SamApiConnector>`:

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 41-45
    :language: python
    :caption: Create a SAM API connector

Then instantiate a
:class:`SamDiagramDownloader <ansys.sam.sysml2.diagrams.tools.sam_diagram_downloader.SamDiagramDownloader>`
object:

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 59
    :language: python
    :caption: Create a SAM diagram downloader

Download all diagrams
---------------------

Download all diagrams and save them into a ZIP archive:

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 69-74
    :language: python
    :caption: Download all diagrams with custom parameters

**Default parameters**

If you do not specify parameters, these defaults are used to format and name your download archive:

- ``file_format``: ``"SVG"``
- ``filename``: ``"<PackageName>_<FileFormat>_diagrams.zip"``

Get and download a single diagram
---------------------------------

List the available diagrams with ``get_diagrams_info``, pick one, and download it in a given format:

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 77-78
    :language: python
    :caption: Get a single diagram identifier

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 80-85
    :language: python
    :caption: Download this single diagram

Download diagrams in a loop
---------------------------

Retrieve the diagram information for the project:

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 55
    :language: python
    :caption: Get the diagrams information

Then iterate through the diagrams and download each one:

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 88-92
    :language: python
    :caption: Download diagrams in a loop

.. only:: html

    .. grid:: 2

        .. grid-item-card:: :fa:`arrow-left` Previous step
            :link: write-model
            :link-type: doc

            Write data to your model

        .. grid-item-card:: Next step :fa:`arrow-right`
            :link: information
            :link-type: doc

            Find information
