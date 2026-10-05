Load a model
############

To load a model, you need an instance of a SysML2 Connector. For more information, (see :ref:`Use a connector <Create_C_Section>`).

You can then create an instance of the :class:`SysML2ProjectManager <ansys.sam.sysml2.builder.sysml2_project_manager.SysML2ProjectManager>` class.
This class helps you load a model in Python, using the SysML2 standard API.

.. literalinclude:: ../../_static/code/computer-cost.py
    :lines: 41
    :language: python
    :caption: Create a SysML2 project manager instance

For more information, see the :class:`SysML2ProjectManager <ansys.sam.sysml2.builder.sysml2_project_manager.SysML2ProjectManager>` class.


With the project manager, and the ID of the project you want, you can load two types of projects:

SysML2 project (Static approach)
================================

SysML2 projects use a Python-based metamodel, enabling static completion for all SysML2 properties.

.. code:: python

    project = project_manager.get_sysml_project(
        "<Computer Project ID>"
    )  # You can find your project ID in the URL of the editor.

Scripting project (Dynamic approach)
====================================

Scripting projects use a dynamic class generation approach. This offers flexibility but does not provide autocompletion.

.. literalinclude:: ../../_static/code/computer-cost.py
    :lines: 43-45
    :language: python
    :caption: Get the project using the project ID

Both of the approaches give you a Python version of your model.

See :ref:`Approaches dynamic and static <Approaches_Section>` for more information about the differences between these approaches and when to use each of them.

.. only:: html

    .. grid:: 2

        .. grid-item-card:: :fa:`arrow-left` Previous step
            :link: approaches
            :link-type: doc

            Dynamic vs static approaches

        .. grid-item-card:: Next step :fa:`arrow-right`
            :link: read-model
            :link-type: doc

            Read a model