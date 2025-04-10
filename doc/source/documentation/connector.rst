.. _C_I_Section:

Connector Package
#################

AnsysSysML2APIConnector
~~~~~~~~~~~~~~~~~~~~~~~

.. note::

    To find all required data (Ids, token,..)  see :ref:`Here <Info_Section>`

.. autoclass:: ansys.sam.sysml2.api.ansys_sysml2_api_connector.AnsysSysML2APIConnector
   :members: __init__, get_projects,get_project_by_id,create_project,get_all_elements,get_element_by_id,get_root_elements,execute_query,_build_endpoint,_add_authentication_field
   :undoc-members:
   :show-inheritance:



SysML2APIConnector
~~~~~~~~~~~~~~~~~~

This is the interface for all Sysml V2 Api Connector


.. autoclass:: ansys.sam.sysml2.api.sysml2_api_connector.SysML2APIConnector
   :members: get_projects,get_project_by_id,create_project,get_all_elements,get_element_by_id,get_root_elements,execute_query
   :undoc-members:


