from ._wrapper_factory import create_wrapper
from ..setups.middleware import MiddlewareSetup

def middleware(*args, **kwargs):
    return create_wrapper(MiddlewareSetup, *args, **kwargs)