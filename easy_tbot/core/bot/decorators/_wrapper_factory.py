import inspect
from functools import  update_wrapper
from ..setups.base import SetupMixin

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
                
            def setup(self, bot):
                return base_class.setup(self, bot)
        
        class AsyncWrapper(Wrapper):
            async def __call__(self, *args, **kwargs):
                return await f(*args, **kwargs)

        class SyncWrapper(Wrapper):
            def __call__(self, *args, **kwargs):
                return f(*args, **kwargs)

        return AsyncWrapper if inspect.iscoroutinefunction(f) else SyncWrapper
    return decorator