from .base import  SetupMixin

class PollHandler(SetupMixin):
    def setup(self, bot):
        bot.add_poll_handler(self)

class PollAnswerHandler(SetupMixin):
    def setup(self, bot):
        bot.add_poll_answer_handler(self)