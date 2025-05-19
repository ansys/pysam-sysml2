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
"""DiagramElement data class."""

from pathlib import Path
from typing import Union


class DiagramElement:
    """DiagramElement Class."""

    _id: str

    def __init__(self, id: str):
        """
        Construct a new Diagram instance.

        Parameters
        ----------
        id : str
            Diagram identifier.
        """
        self._id = id

    def get_content(self, file_format: str) -> bytes:
        """
        Retrieve the diagram content in the specified format.

        Parameters
        ----------
        file_format : str
            Desired file format (e.g., 'png', 'svg').

        Returns
        -------
        bytes
            Binary content of the diagram.
        """

    def download_diagram(self, file_format: str, path: Union[str, Path]) -> dict:
        """
        Download and save this diagram to disk.

        Parameters
        ----------
        file_format : str
            Format to download the diagram in.
        path : str or Path
            Directory or file path to save the diagram.

        Returns
        -------
        dict
            Status and message about the download result.
        """
