from __future__ import print_function

import functools
import inspect
import os
import sys
import traceback


INDENT = '  '
indent = 0


def trace(function=None, log=None):
    # Decorator called as @trace(log=...), affix log and return the decorator.
    if function is None:
        return functools.partial(trace, log=log)
    # Define the tracer (this happens here so we get log by scope).
    if log is None:
        log = print
    def tracer(frame, event, arg):
        global indent
        name = frame.f_code.co_name
        if event == 'call':
            args      = inspect.getargvalues(frame)
            signature = name + inspect.formatargvalues(*args)
            log(INDENT*indent + 'calling %s' % signature)
            indent += 1
        if event == 'return':
            indent -= 1
            log(INDENT*indent + '%s returned %r' % (name, arg))
        if event == 'exception':
            tb = ''.join(traceback.format_exception(*arg)).strip()
            tb = os.linesep.join(INDENT*indent + line for line in tb.splitlines())
            log(INDENT*indent + '%s raised an exception:%s%s' % (name, os.linesep, tb))
        return tracer
    # Decorate the function.
    @functools.wraps(function)
    def traced(*args, **kwds):
        try:
            old = sys.gettrace()
            sys.settrace(tracer)
            return function(*args, **kwds)
        finally:
            sys.settrace(old)
    return traced
