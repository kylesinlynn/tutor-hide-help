from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "common-env-features",
        """
"ENABLE_HELP_LINK": false
"""
    )
)
