
def rearrange(number):
    '''
    Returns an integer consisting of all nonzero digits in "number",
    from smallest to largest.

    You can assume that "number" is a valid strictly positive integer.
    
    >>> rearrange(1)
    1
    >>> rearrange(200)
    2
    >>> rearrange(395)
    359
    >>> rearrange(10029001)
    1129
    >>> rearrange(301302004)
    12334
    >>> rearrange(9409898038908908934890)
    33448888889999999
    '''
    str_number = str(number)
    count = 0
    visited = []
    for char in str_number:
        if char != '0':
            count += 1
            visited.append(char)
    visited_sorted = sorted(visited)
    visited_str = ''.join(visited_sorted)
    print(visited_str)
if __name__ == '__main__':
    import doctest
    doctest.testmod()
