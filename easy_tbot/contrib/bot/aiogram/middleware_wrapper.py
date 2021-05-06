from aiogram.dispatcher.middlewares import BaseMiddleware
import functools
import inspect

class MiddlewareWrapper(BaseMiddleware):
    __middlewares = []

    def __init__(self, func):
        super().__init__()
        self.__func = func
        self.add_instance(func)
        functools.update_wrapper(self,self.__func)

    def setup(self, manager):
        self.__class__.__middlewares.append(self.__func)
        self._manager = manager

    def __getattribute__(self, name):
        if name == 'on_process_message':
            return self
        
        try:
            return super().__getattribute__(name)
        
        except AttributeError:
            return getattr(self.__func, name)
    
    def is_configured(self):
        return self.__func in self.__middlewares

    async def __call__(self, *args, **kwargs):
        if inspect.iscoroutinefunction(self.__func):
            return await self.__func(*args, **kwargs)
        return self.__func(*args, **kwargs)