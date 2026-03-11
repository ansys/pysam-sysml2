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

import pytest

from ansys.sam.sysml2.builder.classes.project_impl import ProjectImpl
from ansys.sam.sysml2.observer.observer import ModificationObserver


class TestObserver:

    @pytest.fixture
    def observer(self) -> ModificationObserver:
        return ModificationObserver(ProjectImpl("", ""), None)

    def test_transactional_mode_for_notify(self, observer: ModificationObserver):
        observer.set_transactional_mode(True)
        observer.notify("id", "name", "New Name")

        assert "id" in observer._stack
        assert observer._stack["id"] == [("name", "New Name")]

    def test_transactional_mode_for_list(self, observer: ModificationObserver):
        observer.set_transactional_mode(True)
        observer.list_notify("id", "definition", ["t", "t"])

        assert "id" in observer._stack
        assert observer._stack["id"] == [("definition", ["t", "t"])]

    def test_transactional_mode_for_delete(self, observer: ModificationObserver):
        observer.set_transactional_mode(True)
        observer.delete_element("id")

        assert "id" in observer._stack
        assert len(observer._stack["id"]) == 0
