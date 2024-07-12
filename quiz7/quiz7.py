from random import seed, randrange
import sys

dim = 10

def display_grid():
    global grid, dim
    print('   ', '-' * (2 * dim + 1))
    for i in range(dim):
        print('   |', ' '.join('*' if grid[i][j] else ' '
                                  for j in range(dim)
                              ), end = ' |\n'
             )
    print('   ', '-' * (2 * dim + 1))

def display_path(path):
    for i in range(dim):
        row_str = ''
        for j in range(dim):
            char = ' '  # Default character for empty space
            if [i, j] == end and grid[i][j] == False:
                print("There is no path joining both points.")
                sys.exit()
            if [i, j] in path:
                index = path.index([i, j])
                if index == len(path) - 1:
                    char = chr(128308)  # Red dot for end
                else:
                    # Determine direction and set color
                    next_point = path[index + 1]
                    if next_point[0] < i:  # Moving North
                        char = chr(129000)  # Yellow square
                    elif next_point[0] > i:  # Moving South
                        char = chr(129001)  # Green square
                    elif next_point[1] > j:  # Moving East
                        char = chr(129003)  # Brown square
                    elif next_point[1] < j:  # Moving West
                        char = chr(129002)  # Purple square
            elif grid[i][j]:
                char = chr(11035)  # Black square for star
            else:
                char = chr(11036)  # White square for empty space
            row_str += char
        print('   ',row_str)

def dfs(start, end, visited=None):
    if visited is None:
        visited = [[False] * dim for _ in range(dim)]
    visited[start[0]][start[1]] = True

    if start == end:
        return [start]

    directions = {'?': (-1, 0), '?': (1, 0), '?': (0, -1), '?': (0, 1)}
    for direction in direction_preferences:
        dx, dy = directions[direction]
        next_cell = [start[0] + dx, start[1] + dy]

        if 0 <= next_cell[0] < dim and 0 <= next_cell[1] < dim and \
           not visited[next_cell[0]][next_cell[1]] and grid[next_cell[0]][next_cell[1]]:
            path = dfs(next_cell, end, visited)
            if path is not None:
                return [start] + path
    return None


try: 
    for_seed, density, dim = (int(x)
                                  for x in input('Enter three integers, '
                                                 'the second and third ones '
                                                 'being strictly positive: '
                                                ).split()
                             )
    if density <= 0 or dim <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try: 
    start = [int(x) for x in input('Enter coordinates '
                                   'of start point:'
                                  ).split()
            ]
    if len(start) != 2 or not (0 <= start[0] < dim)\
                       or not (0 <= start[1] < dim):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:  
    end = [int(x) for x in input('Enter coordinates '
                                 'of end point:'
                                ).split()
          ]
    if len(end) != 2 or not (0 <= end[0] < dim)\
                       or not (0 <= end[1] < dim):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
direction_preferences = input('Input the 4 directions, from most '
                              'preferred to least preferred:'
                             )
if set(direction_preferences) != {'?', '?', '?', '?'}:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
             for _ in range(dim)
       ]
print('Here is the grid that has been generated:')
display_grid()
print()

path = dfs(start, end)
if path is None:
    print("There is no path joining both points.")
else:
    print(f"There is a path joining both points, of length {len(path)}:")
    display_path(path)