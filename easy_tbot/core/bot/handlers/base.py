from abc import ABC, abstractmethod

class HandlerMixing(ABC):
    @abstractmethod
    def __call__(self,*args, **kwargs):
       pass