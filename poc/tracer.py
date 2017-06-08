import functools
import inspect
import os
import traceback


def trace(function):
    @functools.wraps(function)
    def traced(*args, **kwds):
        name      = function.__name__
        callargs  = inspect.getcallargs(function, *args, **kwds)
        signature = '%s(%s)' % (name, ', '.join('%s=%r' % item for item in callargs.items()))
        print('calling %s...' % signature)
        try:
            retval = function(*args, **kwds)
            print('%s returned %r' % (name, retval))
            return retval
        except:
            print('%s raised an exceptin:%s%s' % (name, os.linesep, traceback.format_exc().strip()))
            raise
    return traced
