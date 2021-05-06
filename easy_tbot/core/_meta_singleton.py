from abc import ABCMeta

class MetaSingleton(type):
    instances = {}
    def __call__(cls, *args, **kwargs):
        if not cls in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]

class ABCMetaSingleton(ABCMeta, MetaSingleton):
    pass



