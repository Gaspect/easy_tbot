from .loader import TemplateEngine

def render(template, *args, **kwargs):
    return TemplateEngine().render(template, *args, **kwargs)