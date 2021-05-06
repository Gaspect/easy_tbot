import typing
from aiogram import Bot, Dispatcher, executor
from easy_tbot.core.bot.backend import Backend
from easy_tbot.core.bot.handlers.base import SetupMixin
from .middleware_wrapper import MiddlewareWrapper

class AiogramBackend(Backend):
    def __init__(self, *args, **kwargs):
        
        self.__skip_updates = False
        if 'skip_updates' in kwargs:
            self.__skip_updates = kwargs['skip_updates']
            del kwargs['skip_updates']

        self.__bot = Bot(*args, **kwargs)
        self.__dispatcher = Dispatcher(self.__bot)

    @property
    def bot(self):
        return self.__bot

    @property
    def dispatcher(self):
        return self.__dispatcher
    
    @staticmethod
    def __add(handler:SetupMixin, decorator:typing.Callable):
        # for function , class compatibility
        kwargs = handler.meta
        args = kwargs.pop('args',[])
        if not args:
            args = kwargs.pop('custom_filters', [])
        return decorator(*args, **kwargs)(handler)
    
    def add_middleware_handler(self, handler):
        self.dispatcher.setup_middleware(MiddlewareWrapper(handler))
    
    def add_message_handler(self, handler):
        decorator = self.dispatcher.message_handler
        return self.__add(handler, decorator)
    
    def add_edited_message_handler(self, handler):
        decorator = self.dispatcher.edited_message_handler
        return self.__add(handler, decorator)

    def add_chanel_post_handler(self, handler):
        decorator = self.dispatcher.channel_post_handler
        return self.__add(handler, decorator)

    def add_edited_chanel_post_handler(self, handler):
        decorator  = self.dispatcher.edited_channel_post_handler
        return self.__add(handler, decorator)
    
    def add_inline_handler(self,handler):
        decorator = self.dispatcher.inline_handler
        return self.__add(handler, decorator)

    def add_chosen_inline_handler(self, handler):
        decorator = self.dispatcher.chosen_inline_handler
        return self.__add(handler, decorator)

    def add_callback_query_handler(self, handler):
        decorator = self.dispatcher.callback_query_handler
        return self.__add(handler, decorator)

    def add_shipping_query_handler(self, handler):
        decorator  = self.dispatcher.shipping_query_handler
        return self.__add(handler, decorator)
    
    def add_pre_checkout_query_handler(self, handler):
        decorator = self.dispatcher.pre_checkout_query_handler
        return self.__add(handler, decorator)

    def add_poll_handler(self, handler):
        decorator  = self.dispatcher.poll_handler
        return self.__add(handler, decorator)

    def add_poll_answer_handler(self, handler):
        decorator  = self.dispatcher.poll_answer_handler
        return self.__add(handler, decorator)

    def run(self, *args, **kwargs):
        return executor.start_polling(self.dispatcher, skip_updates=self.__skip_updates)