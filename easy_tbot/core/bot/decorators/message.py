from ._wrapperfactory import create_wrapper
from ..handlers.message import MessageHandler, EditedMessageHandler

def message_handler(*args, **kwargs):
    return create_wrapper(MessageHandler, *args, **kwargs)

def edited_message_handler(*args, **kwargs):
    return create_wrapper(EditedMessageHandler, *args, **kwargs)