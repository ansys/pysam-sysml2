.. _Bike_Example:

Calculate bike weight
#####################

Download the bike model used in this example and import it into a new project to work on.

#. Download the model: :download:`Bike Model <../_static/code/bike.xmi>`.

#. Open the SAM editor in your browser and select the desired organization (for example, *MyOrga*).

#. Select **New Project** > **SysML V2** > **Import File**.

#. Select **Choose File** for the **File to import** option.

#. Select the ``bike.xmi`` file that you just downloaded. The project name is automatically set to ``bike``.

#. Click **Import** and wait for the project to load.

You can now work on this bike model.

Calculate weight
~~~~~~~~~~~~~~~~

The bike weight is the sum of the frame weight and the weight of all wheel component elements. Thus, you want to calculate the sum of all blue elements in the model:

.. figure:: /_static/images/weight-bike.png

Step 1: Load the project
------------------------

.. note::

    Ensure that you have installed PySam SysML. If not, see :ref:`Installation <Installation_Section>`.

Before loading the project, create a connector and a project manager.

To obtain the required data, see :ref:`Find organization ID <Info_O_Id_Section>` and :ref:`Find bearer token <Info_B_Token_Section>`.

.. literalinclude:: ../_static/code/weight-bike.py
    :lines: 3-18
    :language: python
    :caption: Import libraries and create a connection to the SysML2 API server

After logging in, load the ``bike`` project.

.. note::

    To load a project, you need its ID. Find it in the editor's URL.

.. literalinclude:: ../_static/code/weight-bike.py
    :lines: 22
    :language: python
    :caption: Load the bike project

For more information about the project object, see :class:`Project <ansys.sam.sysml2.classes.project.Project>` in the API reference documentation.

Step 2: Calculate bike weight
-----------------------------

After loading the project, get the ``Bike`` element. As explained in :ref:`Access methods <Getter>`, there are many ways to get an element. This code uses dot notation:

.. literalinclude:: ../_static/code/weight-bike.py
    :lines: 26
    :language: python
    :caption: Get the bike element from the project structure

To calculate the bike weight, sum the weight of all blue elements in the model:

.. figure:: /_static/images/bike-access.png

To get the weight of each piece, use the ``weight`` attribute with dot notation:

.. literalinclude:: ../_static/code/weight-bike.py
    :lines: 28-34
    :language: python
    :caption: Calculate total bike weight by summing component weights

Print the bike weight:

.. literalinclude:: ../_static/code/weight-bike.py
    :lines: 35
    :language: python
    :caption: Print the calculated bike weight

You now have the total bike weight.

.. note::

    :download:`Download <../_static/code/weight-bike.py>` the full code.