from itertools import zip_longest
def f(height, width, starting_with = 'A'):
    '''
    >>> f(0, 0)
    >>> f(4, 1)
    A
    B
    C
    D
    >>> f(1, 4)
    ABCD
    >>> f(4, 4, 'X')
    XEFM
    YDGL
    ZCHK
    ABIJ
    '''
    count = 0
    results = []
    starts_ascii = ord(starting_with)
    for i in range(width):
        visited = []
        for j in range(height):
            if count + starts_ascii <=90:
                visited.append(chr(starts_ascii+count))
                count += 1
            else:
                visited.append(chr((starts_ascii+count-91)%26+65))
                count += 1
        results.append(visited)
    new_results = []
    for e in range(len(results)):
        if e % 2 == 0:
            new_results.append(results[e])
        elif e % 2 == 1:
            new_line = results[e]
            new_results.append(new_line[::-1])
    for result in zip_longest(*new_results):
        print(''.join(result))
if __name__ == '__main__':
    import doctest

    doctest.testmod()