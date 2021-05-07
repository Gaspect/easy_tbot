import types
import sys

# This requires a bit of explanation: The purpose is create a class that can make a dummy
# metaclass for one level of class instantiation that replaces itself with
# the actual metaclass.

class MultiMetaFactory:
    '''
    Factory class that create dummy metaclasses blending multiples metclasses and normal classes.
    '''
    
    def __getitem__(self, base_class):
        """Create a base class with a set of many bases classes, simultaneous metaclass are allowed."""
       
        #We declare a variable for store meta classes
        metas = []

        #and another to store normal base classes
        bases = []
        
        #and now we split them 
        for _class in base_class:
            if issubclass(_class, type):
                metas.append(_class)
            else:
                bases.append(_class)

        # turn the bases list into a tuple
        bases = tuple(bases)

        # and create a base class that inherits from all meta classes filtered
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

# Now we create a instance for easing developers life.
MultiMeta = MultiMetaFactory()