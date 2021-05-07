from ._wrapper_factory import create_wrapper
from ..setups.message import MessageHandlerSetup, EditedMessageHandlerSetup

def message_handler(*args, **kwargs):
    return create_wrapper(MessageHandlerSetup, *args, **kwargs)

def edited_message_handler(*args, **kwargs):
    return create_wrapper(EditedMessageHandlerSetup, *args, **kwargs)