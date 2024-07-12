from fractions import Fraction

def f(L, window_size=1):
    '''
    >>> f([1,2,3,4,5])
    The max average in the window size of 1 is 5.
    Find on the index 4 : 5
    >>> f([0,3,6,8,3,6,9,6,7,9])
    The max average in the window size of 1 is 9.
    Find on the index 6 : 9
    Find on the index 9 : 9
    >>> f([6,6],2)
    The max average in the window size of 2 is 6.
    Find on the indexes between 0 and 1 : 6--6
    >>> f([6,2,3,4,7],2)
    The max average in the window size of 2 is 11/2.
    Find on the indexes between 3 and 4 : 4--7
    >>> f([1,2,3,5,7,9],6)
    The max average in the window size of 6 is 9/2.
    Find on the indexes between 0 and 5 : 1--2--3--5--7--9
    '''
    max_sum = 0
    visited = []
    position = []
    for i in range(len(L) - window_size+ 1):
        new_line = L[i:window_size+i]
        result = sum(new_line)
        if result > max_sum:
            visited = [new_line]
            max_sum = result
            position = [i]
        elif result == max_sum:
            visited.append(new_line)
            position.append(i)
    print(f'The max average in the window size of {window_size} is {Fraction(max_sum/window_size)}.')
    results = []
    for j in range(len(visited)):
        new_line = []
        for a in visited[j]:
            new_line.append(str(a))
        results.append(new_line)
        if window_size == 1:
            print(f"Find on the index {position[j]} : {'--'.join(results[j])}")
        else:
            print(f"Find on the indexes between {position[j]} and {position[j]+window_size-1} : {'--'.join(results[j])}")

if __name__ == '__main__':
    import doctest
    doctest.testmod()