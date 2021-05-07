from ._wrapper_factory import create_wrapper
from ..handlers.inline import InlineHandler, ChosenInlineHandler

def inline_handler(*args, **kwargs):
    return create_wrapper(InlineHandler, *args, **kwargs)

def chosen_inline_handler(*args, **kwargs):
    return create_wrapper(ChosenInlineHandler, *args, **kwargs)