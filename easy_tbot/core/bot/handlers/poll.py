from .base import HandlerMixing, SetupMixin

class PollHandler(HandlerMixing, SetupMixin):
    def setup(self, bot):
        bot.add_poll_handler(self)

class PollAnswerHandler(HandlerMixing, SetupMixin):
    def setup(self, bot):
        bot.add_poll_answer_handler(self)