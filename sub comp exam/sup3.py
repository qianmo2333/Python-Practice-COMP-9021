def reduce(x):
    '''
    >>> reduce(0)
    >>> reduce(1)
    >>> reduce(12345)
    1 + 2 + 3 + 4 + 5 = 15
    1 + 5 = 6
    >>> reduce(123456)
    123 + 456 = 579
    5 + 7 + 9 = 21
    2 + 1 = 3
    >>> reduce(123456789)
    123 + 456 + 789 = 1368
    13 + 68 = 81
    8 + 1 = 9
    >>> reduce(3559327975051749)
    3559 + 3279 + 7505 + 1749 = 16092
    1 + 6 + 0 + 9 + 2 = 18
    1 + 8 = 9
    '''
    div_number = []
    str_x = str(x)
    for i in range(1,len(str_x)):
        if len(str_x) % i == 0:
            div_number.append(i)
    print(div_number)
    results = []
    for element in div_number:
        j = 0
        result = 0
        for _ in range(int(len(str_x)/element)):
            small_num = str_x[j:j+element]
            result += int(small_num)
            j += element
        results.append(result)
    print(results)


if __name__ == '__main__':
    import doctest

    doctest.testmod()