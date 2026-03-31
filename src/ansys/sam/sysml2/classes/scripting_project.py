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

"""Scripting project interface for users."""

from abc import ABC, abstractmethod
from typing import List

from ansys.sam.sysml2.classes.sysml_element import SysMLElement


class ScriptingProject(ABC):
    """Scripting project interface for users."""

    @property
    def root(self) -> List[SysMLElement]:
        """Get a list of root packages."""
        return self.get_root()

    @property
    def name(self) -> str:
        """Get the project name."""
        return self.get_name()

    @property
    def root_package(self) -> SysMLElement:
        """Get the root package."""
        return self.get_root_package()

    @abstractmethod
    def get_name(self) -> str:
        """Get the project name."""

    @abstractmethod
    def get_root(self) -> List[SysMLElement]:
        """Get a list of root packages."""

    @abstractmethod
    def get_root_package(self) -> SysMLElement:
        """Get the root package."""

    @abstractmethod
    def find_element_by_id(self, element_id: str) -> SysMLElement:
        """
        Find an element by ID.

        Parameters
        ----------
        element_id : str
            Element ID.

        Returns
        -------
        SysMLElement
            Element retrieved.
        """

    @abstractmethod
    def find_elements_by_name(self, element_name: str) -> List[SysMLElement]:
        """
        Find all elements by name.

        Parameters
        ----------
        element_name : str
            Name of elements.

        Returns
        -------
        List[SysMLElement]
            List of elements retrieved.
        """

    @abstractmethod
    def start_transactional_mode(self):
        """
        Start a transactional mode for model edition.

        This method will stop direct update for the model,
        and register all changes until you commit or stop the transactional mode.

        Warning, all calculated modifications will not be applied,
        until the commit of all changes.
        """

    @abstractmethod
    def stop_transactional_mode(self):
        """
        Stop the current transaction.

        This method will close the current transaction and commit all changes to the server.
        """
