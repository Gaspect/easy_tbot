import types
import sys

class MultiMeta:
    
    @classmethod
    def __getitem__(cls, *args):
        """Create a base class with a metaclass."""
        # This requires a bit of explanation: the basic idea is to make a dummy
        # metaclass for one level of class instantiation that replaces itself with
        # the actual metaclass.
        metas = []
        bases = []
        for _class in args:
            if issubclass(_class, type):
                metas.append(_class)
            else:
                bases.append(_class)

        class meta_mix(*metas):
            pass


        class metaclass(type):

            def __new__(cls, name, this_bases, d):
                if sys.version_info[:2] >= (3, 7):
                    # This version introduced PEP 560 that requires a bit
                    # of extra care (we mimic what is done by __build_class__).
                    resolved_bases = types.resolve_bases(bases)
                    if resolved_bases is not bases:
                        d['__orig_bases__'] = bases
                else:
                    resolved_bases = bases
                return meta_mix(name, resolved_bases, d)

            @classmethod
            def __prepare__(cls, name, this_bases):
                return meta_mix.__prepare__(name, bases)

        return type.__new__(metaclass, 'temporary_class', (), {})

