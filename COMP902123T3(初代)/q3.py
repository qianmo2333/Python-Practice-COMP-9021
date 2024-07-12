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
    >>> f('0_ + 00 = 0_')
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
    flag = False
    left_num = expression.split('+')[0].strip()
    new_expression = expression.split('+')[1]
    right_num = new_expression.split('=')[0].strip()
    result_num = new_expression.split('=')[1].strip()
    if '_' not in left_num and  '_' not in right_num and  '_' not in result_num:
        return None
    else:
        for i in range(10):
            left_new = left_num.replace('_',str(i))
            right_new = right_num.replace('_',str(i))
            result_new = result_num.replace('_',str(i))
            if int(left_new)+int(right_new) == int(result_new):
                flag = True
                print(f'{int(left_new)} + {int(right_new)} = {int(result_new)}')
        if flag == False and '_' in left_num:
            print('No solution!')
if __name__ == '__main__':
    import doctest

    doctest.testmod()