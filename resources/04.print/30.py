# ord(c) returns the encoding of character c.
# chr(e) returns the character encoded by e.


def rectangle(width, height):
    '''
    Displays a rectangle by outputting lowercase letters, starting with a,
    in a "snakelike" manner, from left to right, then from right to left,
    then from left to right, then from right to left, wrapping around when z is reached.
    
    >>> rectangle(1, 1)
    a
    >>> rectangle(2, 3)
    ab
    dc
    ef
    >>> rectangle(3, 2)
    abc
    fed
    >>> rectangle(17, 4)
    abcdefghijklmnopq
    hgfedcbazyxwvutsr
    ijklmnopqrstuvwxy
    ponmlkjihgfedcbaz
    '''
    e = i = 0
    f = 0
    for j in range(height):
        if j % 2 == 0:
            for i in range(width):
                print(chr((i+f)%26+97),end='')
            print()
            f += width
        else:
            for e in range(width-1,-1,-1):
                print(chr((e+f)%26+97),end='')
            f += width
            print()
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
