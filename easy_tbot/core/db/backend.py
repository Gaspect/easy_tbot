from abc import ABC, abstractmethod

class Backend(ABC):
    
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass