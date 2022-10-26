from collections.abc import Iterable

def infloop(iterable):
    if not isinstance(iterable, Iterable):
        raise TypeError('parameter should be Iterable.')

    while True:
        for x in iterable:
            yield x