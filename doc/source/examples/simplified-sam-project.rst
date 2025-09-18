.. _Simplified_SAM_Example:

Simplify SAM project initialization
###################################

This example shows how to use the simplified
:class:`ansys.sam.sysml2.tools.ansys_sysml2_project.AnsysSysML2Project` class to work with a SysML v2 project on SAM. This approach reduces boilerplate code by automatically initializing all
necessary connectors. It explains how to perform these tasks:

- Simplify project initialization with a single class.
- Download diagrams (single and batch).
- Create new elements.
- Navigate through project diagrams.
- Retrieve diagram information.

.. note::

    The ``AnsysSysML2Project`` class is specifically designed for SAM projects and automatically handles the initialization of these classes: ``AnsysSysML2APIConnector``, ``SamRestApiConnector``,
    ``SysML2ProjectManager``, and ``SAMDiagramManager``.

Prerequisites for simplified SAM
================================

Ensure that you meet these prerequisites:

- A running SAM server instance.
- A valid organization ID, project ID, and token.
- The `bike.xmi` model imported into your project.

Simplified Python example
=========================

.. literalinclude:: ../_static/code/simplified-sam-project.py
    :language: python
    :caption: Simplified example using AnsysSysML2Project for SAM projects
    :linenos:

Key advantages
==============

Compared to the traditional approach described in (:ref:`Download diagrams and create new elements<Download_Example>`), using the simplified
:class:`ansys.sam.sysml2.tools.ansys_sysml2_project.AnsysSysML2Project` class offers these advantages:

- **Single initialization**: One class automatically handles all connectors.
- **Built-in diagram management**: Removes the need to manually create and manage the ``SAMDiagramManager`` class.
- **Streamlined API**: Provides direct access to project operations without managing multiple connector instances.
- **Integrated features**: Combines project management, diagram operations, and element creation in one interface.

.. note::

  - Replace placeholder values with your actual SAM configuration.
  - The ``AnsysSysML2Project`` class automatically manages diagram loading and the connector lifecycle.
  - The class supports all diagram formats (``png``, ``svg``, ``jpeg``) for downloads.