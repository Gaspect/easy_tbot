from .base import  SetupMixin

class PollHandlerSetup(SetupMixin):
    def setup(self, bot):
        bot.add_poll_handler(self)

class PollAnswerHandlerSetup(SetupMixin):
    def setup(self, bot):
        bot.add_poll_answer_handler(self)