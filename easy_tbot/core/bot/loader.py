from abc import ABCMeta
import inspect
from importlib import import_module
from .backend import Backend
from .setups.base import SetupMixin
from ..settings import Settings
from ..tools.meta import MultiMeta
from ..tools.meta_singleton import MetaSingleton



class Bot(MultiMeta[ABCMeta, MetaSingleton, Backend ]):

    def __init__(self):
        settings = Settings()

        if not issubclass(settings.BOT['backend'], Backend):
            raise Exception('Bot backend has incorrect parent class')

        self.__bot:Backend = settings.BOT['backend'](**settings.BOT['config'])
        settings.setup_apps(self.setup_app)

    def setup_app(self, app):
        lmodule = import_module(f"{app}.handlers")
        for name, value in inspect.getmembers(lmodule, inspect.isclass):
            if issubclass(value,SetupMixin) and not inspect.isabstract(value):
                value().setup(self)
    
    def __getattribute__(self,name):
        try:
           return super().__getattribute__(name)
        except AttributeError:
            return getattr(self.__bot, name)
    
    
    def add_middleware(self,middleware):
        return self.__bot.add_middleware(middleware)

    def add_message_handler(self, message_handler):
        return self.__bot.add_message_handler(message_handler)

    def add_edited_message_handler(self, edited_message_handler):
        return self.__bot.add_edited_message_handler(edited_message_handler)

    def add_chanel_post_handler(self, ch_post_handler):
        return self.__bot.add_chanel_post_handler(ch_post_handler)

    def add_edited_chanel_post_handler(self, ch_post_handler):
        return self.__bot.add_edited_chanel_post_handler(ch_post_handler)
    
    def add_inline_handler(self,inline_handler):
        return self.__bot.add_inline_handler(inline_handler)
    
    def add_chosen_inline_handler(self, chosen_inline_handler):
        return self.__bot.add_chosen_inline_handler(chosen_inline_handler)

    def add_callback_query_handler(self, callback_query_handler):
        return self.__bot.add_callback_query_handler(callback_query_handler)

    def add_shipping_query_handler(self, shipping_query_handler):
        return self.__bot.add_shipping_query_handler(shipping_query_handler)
    
    def add_pre_checkout_query_handler(self, pre_checkout_query_handler):
        return self.__bot.add_pre_checkout_query_handler(pre_checkout_query_handler)

    def add_poll_handler(self, poll_handler):
        return self.__bot.add_poll_handler(poll_handler)

    def add_poll_answer_handler(self, poll_answer_handler):
        return self.__bot.add_poll_answer_handler(poll_answer_handler)

    def run(self, *args, **kwargs):
        return self.__bot.run(*args, **kwargs)