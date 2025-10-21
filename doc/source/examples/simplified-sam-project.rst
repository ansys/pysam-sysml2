.. _Simplified_SAM_Example:

Simplify SAM project initialization
###################################

This example shows how to use the simplified
:class:`AnsysSysML2Project <ansys.sam.sysml2.tools.ansys_sysml2_project.AnsysSysML2Project>` class
to work with a SysML v2 project on SAM. This approach reduces boilerplate code by automatically
initializing all necessary connectors. It explains how to perform these tasks:

- Simplify project initialization with a single class.
- Download diagrams (single and batch).
- Create new elements.
- Navigate through project diagrams.
- Retrieve diagram information.

.. note::

    The
    :class:`AnsysSysML2Project <ansys.sam.sysml2.tools.ansys_sysml2_project.AnsysSysML2Project>`
    class is specifically designed for SAM projects and automatically handles the initialization
    of these classes:
    :class:`AnsysSysML2APIConnector <ansys.sam.sysml2.api.ansys_sysml2_api_connector.AnsysSysML2APIConnector>`,
    :class:`SamRestApiConnector <ansys.sam.sysml2.diagrams.api.sam_rest_api_connector.SamRestApiConnector>`,
    :class:`SysML2ProjectManager <ansys.sam.sysml2.builder.sysml2_project_manager.SysML2ProjectManager>`,
    and :class:`SAMDiagramManager <ansys.sam.sysml2.diagrams.sam_diagram_manager.SAMDiagramManager>`.

Prerequisites for simplified SAM
================================

Ensure that you meet these prerequisites:

- A running SAM server instance.
- A valid organization ID, project ID, and token.
- The ``bike.xmi`` model imported into your project.

Simplified Python example
=========================

.. literalinclude:: ../_static/code/simplified-sam-project.py
    :language: python
    :caption: Simplified example using AnsysSysML2Project for SAM projects
    :linenos:

Key advantages
==============

Compared to the traditional approach described in
:ref:`Download diagrams and create new elements<Download_Example>`, using the simplified
:class:`AnsysSysML2Project <ansys.sam.sysml2.tools.ansys_sysml2_project.AnsysSysML2Project>` class
offers these advantages:

- **Single initialization**: One class automatically handles all connectors.
- **Built-in diagram management**: Removes the need to manually create and manage the
  :class:`SAMDiagramManager <ansys.sam.sysml2.diagrams.sam_diagram_manager.SAMDiagramManager>`
  class.
- **Streamlined API**: Provides direct access to project operations without managing multiple
  connector instances.
- **Integrated features**: Combines project management, diagram operations, and element creation in
  one interface.

.. note::

  - Replace placeholder values with your actual SAM configuration.
  - The :class:`AnsysSysML2Project <ansys.sam.sysml2.tools.ansys_sysml2_project.AnsysSysML2Project>`
    class automatically manages diagram loading and the connector lifecycle.
  - The class supports all diagram formats (``png``, ``svg``, ``jpeg``) for downloads.