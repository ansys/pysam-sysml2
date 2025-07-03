.. _C_I_Section:

Connector package
#################

.. note::

    To find all required data (Ids, token,..)  see :ref:`Here <Info_Section>`

AnsysSysML2APIConnector
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: ansys.sam.sysml2.api.ansys_sysml2_api_connector.AnsysSysML2APIConnector
   :members: __init__, get_projects,get_project_by_id,create_project,get_all_elements,get_element_by_id,get_root_elements,execute_query
   :undoc-members:
   :show-inheritance:


SamRestApiConnector
~~~~~~~~~~~~~~~~~~~

.. autoclass:: ansys.sam.sysml2.diagrams.api.sam_rest_api_connector.SamRestApiConnector
   :members: get_project_data,get_diagrams_info,get_single_diagram_info,get_diagram_image_as_svg,get_diagram_image_as_png,get_diagram_image_as_jpeg,get_all_diagram_image_from_project
   :undoc-members: