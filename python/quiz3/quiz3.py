# Written by Eric Martin for COMP9021
#
# Implements a function that takes as argument a string
# consisting of arrows pointing North, East, South or West.
#
# Following the provided directions,
# - if the exploration gets back to the starting point, then this
#   common location will be represented by a black circle;
# - otherwise, the starting point will be represented by a blue circle
#   and the final destination by a red circle.

# All other visited locations will be represented by a square, of colour:
# - yellow if visited exactly once, 6 times, 11 times, 16 times...
# - orange if visited exactly twice, 7 times, 12 times, 17 times...
# - brown if visited exactly trice, 8 times, 13 times, 18 times...
# - green if visited exactly 4 times, 9 times, 14 times, 19 times...
# - purple if visited exactly 5 times, 10 times, 15 times, 20 times...

# The explored area is displayed within the smallest rectangle in
# which it fits; all unvisited locations within that rectangle are
# represented by white squares.
#
# The code points of the characters involved in this quiz are:
# 9899(black circle), 11036(white square), 128308(red circle), 128309(blue circle),
# 128999(orange square), 129000(yellow square), 129001(green square), 129002(purple square), 129003(brown square)
# 11014(up) 11157(right) 11015(down) 11013(left)
print(chr(11014),chr(11157),chr(11015),chr(11013))
def explore_this_way(directions):
    color_square = [chr(129000), chr(128999),chr(129003),chr(129001),chr(129002)]
    visited = {}
    current_position = [0, 0]
    visited[0, 0] = 0
    for e in directions:
        if e == chr(11014):
            current_position[0] -= 1
        elif e == chr(11015):
            current_position[0] += 1
        elif e == chr(11157):
            current_position[1] += 1
        elif e == chr(11013):
            current_position[1] -= 1
    current_position_tuple = tuple(current_position)
    if current_position_tuple not in visited:
        visited[current_position_tuple] = 0
    else:
        visited[current_position_tuple] = (visited[current_position_tuple] + 1) % len(color_square)
    
    min_x = min(x for (x,y) in visited)
    max_x = max(x for (x,y) in visited)
    min_y = min(y for (x,y) in visited)
    max_y = max(y for (x,y) in visited)

    for i in range(min_x,max_x+1):
        for j in range(min_y,max_y+1):
            if (i,j) == (0,0) and (i,j) == tuple(current_position):
                print(chr(9899),end='')
            elif (i,j) == (0,0) and (i,j) != tuple(current_position):
                print(chr(128309), end = '')
            elif (i,j) != (0,0) and (i,j) == tuple(current_position):
                print(chr(128308),end='')
            elif (i,j) in visited and (i,j) != (0,0) and (i,j) != tuple(current_position):
                print(color_square[visited[i,j]],end='')
            elif (i,j) not in visited:
                print(chr(11036),end='')
        print()
directions = input("Please enter your input: ")
explore_this_way(directions)