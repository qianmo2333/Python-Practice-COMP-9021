def f(word):
    '''
    Recall that if c is an ascii character then ord(c) returns its ascii code.
    Will be tested on nonempty strings of lowercase letters only.

    >>> f('x')
    The longest substring of consecutive letters has a length of 1.
    The leftmost such substring is x.
    >>> f('xy')
    The longest substring of consecutive letters has a length of 2.
    The leftmost such substring is xy.
    >>> f('ababcuvwaba')
    The longest substring of consecutive letters has a length of 3.
    The leftmost such substring is abc.
    >>> f('abbcedffghiefghiaaabbcdefgg')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is bcdefg.
    >>> f('abcabccdefcdefghacdef')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is cdefgh.
    '''
    count = 0
    visited = []
    small_list = []
    for i in range(len(word)):
        if not small_list or ord(word[i])-1 == ord(small_list[-1]):
            small_list.append(word[i])
            if len(small_list) > len(visited):
                visited = small_list
                count = len(visited)
            elif len(small_list) <= len(visited):
                count = len(visited)
        elif ord(word[i])-1 != ord(small_list[-1]):
            small_list = [word[i]]
    visited_list = ''.join(visited)
    print(f'The longest substring of consecutive letters has a length of {count}.')
    print(f'The leftmost such substring is {visited_list}.')
if __name__ == '__main__':
    import doctest

    doctest.testmod()
