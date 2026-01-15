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
"""File management utilities for diagram operations."""

from pathlib import Path
from typing import Union

import requests


class FileManager:
    """Handles file operations and path management."""

    @staticmethod
    def save_binary_content(
        content: bytes, path: Union[str, Path], filename: str, file_format: str
    ) -> Path:
        """
        Save binary content to a file.

        Parameters
        ----------
        content : bytes
            Binary content to write.
        path : str or Path
            Path to a file or directory.
        filename : str
            Name of the file to save.
        file_format : str
            Format requested.

        Returns
        -------
        Path
            Path where the file was saved.
        """
        if not filename.endswith(f".{file_format}"):
            filename = f"{filename}.{file_format}"

        file_path = FileManager.resolve_file_path(path, filename)
        FileManager.ensure_directory_exists(file_path.parent)

        with file_path.open("wb") as f:
            f.write(content)

        return file_path

    @staticmethod
    def save_response_content(
        response: requests.Response, path: Union[str, Path], filename: str
    ) -> Path:
        """
        Save streamed response content to a file.

        Parameters
        ----------
        response : requests.Response
            Response object containing the streamed data.
        path : str or Path
            Path to a file or directory.
        filename : str
            Name of the file to save.

        Returns
        -------
        Path
            Path where the file was saved.
        """
        file_path = FileManager.resolve_file_path(path, filename)
        FileManager.ensure_directory_exists(file_path.parent)

        with file_path.open("wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        return file_path

    @staticmethod
    def resolve_file_path(path: Union[str, Path], filename: str) -> Path:
        """
        Resolve a valid file path from the given path and default filename.

        If a file is specified, use its parent directory and concatenate with the filename.

        Parameters
        ----------
        path : str or Path
            Directory or file path.
        filename : str
            Default filename if path is a directory
            or filename to use with parent directory if path is a file.

        Returns
        -------
        Path
            Resolved file path.

        Raises
        ------
        ValueError
            If the path cannot be resolved properly.
        """
        if not path or (isinstance(path, str) and path.strip() == ""):
            raise ValueError("Cannot resolve path: Empty or invalid path is provided.")

        path = Path(path)

        if path.is_dir() or (not path.suffix and not path.exists()):
            FileManager.ensure_directory_exists(path)
            return path / filename

        if path.suffix or path.exists():
            parent_dir = path.parent
            FileManager.ensure_directory_exists(parent_dir)
            return parent_dir / filename

        FileManager.ensure_directory_exists(path)
        return path / filename

    @staticmethod
    def ensure_directory_exists(directory_path: Path) -> None:
        """
        Ensure that a directory exists. Create it if needed.

        Parameters
        ----------
        directory_path : Path
            Directory to check or create.
        """
        directory_path.mkdir(parents=True, exist_ok=True)
