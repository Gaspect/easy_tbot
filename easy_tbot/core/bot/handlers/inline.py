from .base import HandlerMixing, SetupMixin

class InlineHandler(HandlerMixing, SetupMixin):
    def setup(self, bot):
        bot.add_inline_handler(self)

class ChosenInlineHandler(HandlerMixing, SetupMixin):
    def setup(self, bot):
        bot.add_chosen_inline_handler(self)
