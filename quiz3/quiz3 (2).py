def explore_this_way(directions):
    color_square = ['🟨', '🟧', '🟫', '🟩', '🟪']
    visited = {}
    current_position = [0,0]
    visited[0, 0] = 0
    for e in directions:
        if e == '⬆':
            current_position[0] -= 1
        elif e == '⮕':
            current_position[1] += 1
        elif e == '⬇':
            current_position[0] += 1
        elif e == '⬅':
            current_position[1] -= 1
        now_position = tuple(current_position)
        if now_position not in visited:
            visited[now_position] = 0
        else:
            visited[now_position] = (visited[now_position]+1)%len(color_square)
    max_x = max(x for (x,y) in visited)
    min_x = min(x for (x,y) in visited)
    max_y = max(y for (x,y) in visited)
    min_y = min(y for (x,y) in visited)

    for i in range(min_x, max_x + 1):
        for j in range(min_y,max_y + 1):
            if (i,j) == (0,0):
                if (i,j) ==tuple(current_position):
                    print('⚫', end='')
                else:
                    print('🔵', end='')
            elif (i,j) == tuple(current_position):
                print('🔴', end='')
            else:
                print(color_square[visited[i,j]] if (i,j) in visited else '⬜',end='')
        print()
directions = input("Please enter your input: ")
explore_this_way(directions)