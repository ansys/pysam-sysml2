Pysam sysml2
============
|pyansys| |python| |pypi| |GH-CI| |codecov| |MIT| |black|

.. |pyansys| image:: https://img.shields.io/badge/Py-Ansys-ffc107.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC
   :target: https://docs.pyansys.com/
   :alt: PyAnsys

.. |python| image:: https://img.shields.io/pypi/pyversions/ansys-sam-sysml2?logo=pypi
   :target: https://pypi.org/project/ansys-sam-sysml2/
   :alt: Python

.. |pypi| image:: https://img.shields.io/pypi/v/ansys-sam-sysml2.svg?logo=python&logoColor=white
   :target: https://pypi.org/project/ansys-sam-sysml2
   :alt: PyPI

.. |codecov| image:: https://codecov.io/gh/ansys/pysam-sysml2/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/ansys/pysam-sysml2
   :alt: Codecov

.. |GH-CI| image:: https://github.com/ansys/pysam-sysml2/actions/workflows/ci_cd.yml/badge.svg
   :target: https://github.com/ansys/pysam-sysml2/actions/workflows/ci_cd.yml
   :alt: GH-CI

.. |MIT| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
   :alt: MIT

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat
   :target: https://github.com/psf/black
   :alt: Black


Overview
--------

Python library for SysML2 model manipulation

Getting started
===============

This section's scope is about user installation.


ToDO
====

- [ ] Add Search function
- [ ] Add element["member"]
- [ ] Add Organization_name in connector
- [ ] Add manager.get_project_by_name
- [ ] Add Get Token with username-password

Dev Installation
----------------


#. Start by cloning this repository:

   .. code:: bash

      git clone https://github.com/ansys-internal/pysam-sysml2



#. Make sure you have the latest required build system and doc, testing, and CI tools:

   .. code:: bash

      python -m pip install -U pip flit tox
      python -m pip install -r requirements.txt


#. Finally, verify your development installation by running:

    .. code:: bash

        tox


Development
-----------

You can use tox to: run test, format code, add Copyrights, sort imports

Run tox to run everything :

.. code:: bash

   tox

or select the run with :

- Test :
   .. code:: bash

      tox -e py

- Formatting & Copyrights (pre-commit):
   .. code:: bash

      tox -e style


.. note::
    When you run pre-commit, you (style), it's will check for staged changes, if the pre-commit tools modify a file, you need to stage the changes before re-run tox.



Usage
-----

Create a connector
~~~~~~~~~~~~~~~~~~

Start a Python INterpreter and import PySam Package:

.. code:: python

    from ansys.sam import ConnectorFactory,SysMLModelManager

Next, create the connector for your tool. Here for SAM SysML2 API.

.. code:: python

    conn = ConnectorFactory.create_ansys_sysml_connector(
            server_url="https://sam-testing.ansys.com:9050",
            organization_id="<organization_id>",
            token=<token>,
            is_secure=False
            )

Load a model
~~~~~~~~~~~~

To load  a model, use SysMLModelManager()

.. code:: python

   model = SysMLModelManager(project_id="17a0fb7c-6236-4801-9746-e626eea78c01", connector=conn)


Access to model element
~~~~~~~~~~~~~~~~~~~~~~~

To access model element, you can use direct dot notation:


.. code:: python

   Bike.frame

Or call a SysML Basing function:


.. code:: python

      for part in Bike._ownedElement:
         print(part)


Check sysml type
~~~~~~~~~~~~~~~~

.. code:: python

   from ansys.sam import SysmlTools

   SysmlTools.isinstance(Bike,"PartUsage")
