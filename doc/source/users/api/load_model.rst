Load a model
############

To load a model, you need an instance of a SysML Connector (see :ref:`here <Create_C_Section>`).

After this, you can create a SysML2ProjectManager.
This class will help you to load a model in Python, using the Sysml V2 Standard API.

.. code:: python

   model_manager = SysML2ProjectManager(connector=conn)


You can find information about this class :ref:`here <PM_Section>`.

With this model manager, you can load your project like this:

.. code:: python

   project = model_manager.get_project("<Project ID>") #You can find it in the URL of the Editor


Once you got this project variable, you have a Python version of your model.

.. only:: html

    .. grid:: 2

        .. grid-item-card:: :fa:`arrow-left` Previous step
            :link: create_conn
            :link-type: doc

            Use a connector

        .. grid-item-card:: Next step :fa:`arrow-right`
            :link: read_model
            :link-type: doc

            Read a model