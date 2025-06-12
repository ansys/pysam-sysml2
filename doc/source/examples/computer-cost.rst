.. _Computer_Example:

Computer example
################

A computer model is required to get started.

One is provided for your convenience.

Download this model : `Computer Model </_static/code/computer.xmi>`_.

Open SAM Editor on your browser, and select the wanted organization (*MyOrga* for example).
Then, click **New Project** > **SysML V2** > **Import File**.
Click on **Choose File** in the **File to import** input, and select the ``computer.xmi`` file you just downloaded.
The name of the project is automatically set to ``computer``.
Click on `Import` and wait for the project to be loaded.

*Congratulations, you now have a computer model to work on !*


Calculate the computer cost
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

    You need to change `Organization ID`, `Server URL` and `Token` with your own data, see :ref:`This section for more information<Info_Section>`.

.. code:: python

    from ansys.sam.sysml2 import AnsysSysML2APIConnector, SysML2ProjectManager
    from ansys.sam.sysml2.tools import SysMLTools
    import requests
    from urllib3.exceptions import InsecureRequestWarning

    requests.packages.urllib3.disable_warnings(
        InsecureRequestWarning
    )

    conn = AnsysSysML2APIConnector(
        server_url="https://127.0.0.1:8443/", # Your Sam server base URL
        organization_id="<Orga ID>", # The Organization ID
        token="<Token>", # Your Auth Token (See section below)
        use_ssl=False # If the server has a valid SSL
    )

    model_manager = SysML2ProjectManager(connector=conn)

    project = model_manager.get_project("<Computer Project ID>") # You can find it in the URL of the Editor

    realSystems = project.get_root_package().RealSystems


    def assess_cost(element):
        if hasattr(element, "cost") and (
            element.cost.get_value() is not None):
            return element.cost.get_value()
        cost = 0
        for sub_element in element._ownedElement:
            if SysMLTools.isinstance(sub_element, "PartUsage"):
                cost += assess_cost(sub_element)
        return cost


    for system in realSystems._ownedElement:
        print(system._name, " : ", assess_cost(system))