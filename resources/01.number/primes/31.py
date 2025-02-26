from itertools import compress,accumulate
from math import sqrt
import operator
def sieve_of_primes_up_to(n):
   sieve = [True] * (n + 1)
   for p in range(2, round(sqrt(n)) + 1):
      if sieve[p]:
         for i in range(p * p, n + 1, p):
            sieve[i] = False
   return sieve
def single_factors(number):
    '''
    Returns the product of the prime divisors of "number"
    (using each prime divisor only once).

    You can assume that "number" is an integer at least equal to 2.

    >>> single_factors(2)
    2
    >>> single_factors(4096)                 # 4096 == 2**12
    2
    >>> single_factors(85)                   # 85 == 5 * 17
    85
    >>> single_factors(10440125)             # 10440125 == 5**3 * 17**4
    85
    >>> single_factors(154)                  # 154 == 2 * 7 * 11
    154
    >>> single_factors(52399401037149926144) # 52399401037149926144 == 2**8 * 7**2 * 11**15
    154
    '''
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
