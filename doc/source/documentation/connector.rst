Create a New SysML Connector
============================

Add a RouteDispatcher
----------------------

A *RouteDispatcher* helps the SysML Connector construct full URLs for standard SysML2 endpoints.

To create a new RouteDispatcher, navigate to the folder:

``ansys/sam/sysml2/routes``

Then, create a new file named: *XXXX_route_dispatcher.py*.

Define your class as follows:

.. code-block:: python

    class XXXXRouteDispatcher(RouteDispatcher):
        """Class dedicated to XXXX specific API routes."""

        def __init__(self, server_url: str) -> None:
            super().__init__(server_url)

        @overrides
        def build_endpoint(self, endpoint: str) -> str:
            """
            Creates the full URL using the given API endpoint.

            Parameters
            ----------
            endpoint : str
                The endpoint to build.

            Returns
            -------
            str
                The full URL.
            """
            return f"{self._server_url}/sysml2/{endpoint}"

Add SysML Auth
--------------

Once the RouteDispatcher is ready, you need to authenticate your connector to the server.

Go to the folder:

``ansys/sam/sysml2/auth``

Create a new file named: *xxx_auth.py*.

Define your authentication class as follows:

.. code-block:: python

    class XXXXAuth(SysMLAuth):
        """XXXXAuth provides the correct authentication for the XXXX Standard API implementation."""

        _token: str

        def __init__(self, token: str) -> None:
            self._token = token
            super().__init__()

        @overrides
        def update_request(self, request: HttpRequest) -> HttpRequest:
            """
            Updates the HttpRequest with the necessary authorization header.

            Parameters
            ----------
            request : HttpRequest
                The request to update.

            Returns
            -------
            HttpRequest
                The updated request.
            """
            request.headers["Authorization"] = self._token
            return request

At this stage, you have all the necessary classes for your connector. The next step is to update the Factory to include your new SysML2 connector.

Update Factory
--------------

To provide your new connector to users, update the *ConnectorFactory* with a new method:

.. code-block:: python

    @staticmethod
    def create_xxxx_sysml_connector(
        server_url: str = "http://localhost:8443",
        auth: str = None,
        is_secure: bool = True
    ) -> SysMLConnector:
        """
        Creates a new SysML connector for the XXXX API.

        Parameters
        ----------
        server_url : str
            The base URL of the server.
        auth : str
            The authentication token.
        is_secure : bool
            Indicates if the server uses SSL.

        Returns
        -------
        SysMLConnector
            The initialized SysML connector.
        """
        routes = XXXXRouteDispatcher(server_url)
        authentication = XXXXAuth(auth)
        return SysMLConnector(routes, authentication, is_secure)

This example requires the user to provide the `server_url`, an authentication token (`auth`), and whether the server is SSL-secure
