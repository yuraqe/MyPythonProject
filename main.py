import functools


def recviz(func):
    level = -1

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal level
        level += 1

        pos_args = list(map(repr, args))
        keyword_args = [f'{k}={v!r}' for k, v in kwargs.items()]

        print('    ' * level + '->', f'{func.__name__}({", ".join(pos_args + keyword_args)})')
        value = func(*args, **kwargs)
        print('    ' * level + '<-', repr(value))

        level -= 1
        return value

    return wrapper


@recviz
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


fact(5)