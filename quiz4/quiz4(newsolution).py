from math import sqrt
def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve #找出素数的函数1
def primes_in_window(size, lower_bound, upper_bound):
    if size > upper_bound - lower_bound + 1:
        print('Window size is too large for these bounds,',
              'leaving it there.'
             )
        return
    sieve = sieve_of_primes_up_to(upper_bound + 1) #找出输入上限之前的所有素数
    max_window_density = sum(1 for i in range(lower_bound, lower_bound + size)
                                   if sieve[i]
                            ) #第一个窗口被有多少个素数
    current_window_density = max_window_density
    starts_of_windows_of_max_density = [lower_bound] #存储具有最大素数密度的窗口起始位置
    for i in range(lower_bound, upper_bound - size + 1): #开始窗口移动，每个窗口应当为（i，i+size-1）
        if sieve[i]: 
            current_window_density -= 1
        if sieve[i + size]:
            current_window_density += 1
        if current_window_density > max_window_density:
            max_window_density = current_window_density
            starts_of_windows_of_max_density = [i + 1] #更新最大素数密度的窗口起始位置
        elif current_window_density == max_window_density:
            starts_of_windows_of_max_density.append(i + 1) #列表
    if max_window_density == 0:
        print(f'There is no prime in a window of size {size}.')
        return
    elif max_window_density == 1:
        print(f'There is at most one prime in a window of size {size}.')
    else:
        print(f'There are at most', max_window_density,
              f'primes in a window of size {size}.'
             )
    index_of_first_prime_in_window = 0
    for i in range(len(starts_of_windows_of_max_density)):
        j = starts_of_windows_of_max_density[i]
        while not sieve[j]:
            j += 1
        if j == index_of_first_prime_in_window:
            continue
        index_of_first_prime_in_window = j
        k = starts_of_windows_of_max_density[i] + size - 1
        while not sieve[k]:
            k -= 1
        print('In some window, the smallest prime is', j,
              'and the largest one is', k, end='.\n'
             )            