.. _Create_C_Section:

Use a connector
###############

A connector is the interface between PySAM SysML2 and the SysML V2 server.

.. note::

    To find all required data, such as organization IDs and tokens, see
    :ref:`Find information <Info_Section>`.

Ansys SysML2 API Connector
--------------------------

PySAM SysML2 uses the standard API to load and publish information in a model.

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 35-40
    :language: python
    :caption: Connect to the SysML2 API server

The ``SysML2APIConnector`` class is typically used with project managers for high-level access. However, it also provides direct access to the SysML2 API entry points through the following methods:

* ``get_projects()``: Returns all projects of the connected user.
* ``get_project_by_id(project_id)``: Returns project information for the given ID.
* ``create_project(project_name, project_description)``: Creates a project with the specified name and description.
* ``get_all_elements(project_id)``: Returns all elements of the given project.
* ``get_element_by_id(project_id, element_id)``: Returns element information for the given project and element IDs.
* ``get_root_elements(project_id)``: Returns all root elements of the project.
* ``execute_query(project_id, query)``: Sends a query (in JSON format) to the standard API.
* ``create_commit(project_id, commit)``: Sends a commit (in JSON format) to the standard API.

SAM REST API Connector
----------------------

If you need to access diagrams and their associated elements (available only on Ansys servers), you can use the :class:`SamRestApiConnector <ansys.sam.sysml2.diagrams.api.sam_rest_api_connector.SamRestApiConnector>` connector.

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 42-46
    :language: python
    :caption: Connect to the SAM REST API server

The ``SamApiConnector`` class provides access to diagrams and diagram-related data (Ansys servers only) through the following methods:

* ``get_project_data(model_id)``: Returns project data from the SAM API using the project ID.
* ``get_diagrams_info(project_id)``: Returns metadata and information for all diagrams within a specific project.
* ``get_single_diagram_info(project_id, diagram_id)``: Returns detailed information for a single diagram within a project.
* ``get_diagram_image_as_svg(project_id, diagram_id)``: Downloads a diagram rendered as SVG format.
* ``get_diagram_image_as_png(project_id, diagram_id)``: Downloads a diagram rendered as PNG format.
* ``get_diagram_image_as_jpeg(project_id, diagram_id)``: Downloads a diagram rendered as JPEG format.
* ``get_all_diagram_image_from_project(project_id, file_format)``: Downloads all diagrams from a project as a compressed ZIP archive.

.. only:: html

    .. grid:: 2

        .. grid-item::

        .. grid-item-card:: Next step :fa:`arrow-right`
            :link: approaches
            :link-type: doc

            Dynamic vs static approaches