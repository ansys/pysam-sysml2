Computer Example
################

First of all, we need a computer model to work on!

Fortunately, we have one for you.

Download this model : `Computer Model </_static/code/computer.xmi>`_

Open SAM Editor on your browser, and switch to the good organization (*MyOrga* for example).
Then click on `New Project` > `SysMl V2` > `Import File`.
Click on `Choose File`  in the  `File to import` input, and select the `bike.xmi` file you just downloaded.
The name of the project will automatically be `computer`.
Click on `Import` and wait for the project to be loaded.

*✅ Congratulations, you now have a computer model to work on !*


Calculate the Computer cost
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's calculate the cost of the Computer.


.. note::

    You need to change organization id, Server Url, Token, with your own data, see :ref:`This section for more information<Info_Section>`

.. code:: python

    from ansys.sam.sysml2 import AnsysSysML2APIConnector, SysML2ProjectManager
    import requests
    from urllib3.exceptions import InsecureRequestWarning

    requests.packages.urllib3.disable_warnings(
        InsecureRequestWarning
    )

    token = "eyJraWQi..."


    conn = AnsysSysML2APIConnector(
        server_url="https://127.0.0.1:8443",
        organization_id="<Id>",
        token=token,
        use_ssl=False,
    )


    model_manager = SysML2ProjectManager(connector=conn)

    project = model_manager.get_project("c22d73ac-470c-47c6-ad59-dbad31c600e1")

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