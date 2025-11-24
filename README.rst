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


The email and push notification settings under Account can be enabled/disabled using `NOTIFICATIONS_ENABLE_SHOW_EMAIL_CHANNEL`
and `NOTIFICATIONS_ENABLE_SHOW_PUSH_CHANNEL`. `NOTIFICATIONS_ENABLE_SHOW_EMAIL_CHANNEL` is set to True while `NOTIFICATIONS_ENABLE_SHOW_PUSH_CHANNEL`
is set to False by default.

License
*******

This software is licensed under the terms of the AGPLv3.
