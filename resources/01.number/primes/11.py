import sys
from itertools import compress
from math import sqrt

from itertools import chain

def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve
def f(a, b):
    '''
    The prime numbers between 2 and 12 (both included) are: 2, 3, 5, 7, 11
    The gaps between successive primes are: 0, 1, 1, 3.
    Hence the maximum gap is 3.
    
    Won't be tested for b greater than 10_000_000
    
    >>> f(3, 3)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 4)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 5)
    The maximum gap between successive prime numbers in that interval is 1
    >>> f(2, 12)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(5, 23)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(20, 106)
    The maximum gap between successive prime numbers in that interval is 7
    >>> f(31, 291)
    The maximum gap between successive prime numbers in that interval is 13
    '''
    if a <= 0 or b < a:
        sys.exit()
    max_gap = 0
    prime_list = sieve_of_primes_up_to(b)
    new_list = prime_list[a:]
    for i in range(len(new_list)):
        if new_list[i] == True:
            for j in range(i+1,len(new_list)):
                if new_list[j] == True:
                    minus = j-i-1
                    if minus > max_gap:
                        max_gap = minus
                        break
                    else:
                        break
                else:
                    continue
        else:
            continue
    print(f"The maximum gap between successive prime numbers in that interval is {max_gap}")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
