from ._wrapper_factory  import create_wrapper
from ..setups.query import CallbackQueryHandlerSetup,\
    ShippingQueryHandlerSetup, PreCheckoutQueryHandlerSetup

def callback_query_handler(*args, **kwargs):
    return create_wrapper(CallbackQueryHandlerSetup, *args, **kwargs)

def shipping_query_handler(*args, **kwargs):
    return create_wrapper(ShippingQueryHandlerSetup, *args, **kwargs)

def pre_checkout_query_handler(*args, **kwargs):
    return create_wrapper(PreCheckoutQueryHandlerSetup, *args, **kwargs)