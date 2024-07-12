from itertools import zip_longest
import math
height = 20
visited = []
count = 0
for j in range(math.ceil(height/2)):
    list = ' '*j 
    for i in range(height-2*j):
        if count+65 <= 90:
            list += chr(count+65)
        else:
            list += chr(((count+65-91)%26)+65)
        count += 1
    visited.append(list)
for element in zip_longest(*visited,fillvalue = ''):
    print(' '.join(element).strip())