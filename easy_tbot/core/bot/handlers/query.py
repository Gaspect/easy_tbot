from .base import HandlerMixing, SetupMixin

class CallbackQueryHandler(SetupMixin):
    def setup(self, bot):
        bot.add_callback_query_handler(self)

class ShippingQueryHandler(SetupMixin):
    def setup(self, bot):
        bot.add_shipping_query_handler(self)

class PreCheckoutQueryHandler(SetupMixin):
    def setup(self, bot):
        bot.add_pre_checkout_query_handler(self)
