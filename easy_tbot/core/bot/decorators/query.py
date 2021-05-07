from ._wrapper_factory  import create_wrapper
from ..handlers.query import CallbackQueryHandler, ShippingQueryHandler, PreCheckoutQueryHandler

def callback_query_handler(*args, **kwargs):
    return create_wrapper(CallbackQueryHandler, *args, **kwargs)

def shipping_query_handler(*args, **kwargs):
    return create_wrapper(ShippingQueryHandler, *args, **kwargs)

def pre_checkout_query_handler(*args, **kwargs):
    return create_wrapper(PreCheckoutQueryHandler, *args, **kwargs)