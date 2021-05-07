from .base import SetupMixin

class Middleware(SetupMixin):
    def setup(self, bot):
        bot.add_middleware_handler(self)
        
