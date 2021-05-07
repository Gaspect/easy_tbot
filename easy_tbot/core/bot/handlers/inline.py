from .base import SetupMixin

class InlineHandler(SetupMixin):
    def setup(self, bot):
        bot.add_inline_handler(self)

class ChosenInlineHandler(SetupMixin):
    def setup(self, bot):
        bot.add_chosen_inline_handler(self)
