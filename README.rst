Notifications plugin for `Tutor <https://docs.tutor.edly.io>`__
###############################################################

A Tutor plugin to manage plugin slot and configuration for tray and email notifications feature. Learn
more about it in
`Notifications & Preferences <https://docs.openedx.org/en/latest/learners/sfd_notifications/index.html>`_ 


Installation
************

.. code-block:: bash

    pip install git+https://github.com/openedx/tutor-contrib-notifications

Usage
*****

.. code-block:: bash

    tutor plugins enable notifications


Configuration
*************

The plugin exposes the following Tutor configuration keys:
  - ``NOTIFICATIONS_DEFAULT_FROM_EMAIL``
  - Default: inherits from the platform `CONTACT_EMAIL`.
  - Purpose: sets the default "from" address used when sending notification emails.

.. code-block:: yaml

    NOTIFICATIONS_DEFAULT_FROM_EMAIL: "no-reply@example.org"

After changing configuration,restart environment so the new environment variable and settings are picked up by the LMS and MFE images.
If you rely on a specific "from" email for outgoing notifications, explicitly set ``NOTIFICATIONS_DEFAULT_FROM_EMAIL`` rather than relying on the platform-wide ``CONTACT_EMAIL``.

Visibility of email notification preferences in the Notifications section on the Account Settings
page is governed by the `NOTIFICATIONS_ENABLE_SHOW_EMAIL_CHANNEL` setting. It is TRUE by default.

Visibility of mobile push notification preferences in the Notifications section on the Account Settings
page is governed by the `NOTIFICATIONS_ENABLE_SHOW_PUSH_CHANNEL`. It is FALSE by default because we do
NOT have support for mobile push notifications at the moment.


License
*******

This software is licensed under the terms of the AGPLv3.
