from .base import SetupMixin, HandlerMixing

class Middleware(HandlerMixing, SetupMixin):
    def setup(self, bot):
        bot.add_middleware_handler(self)
        
