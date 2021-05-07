from .base import HandlerMixing, SetupMixin

class CallbackQueryHandlerSetup(SetupMixin):
    def setup(self, bot):
        bot.add_callback_query_handler(self)

class ShippingQueryHandlerSetup(SetupMixin):
    def setup(self, bot):
        bot.add_shipping_query_handler(self)

class PreCheckoutQueryHandlerSetup(SetupMixin):
    def setup(self, bot):
        bot.add_pre_checkout_query_handler(self)
