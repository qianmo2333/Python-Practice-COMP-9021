def width(width):
    width_int = int(width)
    visited = {}
    a = 0
    x = 0
    y = 0
    i = 0
    for y in range(width_int):
        for x in range(y+1):
            visited[width_int - 1 - x, y] = i % 10
            i = i + 1

    for m in range(width_int):
        for n in range(width_int):
            if (m,n) not in visited:
                print('  ',end='')
            else:
                print(f'{visited[m,n]} ',end='')
        print('')
abandon = input('width:')
width(abandon)