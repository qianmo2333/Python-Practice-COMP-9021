from collections import defaultdict
from pathlib import Path
import csv
import sys
# INSERT YOUR CODE HERE

letter_string_list = []
year_string_list = []
error_message = "Incorrect input, leaving it there."
try:
    letter_string = input("Enter two capitalised strings of letters: ")
    letter_string_list = letter_string.split()
    if len(letter_string_list) != 2:
        raise ValueError
    if letter_string_list[0][0].islower() or letter_string_list[1][0].islower():
        raise ValueError
    if letter_string_list[0][1:].lower() != letter_string_list[0][1:] or letter_string_list[1][1:].lower() != letter_string_list[1][1:]:
        raise ValueError
    year_string = input("Enter two integers between 1947 and 2021: ")
    year_string_list = year_string.split()
    if len(year_string_list) != 2:
        raise ValueError
    if int(year_string_list[0]) < 1947 or int(year_string_list[1]) < 1947 or int(year_string_list[0]) > 2021 or int(year_string_list[1]) > 2021:
        raise ValueError
except ValueError:
    print(error_message)
    sys.exit()

letter_0 = ''
letter_1 = ''
year_0 = 0
year_1 = 0
if letter_string_list[0] <= letter_string_list[1]:
    letter_0 = letter_string_list[0]
    letter_1 = letter_string_list[1]
else:
    letter_1 = letter_string_list[0]
    letter_0 = letter_string_list[1]
if int(year_string_list[0]) <= int(year_string_list[1]):
    year_0 = int(year_string_list[0])
    year_1 = int(year_string_list[1])
else:
    year_0 = int(year_string_list[1])
    year_1 = int(year_string_list[0])

d_all = defaultdict(list)

for i in range(year_0, year_1 +1):
    DIR_PATH = Path("./names") / f"yob{i}.txt"
    d_year = defaultdict(list)
    with DIR_PATH.open("r") as f:
        data = csv.reader(f)
        F_sum = 0
        M_sum = 0
        for row in data:
            if len(row) == 3 and row[2] !='':
                if letter_0 <= row[0] <=letter_1 or letter_1 in row[0]:
                    d_year[row[0]].append(int(row[2]))
                if row[1] == 'F':
                    F_sum += int(row[2])
                if row[1] == 'M':
                    M_sum += int(row[2])

        for key in d_year.keys():
            if len(d_year[key]) == 2:
                prop_F = d_year[key][0] / F_sum
                prop_M = d_year[key][1] / M_sum
                d_all[key].append((i, prop_F, prop_M, abs(prop_F-prop_M)))
if not d_all:
    print("No name was given as both female and male names.")
else:
    print('Here are the names that were given as both\n'
        'female and male names, for the smallest difference\n'
        'of ratio as a female name over all female names\n'
        'and ratio as a male name over all male names,\n'
        'for the years when that happened:')
    name = ''
    info = ()
    min_prop = 1
    for key in d_all.keys():
        for i in range(len(d_all[key])):
            if d_all[key][i][3] < min_prop:
                name = key
                info = d_all[key][i]
                min_prop = d_all[key][i][3]
    print(f'  {name} in {info[0]}, for ratios of')
    print(f'    - {round(info[1]*100, 5)}% as a female name,')
    print(f'    - {round(info[2]*100, 5)}% as a male name.')