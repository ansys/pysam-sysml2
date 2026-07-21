# Copyright (C) 2024 - 2026 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Base module for PySAM SysML2."""

# Version
# ------------------------------------------------------------------------------

import importlib.metadata as importlib_metadata

__version__ = importlib_metadata.version(__name__.replace(".", "-"))
"""PySAM SysML2 version."""

# Ease import statements
# ------------------------------------------------------------------------------


from ansys.sam.sysml2.api.ansys_sysml2_api_connector import (  # noqa: F401, E402 as we export name
    AnsysSysML2APIConnector,
)
from ansys.sam.sysml2.builder.sysml2_project_manager import (  # noqa: F401, E402 as we export name
    SysML2ProjectManager,
)

# IPython completer patch
# ------------------------------------------------------------------------------


def _complete_element_attrs(obj, prev_completions):
    """Return the element's own ``__dir__`` so conditional gating wins over IPython ``dir2()``."""
    try:
        return list(obj.__dir__())
    except Exception:
        return prev_completions


def _patch_completer():
    """Disable Jedi, enable greedy completion, and make IPython honor the element ``__dir__``."""
    try:
        ip = get_ipython()  # noqa: F821
    except NameError:
        return
    if ip is None:
        return
    ip.Completer.use_jedi = False
    ip.Completer.greedy = True
    try:
        from IPython.utils.generics import complete_object

        from ansys.sam.sysml2.classes.sysml_element import SysMLElement
        from ansys.sam.sysml2.meta_model.e_object import EObject
    except ImportError:
        return
    register = getattr(complete_object, "register", None)
    if register is None:
        register = complete_object.when_type
    register(SysMLElement, _complete_element_attrs)
    register(EObject, _complete_element_attrs)


_patch_completer()
