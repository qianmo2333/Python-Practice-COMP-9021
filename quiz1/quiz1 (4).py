import sys
from os.path import exists
num = input('Enter an integer at least equal to 3: ')
if int(num) < 3:
    print('Incorrect input, giving up')
    sys.exit()
file_name = input('Input the name of a file in the working directory: ')
if not exists (file_name):
    print('Incorrect input, giving up')
    sys.exit()
num_dict = {2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight'}
character_dict = {'dashes':'-','stars':'*','carets':'^','dollars':'$'}
with open(file_name) as f :
    for line in f:
        if 'Give' in line:
            line = line.rstrip('\n')
            line_correct = line.split()
            number = num_dict[int(line_correct[2])]
            print(f'Here are your {number} {line_correct[3]}:')
            print(int(line_correct[2])*(character_dict[line_correct[3]]+' '))