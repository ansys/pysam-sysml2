Load a model
############

To load a model, you need an instance of a SysML Connector. For more information, (see :ref:`Use a connector <Create_C_Section>`).

You can then create an instance of the :class:`SysML2ProjectManager <ansys.sam.sysml2.builder.sysml2_project_manager.SysML2ProjectManager>` class.
This class helps you load a model in Python, using the SysML V2 standard API.

.. literalinclude:: ../../_static/code/computer-cost.py
    :lines: 19
    :language: python
    :caption: Create a SysML2 project manager instance

For more information, see the :class:`SysML2ProjectManager <ansys.sam.sysml2.builder.sysml2_project_manager.SysML2ProjectManager>` class.

With the project manager, you can load your project like this:

.. literalinclude:: ../../_static/code/computer-cost.py
    :lines: 21-23
    :language: python
    :caption: Get the project using the project ID

Once you provide the project ID, you get a Python version of your model.

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