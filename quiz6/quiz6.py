from collections import defaultdict
from random import seed, randrange
import sys

def display_grid():
    print('  ', '-' * (2 * dim + 3))
    for row in grid:
        print('   |', *row, '|')
    print('  ', '-' * (2 * dim + 3))

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

seed(for_seed)
grid = [['*' if randrange(density) != 0 else ' ' for _ in range(dim)]
            for _ in range(dim)
       ]
print('Here is the grid that has been generated:')
display_grid()

results = defaultdict(list)

def is_rhombus(j, i, size):
    if j + 2 * size >= dim or i - size < 0 or i + size >= dim:
        return False
    for delta in range(size + 1):
        if grid[j + delta][i - delta] != '*' or grid[j + delta][i + delta] != '*':
            return False
    for delta in range(size):
        if grid[j + 2 * size - delta][i - delta] != '*' or grid[j + 2 * size - delta][i + delta] != '*':
            return False
    return True

def get_vertices(j, i, size):
    top_vertex = (j, i)
    bottom_vertex = (j + 2 * size, i)
    left_vertex = (j + size, i - size)
    right_vertex = (j + size, i + size)
    return top_vertex, bottom_vertex, left_vertex, right_vertex
def is_inside(large_vertices, small_vertices):
    lt, lb, ll, lr = large_vertices
    st, sb, sl, sr = small_vertices
    vertical_condition = lt[0] <= st[0] <= lb[0] and lt[0] <= sb[0] <= lb[0]
    horizontal_condition = ll[1] <= sl[1] <= lr[1] and ll[1] <= sr[1] <= lr[1]
    diagonal_left_condition = lt[1] - st[1] <= st[0] - lt[0] and lb[1] - sb[1] <= lb[0] - sb[0]
    diagonal_right_condition = st[1] - lt[1] <= st[0] - lt[0] and sb[1] - lb[1] <= lb[0] - sb[0]

    
    return vertical_condition and horizontal_condition and diagonal_left_condition and diagonal_right_condition

# 先找出所有的菱形
all_rhombuses = defaultdict(list)
for size in range(1, (dim + 1) // 2 + 1):
    for i in range(dim):
        for j in range(dim):
            if is_rhombus(j, i, size):
                all_rhombuses[size].append(get_vertices(j, i, size))
# 删除被包含在更大菱形中的菱形
to_remove = set()
for large_size in sorted(all_rhombuses, reverse=True):
    for small_size in range(1, large_size):  # 只检查更小的菱形
        for large_rhombus in all_rhombuses[large_size]:
            for small_rhombus in all_rhombuses[small_size]:
                if is_inside(large_rhombus, small_rhombus):
                    to_remove.add((small_size, small_rhombus[0]))


# 从all_rhombuses中移除被包含的菱形
for size, vertex in to_remove:
    all_rhombuses[size] = [rhombus for rhombus in all_rhombuses[size] if rhombus[0] != vertex]

# 更新结果到results字典
results = defaultdict(list)
for size, rhombuses in all_rhombuses.items():
    for rhombus in rhombuses:
        results[size].append(rhombus[0])
                      
print('Here are the rhombuses that are not included in any other:')
for size in sorted(results):
    print(f'Of size {size}:')
    # 对菱形的顶部顶点进行排序
    for (i, j) in sorted(results[size]):
        print(f'  - with top vertex at location ({i}, {j})')
