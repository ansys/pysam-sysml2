# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
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
"""Exception module for PySAM SysML2."""

from .connector_exception import (
    BadRequestConnectionException as BadRequestConnectionException,
    ConnectorConnectionException as ConnectorConnectionException,
    ConnectorException as ConnectorException,
    DiagramConnectorException as DiagramConnectorException,
    DiagramNotAvailableException as DiagramNotAvailableException,
    ElementNotFoundException as ElementNotFoundException,
    HTTPResponseException as HTTPResponseException,
    InvalidElementJsonFoundException as InvalidElementJsonFoundException,
    InvalidProjectNameException as InvalidProjectNameException,
    ProjectNotFoundException as ProjectNotFoundException,
    UnauthorizedConnectionException as UnauthorizedConnectionException,
)
from .mapper_exception import (
    InvalidProjectJSONMapperException as InvalidProjectJSONMapperException,
    MapperException as MapperException,
)
from .query_exception import (
    InvalidCompositeConstraint as InvalidCompositeConstraint,
    InvalidQuery as InvalidQuery,
    QueryException as QueryException,
)
from .runtime_exception import UnsupportedValueExpression as UnsupportedValueExpression
