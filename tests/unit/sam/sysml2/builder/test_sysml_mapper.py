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

"""Unit tests for SysMLMapper mirroring test_scripting_mapper.py."""

import pytest

from ansys.sam.sysml2.builder.mapper.sysml_mapper import SysMLMapper
from ansys.sam.sysml2.exception.mapper_exception import InvalidProjectJSONMapperException
from ansys.sam.sysml2.meta_model.element import Element


class TestSysMLMapper:

    @pytest.fixture
    def sysml_mapper(self):
        return SysMLMapper()

    def test_check_valid_sysml_element(self, sysml_mapper: SysMLMapper):
        data = {
            "@id": "element_id",
            "@type": "PartUsage",
            "qualifiedName": "pp::p",
        }

        element = sysml_mapper.map(data, None).get_element()

        assert isinstance(element, Element)
        assert element.id == "element_id"
        assert element.__class__.__name__ == "PartUsage"

    def test_invalid_sysml_element(self, sysml_mapper: SysMLMapper):
        data = {
            "@id": "element_id",
        }

        with pytest.raises(InvalidProjectJSONMapperException):
            sysml_mapper.map(data, None)

    def test_create_element_string_field(self, sysml_mapper: SysMLMapper):
        data = {
            "@id": "element_id",
            "@type": "PartUsage",
            "name": "Element",
            "qualifiedName": "pp::p",
        }

        element = sysml_mapper.map(data, None).get_element()

        assert isinstance(element, Element)
        assert element.id == "element_id"
        assert element.__class__.__name__ == "PartUsage"
        assert element.name == "Element"

    def test_create_element_list_field(self, sysml_mapper: SysMLMapper):
        data = {
            "@id": "element_id",
            "@type": "PartUsage",
            "ownedElement": [{"@id": "sub_element_id"}],
            "qualifiedName": "pp::p",
        }

        element = sysml_mapper.map(data, None).get_element()

        assert isinstance(element, Element)
        assert element.id == "element_id"
        assert element.__class__.__name__ == "PartUsage"
        assert len(element.owned_element) == 1

    def test_create_element_list_text(self, sysml_mapper: SysMLMapper):
        data = {
            "@id": "element_id",
            "@type": "Comment",
            "body": "Some comment text",
            "qualifiedName": "pp::p",
        }

        element = sysml_mapper.map(data, None).get_element()

        assert isinstance(element, Element)
        assert element.body == "Some comment text"

    def test_create_element_reference_field(self, sysml_mapper: SysMLMapper):
        data = {
            "@id": "element_id",
            "@type": "PartUsage",
            "owner": {"@id": "part_id"},
            "qualifiedName": "pp::p",
        }
        owner_data = {
            "@id": "part_id",
            "@type": "PartDefinition",
            "name": "MyPart",
            "qualifiedName": "pp::p",
        }

        mapped_element = sysml_mapper.map(data, None)
        mapped_owner = sysml_mapper.map(owner_data, None)
        element = mapped_element.get_element()
        owner = mapped_owner.get_element()
        unresolved_fields = (
            mapped_element.get_unresolved_fields()
            + mapped_owner.get_unresolved_fields()
        )
        env = {"element_id": element, "part_id": owner}
        for unresolved_field in unresolved_fields:
            element_id = unresolved_field.get_id()
            el = env.get(element_id, None)
            if el is not None:
                unresolved_field.resolve(el)

        assert isinstance(element, Element)
        assert element.id == "element_id"
        assert element.__class__.__name__ == "PartUsage"
        assert element.owner is owner

    def test_snake_case_field_name(self, sysml_mapper: SysMLMapper):
        """Verify camelCase JSON keys are converted to snake_case attributes."""
        data = {
            "@id": "element_id",
            "@type": "PartUsage",
            "qualifiedName": "pp::p",
            "isAbstract": True,
        }

        element = sysml_mapper.map(data, None).get_element()

        assert element.is_abstract is True

    def test_literal_string_value_unescapes_kerml(self, sysml_mapper: SysMLMapper):
        """API KerML-escaped LiteralString.value is decoded on map."""
        data = {
            "@id": "literal_id",
            "@type": "LiteralString",
            "value": "try\\\\to",
        }

        element = sysml_mapper.map(data, None).get_element()

        assert element.__class__.__name__ == "LiteralString"
        assert element.value == "try\\to"
        assert element.value.count("\\") == 1

    def test_standard_library_package_keeps_unresolved_on_map(self, sysml_mapper: SysMLMapper):
        """map always keeps child references; skip is decided later."""
        data = {
            "@id": "library_id",
            "@type": "LibraryPackage",
            "isLibraryElement": True,
            "isStandard": True,
            "ownedElement": [{"@id": "child_id"}],
        }

        mapped_element = sysml_mapper.map(data, None)

        unresolved_ids = [field.get_id() for field in mapped_element.get_unresolved_fields()]
        assert "child_id" in unresolved_ids
        assert sysml_mapper._should_drop_library_unresolved(
            mapped_element.get_element(), None, False
        )

    def test_user_library_package_keeps_unresolved_fields(self, sysml_mapper: SysMLMapper):
        """Non-standard LibraryPackage keeps child references."""
        data = {
            "@id": "library_id",
            "@type": "LibraryPackage",
            "isLibraryElement": True,
            "isStandard": False,
            "ownedElement": [{"@id": "child_id"}],
        }

        mapped_element = sysml_mapper.map(data, None)

        unresolved_ids = [field.get_id() for field in mapped_element.get_unresolved_fields()]
        assert "child_id" in unresolved_ids
        assert not sysml_mapper._should_drop_library_unresolved(
            mapped_element.get_element(), None, False
        )

    def test_standard_library_package_kept_when_resolving(self, sysml_mapper: SysMLMapper):
        """resolve_standard_libraries does not drop standard LibraryPackage child references."""
        data = {
            "@id": "library_id",
            "@type": "LibraryPackage",
            "isLibraryElement": True,
            "isStandard": True,
            "ownedElement": [{"@id": "child_id"}],
        }

        mapped_element = sysml_mapper.map(data, None)

        assert not sysml_mapper._should_drop_library_unresolved(
            mapped_element.get_element(), None, True
        )

    def test_library_part_usage_dropped_without_env(self, sysml_mapper: SysMLMapper):
        """Library PartUsage without owner env is skipped for fetch."""
        data = {
            "@id": "part_id",
            "@type": "PartUsage",
            "isLibraryElement": True,
            "ownedElement": [{"@id": "child_id"}],
        }

        mapped_element = sysml_mapper.map(data, None)

        unresolved_ids = [field.get_id() for field in mapped_element.get_unresolved_fields()]
        assert "child_id" in unresolved_ids
        assert sysml_mapper._should_drop_library_unresolved(
            mapped_element.get_element(), None, False
        )

    def test_user_library_part_usage_kept_with_owner_env(self, sysml_mapper: SysMLMapper):
        """User-library PartUsage is not skipped when owner is in env."""
        owner_data = {
            "@id": "library_id",
            "@type": "LibraryPackage",
            "isLibraryElement": True,
            "isStandard": False,
        }
        owner = sysml_mapper.map(owner_data, None).get_element()
        data = {
            "@id": "part_id",
            "@type": "PartUsage",
            "isLibraryElement": True,
            "owner": {"@id": "library_id"},
            "ownedElement": [{"@id": "child_id"}],
        }

        mapped_element = sysml_mapper.map(data, None)

        assert not sysml_mapper._should_drop_library_unresolved(
            mapped_element.get_element(), {"library_id": owner}, False
        )
