'''
safe_call takes a function and key-word arguments for it
and if the format mathces it invokes it with the input
else it raises an approporiate error

'''


def test1():
    
    '''
    >>> safe_call(func1, a = 1, b = 2, c = 'hi')
    hihihi

    >>> safe_call(func1, a = 1)
    Traceback (most recent call last):
        ...
    ctypes.ArgumentError: func1 accpects 3 arguments, 1 were given

    >>> safe_call(func1, a = 1, b = 2., c = 'hi')
    Traceback (most recent call last):
        ...
    TypeError: argument b should be of type <class 'int'>

    >>> safe_call(func1, a = 1, d = 2., c = 'hi')
    Traceback (most recent call last):
        ...
    KeyError: 'wrong key-word argument d'

    >>> safe_call(func1, a = 1, b = 2., c = 'hi', d = True)
    Traceback (most recent call last):
        ...
    ctypes.ArgumentError: func1 accpects 3 arguments, 4 were given
    '''
    
def test2():

    '''
    >>> safe_call(func2, x = 13, y = [])
    13

    >>> safe_call(func2)
    Traceback (most recent call last):
        ...
    ctypes.ArgumentError: func2 accpects 2 arguments, 0 were given

    >>> safe_call(func2, x = 1, y = 2.222, z = (3,))
    Traceback (most recent call last):
        ...
    ctypes.ArgumentError: func2 accpects 2 arguments, 3 were given

    >>> safe_call(func2, x = 1, z = 2.222)
    Traceback (most recent call last):
        ...
    KeyError: 'wrong key-word argument z'

    >>> safe_call(func2, x = 'abc', y = {1:{}})
    Traceback (most recent call last):
        ...
    TypeError: argument x should be of type <class 'int'>
    '''



if __name__ == "__main__":

    from sol import safe_call
    import doctest

    def func1(a: int, b: int, c: str) -> float: print(c * (a + b))
    def func2(x: int, y): return x

    doctest.testmod(verbose = True)