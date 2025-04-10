Load a model
############

To load a model, you need an instance of a SysML Connector (see :ref:`here <Create_C_Section>`).

After this, you can create a SysML2ProjectManager.
This class will help you to load model in Python, using the Sysml V2 Standard API.

.. code:: python

   model_manager = SysML2ProjectManager(connector=conn)


You can find information about this classes :ref:`here <PM_Section>`.

With this model manager, you can load project like this:

.. code:: python

   project = model_manager.get_project("ac00103a-8e4d-426d-bd5f-e1e6d360970c")


Once you got this project, you have a Python version of your model.

.. grid:: 2

    .. grid-item-card:: :fa:`arrow-left` Previous step
        :link: create_conn
        :link-type: doc

        Use a connector

    .. grid-item-card:: Next step :fa:`arrow-right`
        :link: read_model
        :link-type: doc

        Read a model