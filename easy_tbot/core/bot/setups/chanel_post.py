from .base import SetupMixin


class ChanelPostHandlerSetup(SetupMixin):
    def setup(self, bot):
        bot.add_chanel_post_handler(self)

class EditedChanelPostHandlerSetup(SetupMixin):
    def setup(self, bot):
        bot.add_edited_chanel_post_handler(self)