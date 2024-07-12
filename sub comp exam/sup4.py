#将输入的格式为 4i7o的字符串识别转换成二级制数字再转成十进制,i代表1，o代表0

def weird_num(x):
    '''
    >>> weird_num('4i7o')
    This is a weird form of 11110000000 , the base 10 is 1920.
    >>> weird_num('3i2o7o2i')
    This is a weird form of 11100000000011 , the base 10 is 14339.
    >>> weird_num('3i2o27i4o')
    This is a weird form of 111001111111111111111111111111110000 , the base 10 is 62277025776.
    '''
    result = ''
    number = ''
    for element in x:
        if element not in 'io':
            number += element
        else:
            if element == 'i':
                result += int(number)*'1'
            elif element == 'o':
                result += int(number)*'0'
            number = ''
    int_result = int(result,2)
    print(f'This is a weird form of {result} , the base 10 is {int_result}.')


if __name__ == '__main__':
    import doctest

    doctest.testmod()