.. _Info_Section:

Find information
################

This section contains instructions for finding required information such as the project ID or your authorization token.


.. _Info_P_Id_Section:

Find project ID
===============

You can find the Project ID in different places:

- **Editor**:
  Open the project in the editor; the Project ID appears in the web page URL:

  .. figure:: /_static/images/project-id-editor.png

- **Dashboard**:
  Open the project view page; the Project ID appears in the web page URL:

  .. figure:: /_static/images/project-id-dashboard.png


.. _Info_O_Id_Section:

Find organization ID
====================

To get your Organization ID, follow these steps:

- Go to your Dashboard
- Click your Organization:

  .. figure:: /_static/images/orga-1.png

- You can find your Organization ID in the URL of the page:

  .. figure:: /_static/images/orga-2.png

You have successfully retrieved your Organization ID.

.. _Info_B_Token_Section:

Find bearer token
==================

You can use a temporary token for quick access or create a Personal Access Token (PAT) for longer-term use.

Temporary token
~~~~~~~~~~~~~~~

To get your Bearer Token, open the SAM Editor Dashboard on your browser. Then click ``F12`` to open the browser's console.

Next, go to the `Network` tab and reload the page.

Many requests appear. Search for one of these:

- ``me``
- ``organizations``
- ``access-rights``

Then, click the relevant request and go to the `Headers` tab.

The `Authorization` header shows the value of your Bearer Token.

.. warning::

    Only take the Token, after "Bearer "

Personal access token (PAT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creating a Personal Access Token (PAT) is the recommended method for authentication with PySAM due to its longer validity.

**New Method (Recommended for Current Servers)**

Follow these steps to generate a PAT directly from your account settings:

1.  **Access Account Settings:**
    From the main page of the SAM Editor, click your account logo in the top right corner, then select "Account settings."

    .. figure:: /_static/images/access-account-settings.png
       :alt: Access Account Settings

2.  **Navigate to Personal Access Tokens:**
    On the settings page, click "Personal access tokens" in the navigation pane.

    .. figure:: /_static/images/personal-access-token.png
       :alt: Personal Access Token section

3.  **Generate New Token:**
    Click the "Generate new token" button.

    .. figure:: /_static/images/generate-new-token.png
       :alt: Generate New Token button

4.  **Configure Token Details:**
    Enter a descriptive label for your token in the "Token Label" field and set the desired expiration date. Then, click "Generate Token."

    .. figure:: /_static/images/generate-token.png
       :alt: Enter Token Label and Expiration Date

5.  **Copy Generated Token:**
    Your newly generated token displays. Copy this token immediately.

    .. figure:: /_static/images/copy-generated-token.png
       :alt: Copy Generated Token

.. important::

    **Store this token in a secured location.** For security reasons, it is not displayed again once you leave this page. You can always generate a new one if needed.

**Old Method (For Older Server Versions)**

If you are using an older server version that does not support the direct account settings method, you can generate a PAT via the Swagger UI.

1.  **Obtain a Temporary Bearer Token:**
    First, you need a valid Bearer Token. Follow the steps in the :ref:`Temporary Token <Info_B_Token_Section>` section to retrieve it using your browser's developer tools.

2.  **Access Swagger UI:**
    Once you have your Bearer Token, navigate to the `Swagger UI` page.
    For example: `https://<SERVER-URL>/api/swagger-ui/index.html`

3.  **Authorize with Bearer Token:**
    Click the **Authorize** button and paste your Bearer Token into the authentication field.

    .. figure:: /_static/images/authorize.png
       :alt: Authorize button on Swagger UI

    .. figure:: /_static/images/bearer-auth.png
       :alt: Bearer Token input field

4.  **Select Personal Access Token API:**
    Once authorized, go to the top right of the page and open the `Select a definition` dropdown. Scroll down and select the **Personal Access Token API**.

    .. figure:: /_static/images/pat-dropdown.png
       :alt: Select Personal Access Token API dropdown

5.  **Generate PAT via POST Request:**
    Use the **POST** request to generate a new PAT. You can optionally define the number of days the token should remain valid (the default is 30 days).

    After submitting the request, your newly generated PAT appears in the response body.

    .. figure:: /_static/images/get-pat.png
       :alt: Get PAT from Swagger UI response

.. note::

    Make sure to save your PAT somewhere secure, as it is not displayed again once you leave the page.
    You can always generate a new one if needed.

.. only:: html

    .. grid:: 2

        .. grid-item-card:: :fa:`arrow-left` Previous step
            :link: diagram-model
            :link-type: doc

            How to get use diagrams

        .. grid-item::