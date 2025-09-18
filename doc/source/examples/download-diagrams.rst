.. _Download_Example:

Download diagrams and create new elements
#########################################

This example shows how to work with the ``Bike`` model in a SysML v2 project using the Ansys SAM API. It explains how to perform these tasks:

- Load and download diagrams.
- Navigate and save diagram content.

.. note::

    If you have never used PySam SysML2 before, start with one of these simpler examples to understand how the library works:
    
    - :ref:`bike_weight<Bike_Example>`
    - :ref:`computer_cost<Computer_Example>`

Prerequisites
=============

Ensure that you meet these prerequisites:

- A running SAM server instance.
- A valid organization ID, project ID, and token.
- The `bike.xmi` model imported into a project.

Python example
==============

.. literalinclude:: ../_static/code/download-diagrams.py
    :language: python
    :caption: Work with diagrams using SAMDiagramManager
    :linenos:

.. note::

    - Replace placeholder values with your actual SAM configuration.
    - Always use the ``SAMDiagramManager`` class within a context manager (``with`` statement).
    - Retrieve diagram content in various formats, such as ``png`` and ``svg``.