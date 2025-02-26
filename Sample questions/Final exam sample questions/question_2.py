# Will be tested with height a strictly positive integer.


def f(height):
    '''
    >>> f(1)
    0
    >>> f(2)
     0
    123
    >>> f(3)
      0
     123
    45678
    >>> f(4)
       0
      123
     45678
    9012345
    >>> f(5)
        0
       123
      45678
     9012345
    678901234
    >>> f(6)
         0
        123
       45678
      9012345
     678901234
    56789012345
    >>> f(20)
                       0                       1
                      123                      3
                     45678                     5
                    9012345                    7
                   678901234
                  56789012345
                 6789012345678
                901234567890123
               45678901234567890
              1234567890123456789
             012345678901234567890
            12345678901234567890123
           4567890123456789012345678            25
          901234567890123456789012345           27
         67890123456789012345678901234          29
        5678901234567890123456789012345         31
       678901234567890123456789012345678        33
      90123456789012345678901234567890123       35
     4567890123456789012345678901234567890      37
    123456789012345678901234567890123456789     39
    '''
    num = 0
    for i in range(1, height + 1):
        print(' ' * (height - i), end='')
        for _ in range(2 * i - 1):
            print(num, end='')
            num = (num + 1) % 10
        print()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
