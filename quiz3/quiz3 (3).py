def my_way(directions):
    color_squares = ['🟨', '🟧', '🟫', '🟩', '🟪']
    visited = {}
    current_position = [0,0]
    visited[0,0] = 0
    for i in directions:
        if i == '⬆':
            current_position[0] -= 1
        elif i == '⮕':
            current_position[1] += 1
        elif i == '⬇':
            current_position[0] += 1
        elif i == '⬅':
            current_position[1] -= 1
        now_position = tuple(current_position)
        if now_position not in visited:
            visited[now_position] = 0
        else:
            visited[now_position] = (visited[now_position]+1) % len(color_squares)
    x_min = min(x for (x,y) in visited)
    x_max = max(x for (x,y) in visited)
    y_min = min(y for (x,y) in visited)
    y_max = max(y for (x,y) in visited)

    for i in range(x_min,x_max+1):
        for j in range(y_min,y_max+1):
            if (i,j) == (0,0):
                if (i,j) == tuple(current_position):
                    print('⚫',end='')
                else:
                    print('🔵',end='')
            elif (i,j) == tuple(current_position):
                print('🔴',end='')
            else:
                if (i,j) not in visited:
                    print('⬜',end='')
                elif(i,j) in visited:
                    print(color_squares[visited[i,j]],end='')
        print()
directions = input('exolore_this_way')
my_way(directions)