import sys
from os.path import exists
num_dict = {2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight'}
character_dict={'dashes':'-','stars':'*','carets':'^','dollars':'$'}

interger = input("Enter an integer at least equal to 3: ")
try:
    if int(interger) < 3:
        raise ValueError
except ValueError:
    print("Incorrect input")
    sys.exit()
file =input("Input the name of a file in the working directory:")
with open (file) as f:
    for line in f:
        if 'Give' in line:
            line = line.rstrip("\n")
            line_real = line.split()
            num = int(line_real[2])
            print(f'Here are your {num_dict[num]} {line_real[3]}:')
            translate = (character_dict[line_real[3]] + " ") * num
            print("    " + translate)