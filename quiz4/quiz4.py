from math import sqrt
def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve #返回的是一个素数列表
def primes_in_window(size,lower_bond,upper_bond):
    if size > upper_bond - lower_bond:
        print('Too large,giving up')
        return
    sieve = sieve_of_primes_up_to(upper_bond+1)
    sum = 0
    for i in range(lower_bond,lower_bond+size):
        if sieve[i]:
            sum += 1 #记录初值
    max_num = sum #当前质数最多的值
    current_num = sum #记录当前质数值
    start_point_of_max_num = [lower_bond] #质数最多窗口的起始点,因为可能有多个，所以列表
    for i in range (lower_bond,upper_bond- size +1):
        if sieve[i]:
            current_num -= 1
        if sieve[i+size]:
            current_num += 1
        if current_num > max_num:
            max_num = current_num
            start_point_of_max_num = [i+1]
        elif current_num == max_num:
            start_point_of_max_num.append(i+1)
    if len(start_point_of_max_num) == 0:
        print(f'There is no prime in a window of size {size}.')
    elif len(start_point_of_max_num) == 1:
        print(f'There is at most one prime in a window of size {size}.')
    else:
        print(f'There are at most {len(start_point_of_max_num)} primes in a window of size {size}.')
    print(start_point_of_max_num)
    i = 0
    for i in start_point_of_max_num:
        smallest_one = largest_one = None
        for a in range(i, i + size):
            if sieve[a]:
                smallest_one = a
                break
        for j in range(i + size - 1, i - 1, -1):
            if sieve[j]:
                largest_one = j
                break
        print(f'In some window, the smallest prime is {smallest_one} and the largest one is {largest_one}.')
size,lower_bond,upper_bond = input('primes_in_window').split()
size = int(size)
lower_bond = int(lower_bond)
upper_bond = int(upper_bond)
primes_in_window(size,lower_bond,upper_bond)