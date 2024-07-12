from random import seed,shuffle
import sys
your_list = [int(x) for x in
             input('Enter a permutation of 0, ..., n for some n >= 0:').split()]
try:
    your_list_set = set(your_list)
    if len(your_list) != len(your_list_set) or your_list_set != set(range(len(your_list))):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up')
    sys.exit()
try:
    for_seed, length = (int(x) for x in
                    input('Enter two integers, the second one between 0 and 10:').split())
    if not 0<=length<=10:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up')
    sys.exit()
seed(for_seed)
my_list = list(range(length))
shuffle(my_list)
print('Here is your list:')
print(your_list)
print('Here is my list:')
print(my_list)

while len(your_list) > 0:
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

if 0 not in my_list:
    print("That's how to travel in my list:")
else:
    print("That's how to travel in my list:")
    print(' ' * my_list.index(0) * 2 + str(0))
    i = 0
    while i <= len(my_list):
        if i+1 not in my_list or i not in my_list:
            break
        else:
            distance = my_list.index(i+1) - my_list.index(i)
            if distance > 0:
                print(' ' * my_list.index(i) * 2 +'-' * distance * 2 + str(i+1))
            elif distance < 0:
                print(' ' * my_list.index(i+1)*2 + str(i+1) + '-' * abs(distance) * 2)
        i += 1