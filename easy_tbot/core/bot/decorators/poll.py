from ._wrapper_factory import create_wrapper
from ..handlers.poll import PollHandler, PollAnswerHandler

def poll_handler(*args, **kwargs):
    return create_wrapper(PollHandler, *args, **kwargs)

def poll_answer_handler(*args, **kwargs):
    return create_wrapper(PollAnswerHandler, *args, **kwargs)
