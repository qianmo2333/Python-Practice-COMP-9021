from itertools import zip_longest
def f(*x):
    '''
    >>> f(0, 0, 0)
    >>> f(1, 2, 3)
        *
      * *
    * * *
    >>> f(1, 2, 1, 0, 0, 0)
      *
    * * *
    >>> f(0, 2, 3, 4)
          *
        * *
      * * *
      * * *
    >>> f(4)
    *
    *
    *
    *
    >>> f(4, 4, 4)
    * * *
    * * *
    * * *
    * * *
    >>> f(4, 0, 2, 2)
    *
    *
    *   * *
    *   * *
    '''
    items = []
    for item in x:
        items.append(item)
    length = len(items)
    width = max(items)
    results = []
    for i in range(length):
        result = ' '*(width-items[i])+'*'*(items[i])
        results.append(result)
    for element in zip_longest(*results):
        print(' '.join(element).rstrip())
if __name__ == '__main__':
    import doctest
    doctest.testmod()
