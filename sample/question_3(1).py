
def rhombus(size, shift_right=False):
    '''
    >>> rhombus(1)
    A
    >>> rhombus(1, True)
    A
    >>> rhombus(2)
     BA
    CD
    >>> rhombus(2, True)
    AB
     DC
    >>> rhombus(3)
      CBA
     DEF
    IHG
    >>> rhombus(3, True)
    ABC
     FED
      GHI
    >>> rhombus(4)
       DCBA
      EFGH
     LKJI
    MNOP
    >>> rhombus(4, True)
    ABCD
     HGFE
      IJKL
       PONM
    >>> rhombus(7)
          GFEDCBA
         HIJKLMN
        UTSRQPO
       VWXYZAB
      IHGFEDC
     JKLMNOP
    WVUTSRQ
    >>> rhombus(7, True)
    ABCDEFG
     NMLKJIH
      OPQRSTU
       BAZYXWV
        CDEFGHI
         PONMLKJ
          QRSTUVW
    '''
    num = 0
    results = []
    for j in range(size):
      line = ''
      for i in range(size):
        if num+65 <= 90:
          line += chr(65+num)
        else:
           line += (chr((65+num-91)%26+65))
        num += 1
      results.append(line)
    new_results = []
    if shift_right == False:
      for e in range(len(results)):
        if e % 2 == 0:
          new_line = results[e]
          new_results.append(new_line[::-1])
        else:
          new_line = results[e]
          new_results.append(new_line)
    elif shift_right == True:
      for e in range(len(results)):
        if e % 2 == 1:
          new_line = results[e]
          new_results.append(new_line[::-1])
        else:
          new_line = results[e]
          new_results.append(new_line)
    for a in range(size):
      if shift_right == False:
        print(' '*(size-a-1)+new_results[a])
      else:
        print(' '*a+new_results[a])
            


if __name__ == '__main__':
    import doctest
    doctest.testmod()
