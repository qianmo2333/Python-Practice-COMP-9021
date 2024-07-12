def remove_consecutive_duplicates(word):
    '''
    >>> remove_consecutive_duplicates('')
    ''
    >>> remove_consecutive_duplicates('a')
    'a'
    >>> remove_consecutive_duplicates('ab')
    'ab'
    >>> remove_consecutive_duplicates('aba')
    'aba'
    >>> remove_consecutive_duplicates('aaabbbbbaaa')
    'aba'
    >>> remove_consecutive_duplicates('abcaaabbbcccabc')
    'abcabcabc'
    >>> remove_consecutive_duplicates('aaabbbbbaaacaacdddd')
    'abacacd'
    '''
    visited = []
    for i in range(len(word)):
        if not visited or visited[-1]!=word[i]:
            visited.append(word[i])
    visited_list = ''.join(visited)
    print(f"'{visited_list}'")
if __name__ == '__main__':
    import doctest

    doctest.testmod()
