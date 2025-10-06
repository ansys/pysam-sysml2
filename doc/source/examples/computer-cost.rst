.. _Computer_Example:

Calculate computer cost
#######################

Download the computer model used in this example and import it into a new project to work on.

#. Download the model: :download:`Computer Model <../_static/code/computer.xmi>`.

#. Open the SAM editor in your browser and select the desired organization (for example, *MyOrga*).

#. Select **New Project** > **SysML V2** > **Import File**.

#. Select **Choose File** for the **File to import** option.

#. Select the ``computer.xmi`` file that you just downloaded. The project name is automatically set to ``computer``.

#. Click **Import** and wait for the project to load.

You can now work on this computer model.


Calculate cost
~~~~~~~~~~~~~~

.. note::

    You need to replace the organization ID, server URL, and token with your own data. For more information, see :ref:`Find information<Info_Section>`.

.. literalinclude:: ../_static/code/computer-cost.py
    :language: python
    :caption: Calculate computer cost using recursive traversal
    :linenos: