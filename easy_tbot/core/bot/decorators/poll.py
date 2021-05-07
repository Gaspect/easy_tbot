from ._wrapper_factory import create_wrapper
from ..setups.poll import PollHandlerSetup, PollAnswerHandlerSetup

def poll_handler(*args, **kwargs):
    return create_wrapper(PollHandlerSetup, *args, **kwargs)

def poll_answer_handler(*args, **kwargs):
    return create_wrapper(PollAnswerHandlerSetup, *args, **kwargs)
