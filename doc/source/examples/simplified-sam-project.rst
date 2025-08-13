.. _Simplified_SAM_Example:

Simplified SAM project initialization
#####################################

This example demonstrates how to use the simplified
:class:`ansys.sam.sysml2.tools.ansys_sysml2_project.AnsysSysML2Project` class to work with a SysML
v2 project on SAM. This approach reduces boilerplate code by automatically initializing all
necessary connectors. It covers:

- Simplified project initialization with a single class.
- Downloading diagrams (single and batch).
- Creating new elements.
- Navigating through project diagrams.
- Retrieving diagram information.

.. note::

    The ``AnsysSysML2Project`` class is specifically designed for SAM projects and automatically
    handles the initialization of ``AnsysSysML2APIConnector``, ``SamRestApiConnector``,
    ``SysML2ProjectManager``, and ``SAMDiagramManager``.

Prerequisites for simplified SAM
================================

Ensure you have:

1. A running SAM server instance.
2. A valid **Organization ID**, **Project ID**, and **Token**.
3. The `bike.xmi` model imported into your project.

Simplified python example
=========================

.. literalinclude:: ../_static/code/simplified-sam-project.py
    :language: python
    :caption: Simplified example using AnsysSysML2Project for SAM projects
    :linenos:

Key advantages
==============

Compared to the traditional approach (:ref:`download_diagrams<Download_Example>`), this simplified
method offers:

- **Single initialization**: One class handles all connectors automatically.
- **Built-in diagram management**: No need to manually create and manage ``SAMDiagramManager``.
- **Streamlined API**: Direct access to project operations without managing multiple connector
  instances.
- **Integrated feature**: Combines project management, diagram operations, and element creation in
  one interface.

.. note::

    - Replace placeholder values with your actual SAM configuration.
    - The ``AnsysSysML2Project`` class automatically manages diagram loading and connector
      lifecycle.
    - All diagram formats (``png``, ``svg``, ``jpeg``) are supported for downloads.