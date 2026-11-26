.. _Download_Example:

Download diagrams and create new elements
#########################################

This example shows how to work with the ``Bike`` model in a SysML v2 project using the
Ansys SAM API. It explains how to perform these tasks:

- Load and download diagrams.
- Navigate and save diagram content.

.. note::

    If you have never used PySAM SysML2 before, start with one of these simpler examples to
    understand how this library works:

    - :ref:`Calculate bike weight<Bike_Example>`
    - :ref:`Calculate computer cost<Computer_Example>`

Prerequisites
=============

Ensure that you meet these prerequisites:

- A running SAM server instance.
- A valid organization ID, project ID, and token.
- The ``bike.xmi`` model imported into a project.

Python example
==============

.. tab-set::

    .. tab-item:: Dynamic approach

        .. literalinclude:: ../_static/code/download-diagrams.py
            :language: python
            :caption: Work with diagrams using SAMDiagramManager
            :linenos:

    .. tab-item:: Static approach

        .. literalinclude:: ../_static/code/download-diagrams-static.py
            :language: python
            :caption: Work with diagrams using SAMDiagramManager
            :linenos:

.. note::

    - Replace placeholder values with your actual SAM configuration.
    - Always use the
      :class:`SAMDiagramManager <ansys.sam.sysml2.diagrams.sam_diagram_manager.SAMDiagramManager>`
      class within a context manager (``with`` statement).
    - Retrieve diagram content in various formats, such as ``png`` and ``svg``.
