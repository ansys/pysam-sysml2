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
"""Custom exceptions for connector-related errors."""


class ConnectorException(Exception):
    """Provides top-level exceptions for connectors."""


class ConnectorConnectionException(ConnectorException):
    """Exception when connection information is invalid."""


class UnauthorizedConnectionException(ConnectorException):
    """Exception when the connection is not authorized."""


class HTTPResponseException(ConnectorException):
    """Exception when the connection returns other than 200."""


class InvalidElementJsonFoundException(ConnectorException):
    """Exception when the received JSON data is invalid."""


class ProjectNotFoundException(ConnectorException):
    """Exception when the requested project is not found."""


class ElementNotFoundException(ConnectorException):
    """Exception when the requested element is not found."""


class InvalidProjectNameException(ConnectorException):
    """Exception when the name given for a project is not correct."""


class ProjectAlreadyExistsException(ConnectorException):
    """Exception when a project with the same name already exists."""


class BadRequestConnectionException(ConnectorException):
    """Exception when request is invalid."""


class DiagramConnectorException(ConnectorException):
    """Exception when trying to download diagrams."""


class DiagramNotAvailableException(ConnectorException):
    """Exception when diagram functionality is not available for the project."""
