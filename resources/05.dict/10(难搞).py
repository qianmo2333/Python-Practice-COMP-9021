from random import seed, randint
import sys


def f(arg_for_seed, nb_of_elements, max_element):
    '''
    >>> f(0, 0, 10)
    Here is L: []
    >>> f(0, 1, 10)
    Here is L: [6]
    1 element starts with 6
    >>> f(0, 2, 10)
    Here is L: [6, 6]
    2 elements start with 6
    >>> f(1, 2, 100)
    Here is L: [17, 72]
    1 element starts with 1
    1 element starts with 7
    >>> f(2, 3, 1000)
    Here is L: [978, 883, 970]
    1 element starts with 8
    2 elements start with 9
    >>> f(8, 6, 1000)
    Here is L: [232, 379, 985, 384, 129, 197]
    2 elements start with 1
    1 element starts with 2
    2 elements start with 3
    1 element starts with 9
    >>> f(20, 8, 10000)
    Here is L: [2477, 4257, 1663, 5364, 9387, 2775, 442, 6742]
    1 element starts with 1
    2 elements start with 2
    2 elements start with 4
    1 element starts with 5
    1 element starts with 6
    1 element starts with 9
    '''
    seed(arg_for_seed)
    L = [randint(0, max_element) for _ in range(nb_of_elements)]
    print('Here is L:', L)
    dic_char = {}
    for char in L:
        str_char = str(char)[0]
        if str_char not in dic_char:
            dic_char[str_char] = 1
        else:
            dic_char[str_char] += 1
    
    for k in sorted(dic_char):
        count = dic_char[k]
        if count == 1:
            print(f'{count} element starts with {k}')
        if count > 1:
            print(f'{count} elements start with {k}')

if __name__ == '__main__':
    import doctest

    doctest.testmod()
