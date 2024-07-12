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
    visited = []
    length = max(x)
    for item in x:
      visited.append(' '*(length-item)+'*'*item)
    for result in zip_longest(*visited):
      print(' '.join(result).rstrip())
if __name__ == '__main__':
    import doctest

    doctest.testmod()
