PySam SysML2
#############

PySam SysML2 provides a Python scripting interface for SysML2 models. It loads models from any SysML2 tool that implements the standard API. The loaded model maps into a Python object, allowing you to manipulate, browse, and edit it. You can then push modifications back to your modeling tool.

PySam SysML2 works with the Ansys SysML2 modeling tool, `Ansys System Architecture Modeler (SAM) <https://www.ansys.com/products/connect/ansys-system-architecture-modeler>`_.

.. only:: html

    .. grid:: 4

        .. grid-item-card:: Getting started :fa:`play-circle`
            :link: getting_started/index
            :link-type: doc

            Shows how to install PySam SysML2 and set up a project, including loading and initializing it.

        .. grid-item-card:: User guide :fa:`compass`
            :link: user_guide/index
            :link-type: doc

            Explains how to interact with your project and model, from loading your model to writing data into it. This section also explains how to access and retrieve elements to manipulate and navigate your project.

        .. grid-item-card:: API reference :fa:`file-lines`
            :link: api/index
            :link-type: doc

            Describes PySam SysML2 functions, classes, and methods to help you use it effectively.

        .. grid-item-card:: Examples :fa:`code`
            :link: examples/index
            :link-type: doc

            Provides code snippets and scripts that demonstrate how to use the library in various scenarios. This section also shows how to access and modify your project and serves as references for common use cases.

.. toctree::
   :hidden:
   :maxdepth: 1

   getting_started/index
   user_guide/index
   api/index
   examples/index
   changelog.rst