from tracer import trace

@trace
def div(x, y):
    return do_div(x, y)


def do_div(x, y):
    return x / y


div(4, 2)
try:
    div(1, 0)
except ZeroDivisionError:
    pass
