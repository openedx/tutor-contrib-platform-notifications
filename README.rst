notifications plugin for `Tutor <https://docs.tutor.edly.io>`__
###############################################################

A Tutor plugin to manage configuration and plugin slots for the Notifications tray feature.


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

The plugin exposes the following Tutor configuration keys :
  - ``NOTIFICATIONS_DEFAULT_FROM_EMAIL``
  - Default: inherits from the platform `CONTACT_EMAIL`.
  - Purpose: sets the default "from" address used when sending notification emails.

.. code-block:: yaml

    NOTIFICATIONS_DEFAULT_FROM_EMAIL: "no-reply@example.org"

After changing configuration,restart environment so the new environment variable and settings are picked up by the LMS and MFE images.
If you rely on a specific "from" email for outgoing notifications, explicitly set ``NOTIFICATIONS_DEFAULT_FROM_EMAIL`` rather than relying on the platform-wide ``CONTACT_EMAIL``.


The email and push notification settings under Account can be enabled/disabled using `NOTIFICATIONS_ENABLE_SHOW_EMAIL_CHANNEL`
and `NOTIFICATIONS_ENABLE_SHOW_PUSH_CHANNEL`. `NOTIFICATIONS_ENABLE_SHOW_EMAIL_CHANNEL` is set to True while `NOTIFICATIONS_ENABLE_SHOW_PUSH_CHANNEL`
is set to False by default.

License
*******

This software is licensed under the terms of the AGPLv3.
