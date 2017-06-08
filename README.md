# Tracer

A decorator to trace function execution.

```python
from tracer import trace

@trace
def div(x, y):
    return do_div(x, y)


def do_div(x, y):
    return x / y


div(4, 2)
div(1, 0)
```

```console
$ python demo.py
calling div(x=4, y=2)
  calling do_div(x=4, y=2)
  do_div returned 2
div returned 2
calling div(x=1, y=0)
  calling do_div(x=1, y=0)
    do_div raised an exception:
    Traceback (most recent call last):
      File "example/demo.py", line 9, in do_div
        return x / y
    ZeroDivisionError: integer division or modulo by zero
  do_div returned None
  div raised an exception:
  Traceback (most recent call last):
    File "example/demo.py", line 5, in div
      return do_div(x, y)
    File "example/demo.py", line 9, in do_div
      return x / y
  ZeroDivisionError: integer division or modulo by zero
div returned None
```
