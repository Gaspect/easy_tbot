import inspect
from functools import  update_wrapper
from ..handlers.base import SetupMixin

def create_wrapper(base_class, *args, **kwargs):
    def decorator(f):
        class Wrapper(SetupMixin):
            
            def __init__(self):
                update_wrapper(self, f)

            @property
            def meta(self):
                d = {'args':args}
                d.update(kwargs)
                return d

            async def __call__(self, *args, **kwargs):
                if inspect.iscoroutinefunction(f):
                    return await f(*args, **kwargs)
                return f(*args, **kwargs)
                
            def setup(self, bot):
                return base_class.setup(self, bot)

        return Wrapper
    return decorator