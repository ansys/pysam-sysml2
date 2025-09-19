.. _Info_Section:

Find information
################

This page explains how to find required information, such as the project ID or your authorization token.

.. _Info_P_Id_Section:

Find project ID
===============

You can find the project ID in different places.

- **Editor**:
  Open the project in the editor. The project ID appears in the web page URL:

  .. figure:: /_static/images/project-id-editor.png

- **Dashboard**:
  Open the project view page. The project ID appears in the web page URL:

  .. figure:: /_static/images/project-id-dashboard.png

.. _Info_O_Id_Section:

Find organization ID
====================

Follow these steps to find your organization ID:

- Go to your dashboard.
- Click your organization.

  .. figure:: /_static/images/orga-1.png

- Find your organization ID in the page URL:

  .. figure:: /_static/images/orga-2.png

.. _Info_B_Token_Section:

Find authorization token
========================

For authorization, you can either use a bearer (temporary) token for quick access or create a Personal Access Token (PAT) for longer-term use.

Bearer token
~~~~~~~~~~~~

Follow these steps to get a bearer token:

#. Open the SAM editor dashboard in your browser.
#. Press ``F12`` to open the browser's console.
#. Go to the **Network** tab and reload the page.

   Many requests appear. Search for one of these:

   - ``me``
   - ``organizations``
   - ``access-rights``

#. Click the relevant request and go to the **Headers** tab.

The **Authorization** header shows the value of your bearer token.

.. caution::

    Copy only the token after ``Bearer``.

Personal Access Token (PAT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creating a Personal Access Token (PAT) is the recommended method for authentication with PySAM due to its longer validity.

**New method (recommended for current servers)**

Follow these steps to generate a PAT from your account settings:

#. **Access account settings:**
   From the main page of the SAM editor, click your account logo in the top right corner and select **Account settings**.

   .. figure:: /_static/images/access-account-settings.png
      :alt: Access account settings

#.  **Navigate to personal access tokens:**
   On the **Account settings** page, click **Personal access tokens** in the navigation pane.

   .. figure:: /_static/images/personal-access-token.png
      :alt: Personal access tokens option

3.  **Generate new token:**
   Click the **Generate new token** button.

   .. figure:: /_static/images/generate-new-token.png
      :alt: Generate new token button

4. **Configure token details:**
   Enter a descriptive label for your token in the **Token label** field and set the expiration date. Click the **Generate token** button.

   .. figure:: /_static/images/generate-token.png
      :alt: Enter token label and expiration date

#.  **Copy generated token:**
   When the token displays, click **Copy** to save it to your clipboard.

   .. figure:: /_static/images/copy-generated-token.png
      :alt: Copy generated token

.. important::

    **Store this token in a secure location.** The token is not displayed again after you leave this page. Generate a new one if needed.

**Old method (for older server versions)**

If you are using an older server version that does not support the direct account settings method, you can generate a PAT via the Swagger UI.

#. **Obtain a temporary bearer token:**
   First, get a valid bearer token. Follow the steps in the :ref:`Temporary token <Info_B_Token_Section>` section to retrieve it using your browser's developer tools.

#. **Access Swagger UI:**
   Navigate to the Swagger UI page: ``https://<SERVER-URL>/api/swagger-ui/index.html``

#. **Authorize with bearer token:**
   Click the **Authorize** button and paste your bearer token into the authentication field.

   .. figure:: /_static/images/authorize.png
      :alt: Authorize button on Swagger UI

   .. figure:: /_static/images/bearer-auth.png
      :alt: Bearer token input field

#. **Select personal access token API:**
   Open the **Select a definition** dropdown in the top right of the page. Scroll down and select **Personal Access Token API**.

   .. figure:: /_static/images/pat-dropdown.png
      :alt: Select Personal Access Token API from dropdown
      
#. **Generate PAT via POST request:**
   Use the **POST** request to generate a new PAT. Optionally, define the number of days the token remains valid. The default is 30 days.

   After submitting the request, the PAT appears in the response body:

   .. figure:: /_static/images/get-pat.png
      :alt: Get PAT from Swagger UI response

.. note::

    Save your PAT in a secure location because it is not displayed again after you leave the page. Generate a new one if needed.

.. only:: html

    .. grid:: 2

        .. grid-item-card:: :fa:`arrow-left` Previous step
            :link: diagram-model
            :link-type: doc

            Work with diagrams

        .. grid-item::