from .base import HandlerMixing, SetupMixin

class CallbackQueryHandler(HandlerMixing, SetupMixin):
    def setup(self, bot):
        bot.add_callback_query_handler(self)

class ShippingQueryHandler(HandlerMixing, SetupMixin):
    def setup(self, bot):
        bot.add_shipping_query_handler(self)

class PreCheckoutQueryHandler(HandlerMixing, SetupMixin):
    def setup(self, bot):
        bot.add_pre_checkout_query_handler(self)
