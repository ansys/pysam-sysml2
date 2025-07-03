.. _Create_C_Section:

Use a connector
##################


A connector is the interface between the library and the SysML V2 Server.


Connectors
==========

.. note::

    To find all required data (Ids, token,..) see :ref:`Here <Info_Section>`.

    Also, you can find classes specification :ref:`Here <C_I_Section>`.

Ansys SysML2 API Connector
--------------------------

It uses the Standard API to load and publish information in a model.

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 12-17
    :language: python
    :caption: Connect to the SysML2 API server

Sam Rest API Connector
----------------------

It uses the SAM REST API to retrieve diagrams in the model.

.. literalinclude:: ../../_static/code/download-diagrams.py
    :lines: 19-23
    :language: python
    :caption: Connect to the SAM REST API server

.. only:: html

    .. grid:: 2

        .. grid-item::



        .. grid-item-card:: Next step :fa:`arrow-right`
            :link: load-model
            :link-type: doc

            Load a model