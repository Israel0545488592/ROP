from math import ceil
from typing import Iterable

def print_sorted(cont: Iterable):

    def hyrarcy(x):
        return ceil(x) if type(x) in [int, float] else len(str(x))

    if isinstance(cont, dict):

        print('{', end = ' ')

        keys = sorted(cont.keys(), key = hyrarcy)
        for i in range(len(keys)):

            print(keys[i], ' :', end = ' ')
            print_sorted(cont[keys[i]])
            if i != len(keys) -1:
                print(',', end = ' ')

        print('}', end = ' ')

    elif isinstance(cont, set) or isinstance(cont, list) or isinstance(cont, tuple):

        if isinstance(cont, set):
            print('{', end = ' ')
        if isinstance(cont, list):
            print('[', end = ' ')
        if isinstance(cont, tuple):
            print('(', end = ' ')
        
        items = sorted(cont, key = hyrarcy)
        for i in range(len(items)):

            print_sorted(items[i])
            if i != len(items) -1:
                print(',', end = ' ')

        if isinstance(cont, set):
            print('}', end = ' ')
        if isinstance(cont, list):
            print(']', end = ' ')
        if isinstance(cont, tuple):
            print(')', end = ' ')

    else:
        print(cont, end = ' ')


if __name__ == '__main__':

    print_sorted([10, 2, [3, (1, [2, -1], 3), 2]]) 
