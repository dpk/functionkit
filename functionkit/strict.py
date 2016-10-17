from functools import wraps

__all__ = ('strictify', 'listify', 'dictify', 'setify')


def strictify(klass):
    def typify(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            return klass(f(*args, **kwargs))
        return wrapper
    return typify

listify = strictify(list)
dictify = strictify(dict)
setify = strictify(set)
