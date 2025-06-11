.. _Bike_Example:

Bike Example
#############

First of all, we need a bike model to work on!

Fortunately, we have one for you.

Download this model : `Bike Model </_static/code/bike.xmi>`_.

Open SAM Editor on your browser, and select the wanted organization (*MyOrga* for example).
Then, click on `New Project` > `SysMl V2` > `Import File`.
Click on `Choose File`  in the  `File to import` input, and select the `bike.xmi` file you just downloaded.
The name of the project will automatically set to `bike`.
Click on `Import` and wait for the project to be loaded.

*✅ Congratulations, you now have a bike model to work on !*



Calculate the Bike weight
~~~~~~~~~~~~~~~~~~~~~~~~~

Let's calculate the weight of the bike.

When we look at the model, we can see that the weight of the bike is the sum of the weight of the frame and the weight of all elements of the wheel components.

.. note::

    In this case, we want to calculate the sum of all blue elements of the model:

.. figure:: /_static/images/weight-bike.png



Step 1: Load the project
------------------------

.. note::

    We suppose that you have already installed the Library. If not, please refer to the :ref:`Installation <Installation_Section>` section.

Before loading our project, we need to create a Connector and a Project Manager.

See section  :ref:`Organization Id <Info_O_Id_Section>` and :ref:`Bearer Token <Info_B_Token_Section>` to know how to get the required data.



.. code:: python

   # Import Connector and Model Manager
    from ansys.sam.sysml2 import SysML2ProjectManager,AnsysSysML2APIConnector

    # Create your connector for the Sam Server
    connector = AnsysSysML2APIConnector(
        server_url="https://127.0.0.1:8443/", # Your Sam server base URL
        organization_id="<Orga ID>", # The Organization ID
        token="<Token>", # Your Auth Token (See section below)
        use_ssl=False # IF the server has a valid SSL
    )

    project_manager = SysML2ProjectManager(connector=connector)


Now, that you are logged in, you can load the project `bike`.

.. note::

    To load a project, we need his ID. You can find it in the URL of the Editor.


.. code:: python

   myBikeProject = project_manager.get_project("<Bike Project ID>")


`myBikeProject` is the project we will work on. See the :ref:`loaded project <L_Project>` section for more details about the project object.




Step 2: Calculate the weight
----------------------------

Now that we have loaded the project, we can calculate the weight of the bike.

Let's get the Bike element!


.. note::

    There are many ways to get an element, here we will use the dot notation. See the :ref:`Getter <Getter>` section for more details.


.. code:: python

   # Then we can use the following code to get the PartDefinition of the bike
   bike = myBikeProject.get_root_package().Structure.Bike


For weight calculation, nothing more simpler than simple addition!

.. .. note::

..     For access to different elements, we will use another method, dot notation. See the :ref:`Getter <Getter>` section for more details.

So, if we look at each piece of the bike, we have:


.. figure:: /_static/images/bike-access.png

And to get the weight of each piece, we just need to use the `weight` accessor, with the dot notation.

We use the int() function to cast the value to int.



.. code:: python

    bike_weight = (
        bike.frontWheel.rim.weight.get_value()[0]
        + bike.frontWheel.tire.weight.get_value()[0]
        + bike.rearWheel.rim.weight.get_value()[0]
        + bike.rearWheel.tire.weight.get_value()[0]
        + bike.frame.weight.get_value()[0]
    )

And let's print the weight of the bike!


.. code:: python

   print(bike_weight)


✅ You have now the total weight of the bike!


.. note::

    📄 You can get the full code `Here </_static/code/weight-bike.py>`_.