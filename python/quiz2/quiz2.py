from random import seed,shuffle
import sys
your_list = [int(x) for x in input('Enter a permutation of 0, ..., n for some n >= 0:').split()]
your_list_set = set(your_list)
try:
    if your_list_set != set(range(len(your_list))) or len(your_list) != len(your_list_set):
        raise ValueError
except ValueError:
    print('Wrong')
    sys.exit()

for_seed, length = (int(x) for x in input('Enter two integers, the second one between 0 and 10:').split())
if not 0<=length<=10:
    sys.exit()
seed(for_seed)
my_list = list(range(length))
shuffle(my_list)
print('Here is your list:')
print(your_list)
print('Here is my list:')
print(my_list)

for i in range(len(your_list)):
    if your_list[0] == max(your_list) or your_list[0] == min(your_list):
        your_list.remove(your_list[0])
    elif your_list[-1] == max(your_list) or your_list[-1] == min(your_list):
        your_list.remove(your_list[-1])
    else:
        break

print('Removing again and again the currently largest or smallest element in your list for as long as it currently starts or ends the list, we get:')
print(your_list)

print("That's how to travel in my list:")
position = my_list.index(0)
print(' '*2*position+'0')
for i in range(len(my_list)-1):
    distance = my_list.index(i+1) - my_list.index(i)
    if distance > 0:
        print(' '*my_list.index(i)*2+ '-'*2*distance + str(i+1))
    elif distance < 0:
        print(' '*2*my_list.index(i+1) + str(i+1) + '-'*2*abs(distance))