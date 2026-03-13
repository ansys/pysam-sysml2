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

SAM REST API Connector
----------------------

PySAM SysML2 uses the :class:`SamRestApiConnector <ansys.sam.sysml2.diagrams.api.sam_rest_api_connector.SamRestApiConnector>` to retrieve diagrams in the model.

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 42-46
    :language: python
    :caption: Connect to the SAM REST API server

.. only:: html

    .. grid:: 2

        .. grid-item::



        .. grid-item-card:: Next step :fa:`arrow-right`
            :link: load-model
            :link-type: doc

            Load a model