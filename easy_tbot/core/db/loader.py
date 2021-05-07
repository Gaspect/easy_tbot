from abc import ABCMeta
from .backend import Backend
from ..settings import Settings
from ..tools.meta import MultiMeta
from ..tools.meta_singleton import MetaSingleton


class DataBase(MultiMeta[ABCMeta, MetaSingleton, Backend ]):
    
    def __init__(self):
        settings = Settings()

        if not issubclass(settings.DB['backend'], Backend):
            raise Exception('Database backend has incorrect parent class')

        self.__db = settings.DB['backend'](**settings.DB['config'])

    def __getattribute__(self,name):
        try:
           return super().__getattribute__(name)
        except AttributeError:
            return getattr(self.__db, name)