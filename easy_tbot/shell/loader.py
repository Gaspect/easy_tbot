import inspect
from six import with_metaclass
from importlib import import_module
from .backend import Backend
from ..settings import Settings
from ..tools.meta import ABCMetaSingleton


class Shell(with_metaclass(ABCMetaSingleton, Backend)):

    def __init__(self):
        settings  = Settings()

        if not issubclass(settings.SHELL['backend'], Backend):
            raise Exception('Shell backend has incorrect parent class')

        self.__shell = settings.SHELL['backend'](**settings.SHELL['config'])
        settings.setup_apps(self.setup_app)

    def __getattribute__(self,name):
        try:
           return super().__getattribute__(name)
        except AttributeError:
            return getattr(self.__shell, name)
        
    def setup_app(self, app):
        module = import_module(f'{app}.shells')
        for name, value in inspect.getmembers(module, inspect.isclass):
            if self.type_is_command(value):
                self.add_command(value())

    def type_is_command(self, obj_type):
        return self.__shell.type_is_command(obj_type)

    def add_command(self, command):
        return self.__shell.add_command(command)

    def add_commands(self, *args):
        return self.__shell.add_commands(*args)

    def handle_input(self, *args):
        return self.__shell.handle_input(*args)