.. _Info_Section:


Finding information
####################

In this section, you will find instructions for finding required information such as the Project ID or your Auth token.



.. _Info_P_Id_Section:

Find Project ID
================

You can find the Project ID in different places:

- **Editor**:

  - Open the project in the editor, you will have the Project ID in the web page URL:

  .. figure:: /_static/images/projectIdEditor.png

- **Dashboard**:

  - Open the project view page, you will find the Project ID in the web page URL:

  .. figure:: /_static/images/projectIdDashboard.png



.. _Info_O_Id_Section:

Find Organization Id
====================

To get your Organization ID, follow these steps:

- Go to your Dashboard
- Click on your Organization:

   .. figure:: /_static/images/orga1.png

- You can find your Organization ID in the URL of the page:

    .. figure:: /_static/images/orga2.png

✔️ You got your Organization ID!

.. _Info_B_Token_Section:

Find Bearer Token
==================

You can use the temporary token or create a PAT and use this long time token.

Temporary token
~~~~~~~~~~~~~~~

To get your Bearer Token, open the SAM Editor Dashboard on your browser. Then click on ``F12`` to open the developer console.

Then, go to the `Network` tab and reload the page.

You will see a lot of requests, search for one of these:

- `me`
- `organizations`
- `access-rights`

Then, click on it, and go to the `Headers` tab.

You will find the `Authorization` header with the value of your Bearer Token.


.. warning::

  Only take the Token, after "Bearer "

