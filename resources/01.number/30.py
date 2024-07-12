from math import sqrt


def f(n, d):
    '''
    >>> f(2, 1)
    1 is not a proper factor of 2.
    >>> f(2, 2)
    2 is not a proper factor of 2.
    >>> f(16, 2)
    2 is a proper factor of 16 of mutiplicity 4.
    >>> f(100, 20)
    20 is a proper factor of 100 of mutiplicity 1.
    >>> f(8 ** 7 * 3 ** 5 * 11 ** 2, 8)
    8 is a proper factor of 61662560256 of mutiplicity 7.
    >>> f(3 ** 3 * 11 * 13 ** 2 * 40 ** 6, 8)
    8 is a proper factor of 205590528000000 of mutiplicity 6.
    '''
    n_int_show = int(n)
    n_int = int(n)
    count = 0
    if n_int_show == d:
        print(f'{n_int_show} is not a proper factor of {d}.')
    elif d == 1:
        print(f'{d} is not a proper factor of {n_int_show}.')
    else:
        for _ in range(n_int_show):
            if n_int %d == 0:
                count += 1
                n_int = n_int / d
            elif n_int %d !=0:
                break
        print(f'{d} is a proper factor of {n_int_show} of mutiplicity {count}.')

if __name__ == '__main__':
    import doctest

    doctest.testmod()
