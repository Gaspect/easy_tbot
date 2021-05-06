from ._wrapperfactory import create_wrapper
from ..handlers.middleware import Middleware

def middleware(*args, **kwargs):
    return create_wrapper(Middleware, *args, **kwargs)