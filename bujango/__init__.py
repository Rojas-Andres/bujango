from bujango.utils.version import get_version

VERSION = (4, 1, 7, "final", 0)

__version__ = get_version(VERSION)


def setup(set_prefix=True):
    """
    Configure the settings (this happens as a side effect of accessing the
    first setting), configure logging and populate the app registry.
    Set the thread-local urlresolvers script prefix if `set_prefix` is True.
    """
    from bujango.apps import apps
    from bujango.conf import settings
    # from bujango.urls import set_script_prefix
    from bujango.utils.log import configure_logging

    # configure_logging(settings.LOGGING_CONFIG, settings.LOGGING)
    # if set_prefix:
    #     set_script_prefix(
    #         "/" if settings.FORCE_SCRIPT_NAME is None else settings.FORCE_SCRIPT_NAME
    #     )
    apps.populate(settings.INSTALLED_APPS)