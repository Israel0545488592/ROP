from ctypes import ArgumentError
from typing import Callable

def safe_call(f: Callable, **kwards):
    
    arguments = f.__code__.co_varnames
    annotations = f.__annotations__

    if len(arguments) != len(kwards):
        raise ArgumentError('{} accpects {} arguments, {} were given'.format(f.__name__, len(arguments), len(kwards)))
    
    for k in kwards.keys():

        if k not in arguments:
            raise KeyError('wrong key-word argument {}'.format(k))

        if k in annotations:
            if annotations[k] is not type(kwards[k]):
                raise TypeError('argument {} should be of type {}'.format(k, annotations[k]))

    return f(**kwards)


if __name__ == '__main__':

    def func(a: int, b: float, c: str, d: bool) -> None:
        if d:
            return c + str(a + b) 

    print(safe_call(func, a = 1, b = 2., c = '3', d = True))

    try:
        safe_call(func, a = 1)
    except ArgumentError as e:
        print(e)
    try:
        safe_call(func, a = 1, b = 2, c = '3', d = True)
    except TypeError as e:
        print(e)
    try:
        safe_call(func, a = 1, e = 2, c = '3', d = True)
    except KeyError as e:
        print(e)