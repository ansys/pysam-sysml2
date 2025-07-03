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

"""
File  created on Mon Dec 09 2024.

This class simulate a model server.

This server use defined route in the file `routes/__init__.py`.
=> See doc in this file to add your own routes
"""

import threading

from flask import Flask, jsonify
from werkzeug.serving import make_server

from .routes import routes_list


class MockedServer:
    """This class simulate Model server."""

    __app: Flask
    __server = None
    _server_port = 5000

    def __init__(self) -> None:
        app = Flask("Mocked")
        for route in routes_list:
            app.add_url_rule(**route.get_data())

        @app.errorhandler(404)
        @app.errorhandler(403)
        @app.errorhandler(401)
        @app.errorhandler(400)
        def handle_error(e):
            return (
                jsonify(e.description),
                e.code,
            )

        self.__app = app

    def start_server(self):
        """Use this method to start the Mocked Server."""

        server = make_server(
            "localhost",
            self._server_port,
            self.__app,
        )
        self.__server = server
        threading.Thread(target=server.serve_forever).start()

    def stop_server(self):
        """Use this method to stop the server."""
        if self.__server is not None:
            self.__server.shutdown()

    @staticmethod
    def get_url() -> str:
        """
        Use this method to get the base server URL

        Returns
        -------
        str
            The server url
        """
        return f"http://127.0.0.1:{MockedServer._server_port}"

    def get_app(self) -> Flask:
        """
        Use this method to get the Flask App

        Returns
        -------
        Flask
            The app
        """
        return self.__app
