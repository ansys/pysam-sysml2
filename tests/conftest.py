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

"""File  created on Mon Dec 09 2024."""

from pathlib import Path
import shutil

from mocked_server.mocked_server import MockedServer
import pytest

conftest_path = Path(__file__).resolve()
base_dir = conftest_path.parent / "mocked_server"
tmp_dir = conftest_path.parent / "tmp"

original_path = base_dir / "json"
backup_path = base_dir / "json_backup"


@pytest.fixture(scope="session", autouse=True)
def start_server():
    """
    Pytest calls this function once at the start of all tests.
    It backs up the mocked_server/json folder, starts the mock server,
    and restores the json folder when tests are finished.
    """
    server = MockedServer()
    create_projects_backup()
    create_tmp_dir()

    server.start_server()
    yield
    server.stop_server()

    delete_tmp_dir()
    restore_projects_backup()


def create_projects_backup():
    backup_path.parent.mkdir(parents=True, exist_ok=True)

    if backup_path.exists():
        shutil.rmtree(backup_path)

    shutil.copytree(original_path, backup_path)


def restore_projects_backup():
    if original_path.exists():
        shutil.rmtree(original_path)
    shutil.copytree(backup_path, original_path)

    shutil.rmtree(backup_path)


def create_tmp_dir():
    tmp_dir.mkdir(parents=True, exist_ok=True)


def delete_tmp_dir():
    if tmp_dir.exists():
        shutil.rmtree(tmp_dir)
