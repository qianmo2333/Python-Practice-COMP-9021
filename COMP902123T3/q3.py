# f('1 + 2 = 3')
# f('1_3 + 2_4 = 387')
# f('__ + ___ = ____')
# f('1_3 + 2_4 = 388')
# f('0_ + 00 = 0_ ')
def f(expression):
    '''
    >>> f('1 + 2 = 3')
    >>> f('1_3 + 2_4 = 387')
    143 + 244 = 387
    >>> f('__ + ___ = ____')
    0 + 0 = 0
    >>> f('1_3 + 2_4 = 388')
    No solution!
    >>> f('0_ + 00 = 0_ ')
    0 + 0 = 0
    1 + 0 = 1
    2 + 0 = 2
    3 + 0 = 3
    4 + 0 = 4
    5 + 0 = 5
    6 + 0 = 6
    7 + 0 = 7
    8 + 0 = 8
    9 + 0 = 9
    '''
    test = expression.split('+')
    left_item = test[0].strip()
    test2 = test[1].split('=')
    right_item = test2[0].strip()
    result_item = test2[1].strip()
    flag = False
    if not '_' in expression:
        return None
    else:
        for i in range(10):
            left_num = left_item.replace('_',str(i))
            right_num = right_item.replace('_',str(i))
            result_num = result_item.replace('_',str(i))
            if int(left_num)+int(right_num) == int(result_num):
                flag = True
                print(f'{int(left_num)} + {int(right_num)} = {int(result_num)}')
        if flag == False:
            print('No solution!')

if __name__ == '__main__':
    import doctest

    doctest.testmod()