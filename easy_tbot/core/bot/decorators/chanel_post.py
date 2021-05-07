from ._wrapper_factory import create_wrapper
from ..setups.chanel_post import ChanelPostHandlerSetup, EditedChanelPostHandlerSetup

def chanel_post_handler(*args, **kwargs):
    return create_wrapper(ChanelPostHandlerSetup, *args, **kwargs)

def edited_chanel_post_handler(*args, **kwargs):
    return create_wrapper(EditedChanelPostHandlerSetup, *args, **kwargs)
