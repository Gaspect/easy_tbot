import os
from importlib import import_module
from typing import Callable, Any
import logging

class Settings:
    def __init__(self, settings:dict = None):
        if settings is None:
            self.__settings  = import_module(os.environ.get('BOT_SETTING_MODULE'))
        else:
            self.__settings = settings

    def __getattribute__(self, name):
        try:
            return super().__getattribute__(name)
        except AttributeError:
            if isinstance(self.__settings, dict):
                return self.__settings[name]
            else:
                return getattr(self.__settings,name)

    def setup_apps(self, configurator:Callable[..., Any]):
        setup = logging.getLogger('tbot')
            
        for app in self.FRAGMENTS:
            try:
                configurator(app)
            except ImportError as e:
                setup.log(logging.WARNING, str(e))
            except Exception as e:
                setup.log(logging.ERROR, str(e))
                raise e