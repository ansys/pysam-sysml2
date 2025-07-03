.. _Info_Section:


Finding information
###################

This section contains instructions for finding required information such as the Project ID or your Auth token.



.. _Info_P_Id_Section:

Find project ID
================

You can find the Project ID in different places:

- **Editor**:

  - Open the project in the editor, the Project ID appears in the web page URL:

  .. figure:: /_static/images/project-id-editor.png

- **Dashboard**:

  - Open the project view page, the Project ID appears in the web page URL:

  .. figure:: /_static/images/project-id-dashboard.png


.. _Info_O_Id_Section:

Find organization ID
====================

To get your Organization ID, follow these steps:

- Go to your Dashboard
- Click on your Organization:

   .. figure:: /_static/images/orga-1.png

- You can find your Organization ID in the URL of the page:

    .. figure:: /_static/images/orga-2.png

You got your Organization ID.

.. _Info_B_Token_Section:

Find bearer token
==================

You can use the temporary token or create a PAT and use this long time token.

Temporary token
~~~~~~~~~~~~~~~

To get your Bearer Token, open the SAM Editor Dashboard on your browser. Then click ``F12`` to open the browser's console.

Then, go to the `Network` tab and reload the page.

Many requests appear, search for one of these:

- ``me``
- ``organizations``
- ``access-rights``

Then, click it, and go to the `Headers` tab.

The `Authorization` header appears with the value of your Bearer Token.

.. warning::

  Only take the Token, after "Bearer "

PAT token
~~~~~~~~~

To create a **Personal Access Token (PAT)**, you first need a valid **Bearer Token**. Follow the steps in the :ref:`Temporary Token <Info_B_Token_Section>` section to retrieve it using your browser's developer tools.

Once you have your Bearer Token, navigate to the `Swagger UI` page.
For example: `https://<SERVER-URL>/api/swagger-ui/index.html`

Click on the **Authorize** button and paste your Bearer Token in the authentication field.

.. figure:: /_static/images/authorize.png

.. figure:: /_static/images/bearer-auth.png

Once authorized, go to the top right of the page and open the `Select a definition` dropdown. Scroll down and select the **Personal Access Token API**.

.. figure:: /_static/images/pat-dropdown.png

Use the **POST** request to generate a new PAT. You can optionally define the number of days the token should remain valid (the default is 30 days).

After submitting the request, your newly generated PAT appears in the response body.

.. figure:: /_static/images/get-pat.png

.. note::

  Make sure to save your PAT somewhere secure, as it may not be displayed again once you leave the page.
  You can always generate a new one if needed.

.. only:: html

    .. grid:: 2

        .. grid-item-card:: :fa:`arrow-left` Previous step
            :link: diagram-model
            :link-type: doc

            How to get use diagrams

        .. grid-item::