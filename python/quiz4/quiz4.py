from math import sqrt

def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve

def primes_in_window(size, lower_bound, upper_bound):
    current_prime = 0
    sieve = sieve_of_primes_up_to(upper_bound)
    for i in range(lower_bound,lower_bound+size):
        if sieve[i]:
            current_prime += 1
    max_prime = current_prime
    start_window = [lower_bound]
    for j in range(lower_bound,upper_bound-size+1):
        if sieve[j]:
            current_prime -=1
        if sieve[j+size]:
            current_prime +=1
        if current_prime > max_prime:
            max_prime = current_prime
            start_window = [j+1]
        elif current_prime == max_prime:
            start_window.append(j+1)
    if max_prime == 0:
        print(f'There is no prime in a window of size {size}.')
        return
    elif max_prime == 1:
        print(f'There is at most one prime in a window of size {size}.')
    else:
        print(f'There are at most', max_prime,
              f'primes in a window of size {size}.'
             )
    for m in range(len(start_window)):
        n = start_window[m]
        while not sieve[n]:
            n += 1
        k = start_window[m]+size-1
        while not sieve[k]:
            k -= 1
        print('In some window, the smallest prime is', n,
              'and the largest one is', k, end='.\n'
             )
primes_in_window(2,2,7)