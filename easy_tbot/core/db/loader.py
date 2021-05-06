from six import with_metaclass
from .backend import Backend
from ..settings import Settings
from .._meta_singleton import ABCMetaSingleton


class DataBase(with_metaclass(ABCMetaSingleton, Backend)):
    def __init__(self):
        # load here
        settings = Settings()

        if not issubclass(settings.DB['backend'], Backend):
            raise Exception('Database backend has incorrect parent class')

        self.__db = settings.DB['backend'](**settings.DB['config'])

    def __getattribute__(self,name):
        try:
           return super().__getattribute__(name)
        except AttributeError:
            return getattr(self.__db, name)