import sys
from random import seed,shuffle
your_list = [int(x) for x in input('Enter a permutation of 0, ..., n for some n >= 0:').split()]
your_list_as_set = set(your_list)
if len(your_list_as_set) != len(your_list) or your_list_as_set != set(range(len(your_list))):
    print('Incorrect input,giving up')
    sys.exit()
for_seed, length = (int(x) for x in input('Enter two integers, the second one between 0 and 10:').split())
if length<0 or length >10:
    print('Incorrect input,giving up')
    sys.exit()
seed(for_seed)
my_list = list(range(length))
shuffle(my_list)
print(your_list)
print(my_list)
while len(your_list) >0:
    if your_list[0] == max(your_list) or your_list[0] == min(your_list):
        your_list.pop(0)
    elif your_list[-1] == max(your_list) or your_list[-1] == min(your_list):
        your_list.pop(-1)
    else:
        break
print('Removing again and again the currently largest\n'
    'or smallest element in your list for as long as\n'
    'it currently starts or ends the list, we get:')
print(your_list)
if len(my_list) == 0:
    print("That's how to travel in my list:")
else:
    print("That's how to travel in my list:")
    print(' ' * my_list.index(0) * 2 + str(0))
    i = 0
    for i in range(len(my_list)):
        if i+1 not in my_list:
            break
        distance = my_list.index(i+1) - my_list.index(i)
        if distance < 0:
            print(' '* my_list.index(i+1)*2 + str(i+1)+ '-'*abs(distance)*2)
        elif distance >0:
            print(' ' * my_list.index(i)*2 + '-' * distance*2 + str(i+1))
