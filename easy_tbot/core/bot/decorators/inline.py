from ._wrapper_factory import create_wrapper
from ..setups.inline import InlineHandlerSetup, ChosenInlineHandlerSetup

def inline_handler(*args, **kwargs):
    return create_wrapper(InlineHandlerSetup, *args, **kwargs)

def chosen_inline_handler(*args, **kwargs):
    return create_wrapper(ChosenInlineHandlerSetup, *args, **kwargs)