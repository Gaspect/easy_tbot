from .base import SetupMixin


class ChanelPostHandler(SetupMixin):
    def setup(self, bot):
        bot.add_chanel_post_handler(self)

class EditedChanelPostHandler(SetupMixin):
    def setup(self, bot):
        bot.add_edited_chanel_post_handler(self)