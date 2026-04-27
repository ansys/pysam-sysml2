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
        element = sysml_mapper.map("pp", data, None).get_element()
        assert isinstance(element, Element)
        assert element.id == "element_id"
        assert element.__class__.__name__ == "PartUsage"

    def test_invalid_sysml_element(self, sysml_mapper: SysMLMapper):
        data = {
            "@id": "element_id",
        }
        with pytest.raises(InvalidProjectJSONMapperException):
            sysml_mapper.map("pp", data, None)

    def test_create_element_string_field(self, sysml_mapper: SysMLMapper):
        data = {
            "@id": "element_id",
            "@type": "PartUsage",
            "name": "Element",
            "qualifiedName": "pp::p",
        }
        element = sysml_mapper.map("pp", data, None).get_element()
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
        element = sysml_mapper.map("pp", data, None).get_element()
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
        element = sysml_mapper.map("pp", data, None).get_element()
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

        mapped_element = sysml_mapper.map("pp", data, None)
        mapped_owner = sysml_mapper.map("pp", owner_data, None)
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
        element = sysml_mapper.map("pp", data, None).get_element()
        assert element.is_abstract is True
