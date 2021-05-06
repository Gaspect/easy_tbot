from .base import HandlerMixing, SetupMixin


class ChanelPostHandler(HandlerMixing, SetupMixin):
    def setup(self, bot):
        bot.add_chanel_post_handler(self)

class EditedChanelPostHandler(HandlerMixing, SetupMixin):
    def setup(self, bot):
        bot.add_edited_chanel_post_handler(self)