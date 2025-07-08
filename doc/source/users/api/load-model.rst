Load a model
############

To load a model, you need an instance of a SysML Connector (see :ref:`here <Create_C_Section>`).

After this, you can create a SysML2ProjectManager.
This class helps you load a model in Python, using the SysML V2 Standard API.

.. literalinclude:: ../../_static/code/computer-cost.py
    :lines: 19
    :language: python
    :caption: Create SysML2 Project Manager

You can find information about this class :ref:`here <PM_Section>`.

With this project manager, you can load your project like this:

.. literalinclude:: ../../_static/code/computer-cost.py
    :lines: 21-23
    :language: python
    :caption: Get the Project using Project ID

Once you got this project variable, you have a Python version of your model.

.. only:: html

    .. grid:: 2

        .. grid-item-card:: :fa:`arrow-left` Previous step
            :link: create-conn
            :link-type: doc

            Use a connector

        .. grid-item-card:: Next step :fa:`arrow-right`
            :link: read-model
            :link-type: doc

            Read a model