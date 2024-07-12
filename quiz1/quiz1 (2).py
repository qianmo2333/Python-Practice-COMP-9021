import sys
from os.path import exists
num_dict = {1:'one',2:'two',3:'three',4:'four',5:'five'}
character_dict = {'dashes':'-','stars':'*','dollars':'$','carets':'^'}
num = input('Enter an integer at least equal to 3:')
try:
    if int(num) < 3:
        raise ValueError
except ValueError:
    print('Incorrect input')
    sys.exit()

file = input('Input the name of a file in the working directory:')
if not exists(file):
    print('Incorrect input')
    sys.exit()
with open(file) as f:
    for line in f:
        if 'Give' in line:
            line = line.rstrip('\n')
            line_correct = line.split()
            number = int(line_correct[2])
            print(f'Here are your {num_dict[number]} {line_correct[3]}:')
            translate = character_dict[line_correct[3]]
            print((translate+' ') * number)