PySam SysML2
============
|pyansys| |GH-CI| |black| |MIT|

.. .. |python| |pypi| |codecov|

.. |pyansys| image:: https://img.shields.io/badge/Py-Ansys-ffc107.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC
   :target: https://docs.pyansys.com/
   :alt: PyAnsys

.. .. |python| image:: https://img.shields.io/pypi/pyversions/ansys-sam-sysml2?logo=pypi
..    :target: https://pypi.org/project/ansys-sam-sysml2/
..    :alt: Python

.. .. |pypi| image:: https://img.shields.io/pypi/v/ansys-sam-sysml2.svg?logo=python&logoColor=white
..    :target: https://pypi.org/project/ansys-sam-sysml2
..    :alt: PyPI

.. .. |codecov| image:: https://codecov.io/gh/ansys/pysam-sysml2/branch/main/graph/badge.svg
..    :target: https://codecov.io/gh/ansys/pysam-sysml2
..    :alt: Codecov

.. |GH-CI| image:: https://github.com/ansys-internal/pysam-sysml2/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/ansys-internal/pysam-sysml2/actions/workflows/ci.yml
   :alt: GH-CI

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat
   :target: https://github.com/psf/black
   :alt: Black

.. |MIT| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
   :alt: MIT License

Overview
========

PySam provides a Python scripting interface for SysML2 models.
You can load models from any SysML2 tools who provide an implementation of the standard API.
The loaded model is mapped into Python object.
So you can manipulate models, browse through them, edit them, and push the modification inside your modeling tool.

This library intends to work first with `SAM <https://www.ansys.com/products/connect/ansys-system-architecture-modeler>`_, the SysML2 modeling tool of Ansys.

Prerequisites
=============

PySam SysML2 requires `Python <https://www.python.org/downloads/>`_  with at least the 3.10 version installed.

Documentation
=============

There are four different parts in our web documentation:

1. `Getting started`_.
The Getting Started section provides all the necessary information to install the `pysam-sysml2` library.
It also includes a quick tutorial to help you set up your PySam project, along with everything required to load and initialize a project properly.

2. `User guide`_.
The User Guide offers step-by-step instructions on how to interact with your project and model — from loading your model to writing data into it.
It also explains how to access and retrieve the necessary elements to effectively manipulate and navigate your project.

3. `Documentation`_.
The Documentation section presents a detailed overview of the key classes and methods that power the `pysam-sysml2` library.
Each component is fully documented to help you understand its purpose.

4. `Examples`_.
The Examples section provides practical code snippets and complete scripts demonstrating how to use the library in various scenarios.
These examples illustrate how to access, and modify your project, and serve as a reference for common use cases.

License
=======

The license of the PySam SysML2 project is MIT. Read the full text of the license
in the `MIT <https://opensource.org/licenses/MIT/>`_ file.

.. _getting started: ...
.. _user guide: ...
.. _api reference: ...
.. _examples: ...