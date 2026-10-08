# Copyright (C) 2024 - 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

"""Unit tests for ProjectImpl root packages."""

import pytest

from ansys.sam.sysml2.builder.classes.project_impl import ProjectImpl
from ansys.sam.sysml2.meta_model.element import Element
from ansys.sam.sysml2.meta_model.namespace import Namespace
from ansys.sam.sysml2.meta_model.package import Package


def test_get_root_packages_returns_owned_member_packages():
    project = ProjectImpl("project-id", "project")
    root = Namespace("root")
    first = Package("pkg-1")
    second = Package("pkg-2")
    root.owned_member.extend([first, Element("other"), second])
    nested = Package("nested")
    package_root = Package("not-a-namespace-root")
    package_root.owned_member.append(nested)
    project._root = [root, package_root]

    assert project.get_root_packages() == [first, second]
    with pytest.warns(DeprecationWarning, match="get_root_packages"):
        assert project.get_root_package() is first
