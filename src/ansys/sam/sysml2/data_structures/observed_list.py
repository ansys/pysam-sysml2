# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
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

"""Observed List for SysMl List."""

from typing import Any

from ansys.sam.sysml2.classes.sysml_element import SysMLElement


def mount_observer_and_access(function):
    """
    Check write access and notify observer.

    Parameters
    ----------
    function : callable
        Function to watch
    """

    def wrapper(self, *args):
        """Wrapper to notify observer."""
        if self._owner._observer is not None:
            self._owner._observer.list_notify(self._owner._id, self._name, self)
        val = function(self, *args)
        return val

    return wrapper


class ObservedList(list):
    """React (Notification) on each list operation."""

    _content: list
    _name: str
    _owner: SysMLElement

    def __init__(self, owner: SysMLElement, name: str, *args):
        """Initialize class ObservedList.

        Parameters
        ----------
        owner : SysMLElement
            Owner of this list.
        name : str
            Name of the structural feature.(eg ownedElement)
        """
        if len(args) > 0:
            super().extend(args)
        self._owner = owner
        self._name = name

    @mount_observer_and_access
    def append(self, object: Any):
        """Override the list append method."""
        return super().append(object)

    @mount_observer_and_access
    def extend(self, iterable):
        """Override the list extend method."""
        return super().extend(iterable)

    @mount_observer_and_access
    def insert(self, index, object):
        """Override the list insert method."""
        return super().insert(index, object)

    @mount_observer_and_access
    def remove(self, value):
        """Override the list remove method."""
        return super().remove(value)

    @mount_observer_and_access
    def pop(self, index=-1):
        """Override the list pop method."""
        return super().pop(index)

    @mount_observer_and_access
    def reverse(self):
        """Override the list reverse method."""
        return super().reverse()

    @mount_observer_and_access
    def __iadd__(self, value):
        """Override the list __iadd__ method."""
        return super().__iadd__(value)

    @mount_observer_and_access
    def __imul__(self, value):
        """Override the list __imul__ method."""
        return super().__imul__(value)

    @mount_observer_and_access
    def __setitem__(self, key, value):
        """Override the list __setitem__ method."""
        return super().__setitem__(key, value)

    @mount_observer_and_access
    def __delitem__(self, key):
        """Override the list __delitem__ method."""
        return super().__delattr__(key)
