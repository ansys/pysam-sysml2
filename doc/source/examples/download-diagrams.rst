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

.. literalinclude:: ../_static/code/download-diagrams.py
    :language: python
    :caption: Example of working with diagrams using SAMDiagramManager
    :linenos:

.. note::

    - Replace placeholder values with your actual SAM configuration.
    - Always use ``SAMDiagramManager`` within a context manager (``with`` statement).
    - Diagram content can be retrieved in various formats: ``png``, ``svg``, etc.