from jinja2 import FileSystemLoader, Environment, select_autoescape
from easy_tbot.core.render.backend import Backend


class JinjaBackend(Backend):
    def __init__(self, templates:list, allowed_extensions:list):
        autoescape = select_autoescape(allowed_extensions)
        self.__env = Environment(loader=FileSystemLoader(searchpath=templates), autoescape=autoescape)
    
    def render(self, template,*args, **kwargs):
        return self.__env.get_template(template).render(*args, **kwargs)