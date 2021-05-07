from .base import SetupMixin

class InlineHandlerSetup(SetupMixin):
    def setup(self, bot):
        bot.add_inline_handler(self)

class ChosenInlineHandlerSetup(SetupMixin):
    def setup(self, bot):
        bot.add_chosen_inline_handler(self)
