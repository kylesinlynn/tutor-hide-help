from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-lms-common-settings",
        "FEATURES['ENABLE_HELP_LINK'] = False"
    )
)

hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-cms-common-settings",
        "FEATURES['ENABLE_HELP_LINK'] = False"
    )
)