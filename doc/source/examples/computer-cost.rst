.. _Computer_Example:

Computer example
################

A computer model is required to get started.

One is provided for your convenience.

Download this model : :download:`Computer Model <../_static/code/computer.xmi>`.

Open SAM Editor on your browser, and select the wanted organization (*MyOrga* for example).
Then, click **New Project** > **SysML V2** > **Import File**.
Click on **Choose File** in the **File to import** input, and select the ``computer.xmi`` file you just downloaded.
The name of the project is automatically set to ``computer``.
Click on `Import` and wait for the project to be loaded.

*Congratulations, you now have a computer model to work on !*


Calculate the computer cost
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

    You need to change `Organization ID`, `Server URL` and `Token` with your own data, see :ref:`this section for more information<Info_Section>`.

.. literalinclude:: ../_static/code/computer-cost.py
    :language: python
    :caption: Assessing system cost using recursive traversal
    :linenos: