from abc import ABCMeta
from .backend import Backend
from ..settings import Settings
from ..tools.meta import MultiMeta
from ..tools.meta_singleton import MetaSingleton


class TemplateEngine(MultiMeta[ABCMeta, MetaSingleton, Backend ]):
    
    def __init__(self):
        settings = Settings()
        
        if not issubclass(settings.TEMPLATE_ENGINE['backend'],Backend):
            raise Exception('Render backend has incorrect parent class')

        self.__tengine = settings.TEMPLATE_ENGINE['backend'](**settings.TEMPLATE_ENGINE['config'])

        
    def __getattribute__(self,name):
        try:
           return super().__getattribute__(name)
        except AttributeError:
            return getattr(self.__tengine, name)

    def render(self, template, *args, **kwargs):
        return self.__tengine.render(template, *args, **kwargs)