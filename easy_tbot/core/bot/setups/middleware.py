from .base import SetupMixin

class MiddlewareSetup(SetupMixin):
    def setup(self, bot):
        bot.add_middleware_handler(self)
        
