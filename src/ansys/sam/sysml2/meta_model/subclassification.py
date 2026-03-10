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

"""Generated subclassification class from metamodel."""

from __future__ import annotations

from .specialization import Specialization


class Subclassification(Specialization):
    """Java class 'com.ansys.medini.metamodel.sysml.Subclassification'."""

    def __init__(self, id: str):
        """
        Construct new instance.

        Parameters
        ----------
        id : str
            Element ID.
        """
        super().__init__(id)

        self._subclassifier = None
        self._superclassifier = None
        self._owning_classifier = None

    @property
    def subclassifier(self) -> None:  # noqa: F821
        """
        Get the subclassifier property.

        Returns
        -------
        None
            Value of property subclassifier.
        """
        return self._subclassifier

    @subclassifier.setter
    def subclassifier(self, value: None):  # noqa: F821
        """
        Set the subclassifier property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "subclassifier", value)
        self._subclassifier = value

    @property
    def superclassifier(self) -> None:  # noqa: F821
        """
        Get the superclassifier property.

        Returns
        -------
        None
            Value of property superclassifier.
        """
        return self._superclassifier

    @superclassifier.setter
    def superclassifier(self, value: None):  # noqa: F821
        """
        Set the superclassifier property.

        Parameters
        ----------
        value: None
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "superclassifier", value)
        self._superclassifier = value

    @property
    def owning_classifier(self) -> "Classifier":  # noqa: F821
        """
        Get the owning classifier property.

        Returns
        -------
        "Classifier"
            Value of property owning classifier.
        """
        return self._owning_classifier

    @owning_classifier.setter
    def owning_classifier(self, value: "Classifier"):  # noqa: F821
        """
        Set the owning_classifier property.

        Parameters
        ----------
        value: "Classifier"
            New value.
        """
        if self._observer is not None:
            self._observer.notify(self.id, "owning_classifier", value)
        self._owning_classifier = value
