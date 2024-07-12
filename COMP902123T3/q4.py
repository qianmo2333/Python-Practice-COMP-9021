from itertools import zip_longest
def f(height, width, starting_with = 'A'):
    '''
    >>> f(0, 0)
    >>> f(4, 1)
    A
    B
    C
    D
    >>> f(5, 1)
    A
    B
    C
    D
    E
    >>> f(1, 4)
    ABCD
    >>> f(4, 4, 'X')
    XEFM
    YDGL
    ZCHK
    ABIJ
    >>> f(1, 5)
    ABCDE
    >>> f(5, 4, 'X')
    XGHQ
    YFIP
    ZEJO
    ADKN
    BCLM
    '''
    count = 0
    results = []
    prime_ascii = ord(starting_with)
    for _ in range(width):
        result = []
        for _ in range(height):
            if prime_ascii + count <= 90:
                result.append(chr(prime_ascii+count))
            else:
                result.append(chr(((prime_ascii+count-91)%26)+65))
            count += 1
        results.append(result)
    new_result = []
    for i in range(len(results)):
        if i%2 == 0:
            new_result.append(results[i])
        if i%2 == 1:
            line = results[i]
            new_result.append(line[::-1])
    for element in zip_longest(*new_result,fillvalue = ''):
        print(''.join(element).strip())
if __name__ == '__main__':
    import doctest

    doctest.testmod()