import re
from abc import ABC, abstractmethod
from functools import cached_property


class SetupMixin(ABC):
    """
    Very base class, of anything that can be setup in a  bot, base class for every handler
    """

    @cached_property
    def meta(self):
        r = r'__\w+__'
        if hasattr(self, 'Meta'):
            return {key:val for key,val in getattr(self,'Meta').__dict__.items() if not re.match(r,key) }
        return {}    
    
    @abstractmethod
    def setup(self, bot):
        """
        Sets this handler in the proper bot
        :return: None
        """
        pass

class HandlerMixing(ABC):
    @abstractmethod
    def __call__(self,*args, **kwargs):
       pass