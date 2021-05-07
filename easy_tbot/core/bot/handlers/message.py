from .base import SetupMixin

class MessageHandler(SetupMixin):
    def setup(self, bot):
        bot.add_message_handler(self)

class EditedMessageHandler(SetupMixin):
    def setup(self,bot):
        bot.add_edited_message_handler(self)