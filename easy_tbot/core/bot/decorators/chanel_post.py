from ._wrapperfactory import create_wrapper
from ..handlers.channel_post import ChanelPostHandler, EditedChanelPostHandler

def chanel_post_handler(*args, **kwargs):
    return create_wrapper(ChanelPostHandler, *args, **kwargs)

def edited_chanel_post_handler(*args, **kwargs):
    return create_wrapper(EditedChanelPostHandler, *args, **kwargs)
