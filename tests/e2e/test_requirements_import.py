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

"""E2E tests: import requirements from a CSV file into the bike project."""

import csv

import pytest

from ansys.sam.sysml2.tools.factory import Factory

from .conftest import _get_models_dir, load_scripting_project, load_sysml_project

CSV_PATH = _get_models_dir() / "bike" / "data" / "requirements.csv"


def _read_requirements_csv():
    """Read the requirements CSV and return a list of dicts."""
    with open(CSV_PATH, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return rows


@pytest.mark.e2e
class TestRequirementsImportScripting:

    def test_import_requirements_from_csv(self, connector, project_manager):
        """Import 10 requirements from CSV into bike project via scripting API."""
        project = load_scripting_project(connector, project_manager, "bike")
        bike = project.get_root_package().Structure.Bike

        rows = _read_requirements_csv()
        assert len(rows) == 10

        factory = Factory(project, connector)
        for row in rows:
            req = factory.create_requirement_usage(name=row["title"], owner=bike)
            req._text = [row["description"]]
            req._reqId = row["id"]

        bike = project.get_root_package().Structure.Bike
        for row in rows:
            req = getattr(bike, row["title"])
            assert req._name == row["title"]
            assert row["description"] in req._text

        connector.delete_project(project._id)

    def test_import_requirements_transactional(self, connector, project_manager):
        """Import 10 requirements in transactional mode (single commit) via scripting API."""
        project = load_scripting_project(connector, project_manager, "bike")
        bike = project.get_root_package().Structure.Bike

        rows = _read_requirements_csv()
        assert len(rows) == 10

        factory = Factory(project, connector)

        project.start_transactional_mode()
        for row in rows:
            req = factory.create_requirement_usage(name=row["title"], owner=bike)
            req._text = [row["description"]]
            req._reqId = row["id"]
        project.stop_transactional_mode()

        bike = project.get_root_package().Structure.Bike
        for row in rows:
            req = getattr(bike, row["title"])
            assert req._name == row["title"]
            assert row["description"] in req._text

        connector.delete_project(project._id)


@pytest.mark.e2e
class TestRequirementsImportSysML:

    def test_import_requirements_from_csv(self, connector, project_manager):
        """Import 10 requirements from CSV into bike project via SysML API."""
        project = load_sysml_project(connector, project_manager, "bike")
        bike = project.get_root_package().get("Structure").get("Bike")

        rows = _read_requirements_csv()
        assert len(rows) == 10

        factory = Factory(project, connector)
        for row in rows:
            req = factory.create_requirement_usage(name=row["title"], owner=bike)
            req._text = [row["description"]]
            req._reqId = row["id"]

        bike = project.get_root_package().get("Structure").get("Bike")
        for row in rows:
            req = bike.get(row["title"])
            assert req is not None
            assert req.name == row["title"]

        connector.delete_project(project._id)

    def test_import_requirements_transactional(self, connector, project_manager):
        """Import 10 requirements in transactional mode (single commit) via SysML API."""
        project = load_sysml_project(connector, project_manager, "bike")
        bike = project.get_root_package().get("Structure").get("Bike")

        rows = _read_requirements_csv()
        assert len(rows) == 10

        factory = Factory(project, connector)

        project.start_transactional_mode()
        for row in rows:
            req = factory.create_requirement_usage(name=row["title"], owner=bike)
            req._text = [row["description"]]
            req._reqId = row["id"]
        project.stop_transactional_mode()

        bike = project.get_root_package().get("Structure").get("Bike")
        for row in rows:
            req = bike.get(row["title"])
            assert req is not None
            assert req.name == row["title"]

        connector.delete_project(project._id)
