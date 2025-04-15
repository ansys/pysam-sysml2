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

"""Feature Helper Module."""

from ansys.sam.sysml2.dto.commit.commit_class import Commit
from ansys.sam.sysml2.dto.commit.data_version import DataVersion


class FeatureHelper:
    """Feature Helper Class."""

    @staticmethod
    def create_value(element, type_v, value):
        """
        Create a new value into the Feature.

        Parameters
        ----------
        element : SysMLElement
            The Feature element
        type_v : str
            Type of the Value
        value : Any
            The value
        """
        project_id = element._observer._project_id
        commit = Commit(project_id)
        change = DataVersion()
        change.add_change("@type", "FeatureValue")
        if type_v != "operator":
            change.add_change("value", FeatureHelper._adapt_value(value))
        else:
            change.add_change("value", value)
        change.add_change("owner", element)
        commit.add_change(change)
        element._observer._connector.create_commit(project_id, commit.to_json())
        element._observer.reload_project()

    @staticmethod
    def _adapt_value(value):
        """
        Convert the Value to JSON Format.

        Parameters
        ----------
        value : Any
            The Value

        Returns
        -------
        Any
            The value adapted to JSON
        """
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, str):
            return f'"{value}"'
        else:
            return str(value)
