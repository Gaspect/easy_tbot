from six import with_metaclass
from .backend import Backend
from ..settings import Settings
from .._meta_singleton import ABCMetaSingleton

class TemplateEngine(with_metaclass(ABCMetaSingleton, Backend)):
    
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