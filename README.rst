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

PySam SysML2 provides a Python scripting interface for SysML2 models. It loads models from any SysML2 tool that implements the standard API. The loaded model maps into a Python object, allowing you to manipulate, browse, and edit it. You can then push modifications back to your modeling tool.

PySam SysML2 works with the Ansys SysML2 modeling tool, `Ansys System Architecture Modeler (SAM) <https://www.ansys.com/products/connect/ansys-system-architecture-modeler>`_.

Prerequisites
=============

PySam SysML2 requires `Python <https://www.python.org/downloads/>`_ 3.10 or later.

Documentation
=============

The PySam SysML2 documentation includes four sections:

- `Getting started`_: Shows how to install PySam SysML2 and set up a project, including loading and initializing it.
- `User guide`_: Explains how to interact with your project and model, from loading your model to writing data into it. This section also explains how to access and retrieve elements to manipulate and navigate your project.
- `API reference`_: Describes PySam SysML2 functions, classes, and methods to help you use it effectively.
- `Examples`_: Provides code snippets and scripts that demonstrate how to use the library in various scenarios. This section also shows how to access and modify your project and serves as references for common use cases.

License
=======

The PySam SysML2 project uses the MIT license. Read the full text of the license in the `MIT <https://opensource.org/licenses/MIT/>`_ file.

.. _getting started: ...
.. _user guide: ...
.. _api reference: ...
.. _examples: ...