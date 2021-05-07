from .base import SetupMixin

class MessageHandlerSetup(SetupMixin):
    def setup(self, bot):
        bot.add_message_handler(self)

class EditedMessageHandlerSetup(SetupMixin):
    def setup(self,bot):
        bot.add_edited_message_handler(self)