import os
from glob import glob

import importlib_resources
from tutor import hooks
from tutormfe.hooks import PLUGIN_SLOTS

from .__about__ import __version__

########################################
# CONFIGURATION
########################################

hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        # Add your new settings that have default values here.
        # Each new setting is a pair: (setting_name, default_value).
        # Prefix your setting names with 'NOTIFICATIONS_'.
        ("NOTIFICATIONS_VERSION", __version__),
        ("NOTIFICATIONS_ENABLE_SHOW_EMAIL_CHANNEL", True),
        ("NOTIFICATIONS_ENABLE_SHOW_PUSH_CHANNEL", False),
    ]
)

hooks.Filters.CONFIG_UNIQUE.add_items(
    [
        # Add settings that don't have a reasonable default for all users here.
        # For instance: passwords, secret keys, etc.
        # Each new setting is a pair: (setting_name, unique_generated_value).
        # Prefix your setting names with 'NOTIFICATIONS_'.
        # For example:
        ### ("NOTIFICATIONS_SECRET_KEY", "{{ 24|random_string }}"),
    ]
)

hooks.Filters.CONFIG_OVERRIDES.add_items(
    [
        # Danger zone!
        # Add values to override settings from Tutor core or other plugins here.
        # Each override is a pair: (setting_name, new_value). For example:
        ### ("PLATFORM_NAME", "My platform"),
    ]
)


########################################
# INITIALIZATION TASKS
########################################

MY_INIT_TASKS: list[tuple[str, tuple[str, ...]]] = [
    ("lms", ("notifications", "tasks", "lms", "waffle_flags")),
]

for service, template_path in MY_INIT_TASKS:
    full_path: str = str(
        importlib_resources.files("tutornotifications")
        / os.path.join("templates", *template_path)
    )
    with open(full_path, encoding="utf-8") as init_task_file:
        init_task: str = init_task_file.read()
    hooks.Filters.CLI_DO_INIT_TASKS.add_item((service, init_task))


########################################
# TEMPLATE RENDERING
# (It is safe & recommended to leave
#  this section as-is :)
########################################

hooks.Filters.ENV_TEMPLATE_ROOTS.add_items(
    # Root paths for template files, relative to the project root.
    [
        str(importlib_resources.files("tutornotifications") / "templates"),
    ]
)

hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    # For each pair (source_path, destination_path):
    # templates at ``source_path`` (relative to your ENV_TEMPLATE_ROOTS) will be
    # rendered to ``source_path/destination_path`` (relative to your Tutor environment).
    # For example, ``tutornotifications/templates/notifications/build``
    # will be rendered to ``$(tutor config printroot)/env/plugins/notifications/build``.
    [
        ("notifications/build", "plugins"),
        ("notifications/apps", "plugins"),
    ],
)


########################################
# PATCH LOADING
# (It is safe & recommended to leave
#  this section as-is :)
########################################

# For each file in tutornotifications/patches,
# apply a patch based on the file's name and contents.
for path in glob(
    str(importlib_resources.files("tutornotifications") / "patches" / "*")
):
    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))


########################################
# MFE PLUGIN SLOTS
########################################

notification_drawer_config = """
    {
      op: PLUGIN_OPERATIONS.Insert,
      widget: {
        id: 'notification-drawer-widget',
        priority: 10,
        type: DIRECT_PLUGIN,
        RenderWidget: NotificationsTray,
      },
    }
"""

PLUGIN_SLOTS.add_items(
    [
        (
            "all",
            "org.openedx.frontend.layout.header_desktop_secondary_menu.v1",
            notification_drawer_config,
        ),
        (
            "all",
            "org.openedx.frontend.layout.header_learning_help.v1",
            notification_drawer_config,
        ),
        (
            "all",
            "org.openedx.frontend.layout.studio_header_search_button_slot.v1",
            notification_drawer_config,
        ),
    ],
)
