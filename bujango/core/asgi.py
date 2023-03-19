import bujango
from bujango.core.handlers.asgi import ASGIHandler


def get_asgi_application():
    """
    The public interface to Django's ASGI support. Return an ASGI 3 callable.

    Avoids making bujango.core.handlers.ASGIHandler a public API, in case the
    internal implementation changes or moves in the future.
    """
    bujango.setup(set_prefix=False)
    return ASGIHandler()
