try:
    import jinja2
except Exception as e:
    raise e

from .backend import JinjaBackend