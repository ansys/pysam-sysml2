Getting started
===============

This section's scope is about user installation.


.. _Installation_Section:

Installation
-------------


.. code:: bash

    python -m pip install ansys_sam_sysml2-<version>-py3-none-any.whl


Use
---

.. note::

    You can find examples :ref:`here <Example>`.

Connect to the tool
~~~~~~~~~~~~~~~~~~~

Here, the AnsysSysML2 API Connector is used. If you want to connect to any other SysMLV2 tool, please read the developer guide.

.. literalinclude:: ../_static/code/weight-bike.py
    :lines: 5
    :language: python
    :caption: Import the Connector and the Project manager

The connector provides the project manager with access to the model.

Then create the connector :

.. literalinclude:: ../_static/code/weight-bike.py
    :lines: 11-16
    :language: python
    :caption: Connect to the SysML2 API server

Then, you can create the project manager and load a project:

.. literalinclude:: ../_static/code/weight-bike.py
    :lines: 18-20
    :language: python
    :caption: Create the project manager and load a project
