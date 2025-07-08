.. _Bike_Example:

Bike example
############

First of all, a bike model is required to work on.

Fortunately, one is provided for you.

Download this model : :download:`Bike Model <../_static/code/bike.xmi>`.

Open SAM Editor on your browser, and select the wanted organization (*MyOrga* for example).
Then, click **New Project** > **SysML V2** > **Import File**.
Click on **Choose File** in the **File to import** input, and select the ``bike.xmi`` file you just downloaded.
The name of the project is automatically set to ``bike``.
Click on **Import** and wait for the project to be loaded.

*Congratulations, you now have a bike model to work on*



Calculate the bike weight
~~~~~~~~~~~~~~~~~~~~~~~~~

Calculate the weight of the bike.

When looking at the model, the weight of the bike is the sum of the weight of the frame and the weight of all elements of the wheel components.

.. note::

    In this case, calculate the sum of all blue elements of the model:

.. figure:: /_static/images/weight-bike.png



Step 1: Load the project
------------------------

.. note::

    This assumes that you have already installed the Library. If not, please refer to the :ref:`Installation <Installation_Section>` section.

Before loading the project, create a Connector and a Project Manager.

See section  :ref:`Organization Id <Info_O_Id_Section>` and :ref:`Bearer Token <Info_B_Token_Section>` to know how to get the required data.



.. literalinclude:: ../_static/code/weight-bike.py
    :lines: 3-18
    :language: python
    :caption: Import libraries and create connection to SysML2 API server


Now, that you are logged in, you can load the project ``bike``.

.. note::

    To load a project, its ID is needed. You can find it in the URL of the Editor.


.. literalinclude:: ../_static/code/weight-bike.py
    :lines: 22
    :language: python
    :caption: Get the bike project


``myBikeProject`` is the project to work on. See the :ref:`loaded project <L_Project>` section for more details about the project object.




Step 2: Calculate the weight
----------------------------

Now that the project has been loaded, calculate the weight of the bike.

Get the Bike element.


.. note::

    There are many ways to get an element, here the dot notation is used. See the :ref:`Getter <Getter>` section for more details.


.. literalinclude:: ../_static/code/weight-bike.py
    :lines: 26
    :language: python
    :caption: Get the bike part definition from the project structure


For weight calculation, nothing more simpler than simple addition.

So, if looking at each piece of the bike:

.. figure:: /_static/images/bike-access.png

And to get the weight of each piece, just use the ``weight`` attribute, with the dot notation.


.. literalinclude:: ../_static/code/weight-bike.py
    :lines: 28-34
    :language: python
    :caption: Calculate total bike weight by summing component weights

And print the weight of the bike.


.. literalinclude:: ../_static/code/weight-bike.py
    :lines: 35
    :language: python
    :caption: Print the calculated bike weight


You now have the total weight of the bike.


.. note::

    You can get the full code :download:`Here <../_static/code/weight-bike.py>`.