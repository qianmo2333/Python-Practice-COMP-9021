import sys
from math import sqrt
from itertools import compress

from itertools import chain
def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve
def f(n):
    '''
    Won't be tested for n greater than 10_000_000
    
    >>> f(3)
    The largest prime strictly smaller than 3 is 2.
    >>> f(10)
    The largest prime strictly smaller than 10 is 7.
    >>> f(20)
    The largest prime strictly smaller than 20 is 19.
    >>> f(210)
    The largest prime strictly smaller than 210 is 199.
    >>> f(1318)
    The largest prime strictly smaller than 1318 is 1307.
    '''
    if n <= 2:
        sys.exit()
    prime_list = sieve_of_primes_up_to(n)
    for i in range(len(prime_list)-2,1,-1):
        if prime_list[i] == True:
            print(f'The largest prime strictly smaller than {n} is {i}.')
            break

if __name__ == '__main__':
    import doctest
    doctest.testmod()
