from .base import SetupMixin, HandlerMixing

class MessageHandler(HandlerMixing, SetupMixin):
    def setup(self, bot):
        bot.add_message_handler(self)

class EditedMessageHandler(HandlerMixing, SetupMixin):
    def setup(self,bot):
        bot.add_edited_message_handler(self)