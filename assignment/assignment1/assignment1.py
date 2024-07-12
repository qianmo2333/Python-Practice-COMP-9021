import sys
def sir_list(sentence_split_list):
    sir = set()
    name_to_number = {}
    number = -1    
    for i in range(len(sentence_split_list)):
        if 'Sir ' in sentence_split_list[i]:
            sir_temp = sentence_split_list[i].split('Sir ')[1]
            name = sir_temp.split('.')[0].split(',')[0].split('!')[0].split('?')[0].split()[0]
            sir.add(name)
            if name not in name_to_number:
                number += 1
                name_to_number[name] = number
        if 'Sirs ' in sentence_split_list[i]:
            sir_temp = sentence_split_list[i].split('Sirs ')[1]
            sir_temp = sir_temp.split(', ')
            for j in range(len(sir_temp) - 1):
                name = sir_temp[j]
                sir.add(name)
                if name not in name_to_number:
                    number += 1
                    name_to_number[name] = number
            sir_temp_final = sir_temp[-1].split(' and ')
            for name in sir_temp_final:
                name = name.split('.')[0].split(',')[0].split('!')[0].split('?')[0].split()[0]
                sir.add(name)
                if name not in name_to_number:
                    number += 1
                    name_to_number[name] = number
    return  name_to_number, sir

def generate_saying(sentence):
    sentence = sentence.replace('At', 'at').replace('Exactly', 'exactly').replace('All', 'all')
    sentence = sentence.replace('"', '"6')
    sentence_list = sentence.replace('\n', ' ').split('.')
    saying_dict = {}
    person = ''
    saying = ''
    for i in range(len(sentence_list)):
        if '"6' in sentence_list[i] and 'Sir ' in sentence_list[i]:
            sentence_sir_list = sentence_list[i].split('"')
            for j in range(len(sentence_sir_list)):
                if '6 ' not in sentence_sir_list[j] and '6' in sentence_sir_list[j]:
                    saying = sentence_sir_list[j].split('6')[1]
                    if 'Sir ' and ': ' in sentence_sir_list[j - 1]:
                        saying_parts = sentence_sir_list[j - 1].split('Sir ')
                        if len(saying_parts) > 1:
                            person = saying_parts[1].split(' ')[0]
                        else:
                            sys.exit
                        if person not in saying_dict:
                            saying_dict[person] = []
                    elif len(sentence_sir_list) > j + 1 and 'Sir ' and '6 ' in sentence_sir_list[j + 1]:
                        saying_parts = sentence_sir_list[j + 1].split('Sir ')
                        person = saying_parts[1].split(' ')[0]
                        if person not in saying_dict:
                            saying_dict[person] = []
                    saying_dict[person].append(saying)
    all_sir_saying = {}
    for person, sayings in saying_dict.items():
        key = sir_set.get(person)
        if key is not None:
            all_sir_saying[key] = [saying.split() for saying in sayings]
    return all_sir_saying, saying

def test(sir_dict, sir_set):
    saying_d = {}
    for key, sayings in sir_dict.items():
        modified_sayings = []
        for saying in sayings:
            modified_saying = []
            for word in saying:
                if word in sir_set:
                    modified_saying.append(int(sir_set[word]))
                elif word == 'I':
                    modified_saying.append(int(key))
                else:
                    modified_saying.append(word)
            modified_sayings.append(modified_saying)
        saying_d[key] = modified_sayings
    return saying_d

def all_conditions(n):
    all_conditions_list = []
    for i in range(2 ** n):
        all_conditions_list.append([])
        for j in range(n, 0, -1):
            if i % (2 ** j) < 2 ** (j-1):
                all_conditions_list[i].append(False)
            else:
                all_conditions_list[i].append(True)
    return all_conditions_list

def condition_judge(all_sir, saying_d, condition):
    mentioned_name = []
    for word in saying_d:
        if type(word) == int:
            mentioned_name.append(word)
        if word == 'us':
            mentioned_name = [i for i in range(len(all_sir))]
    temp = []
    #case 1: at least
    if 'least' in saying_d:
        if 'Knight' in saying_d:
            for i in range(len(condition)):
                for name in mentioned_name:
                    if i == name and condition[i] == True:
                        temp.append(True)
        elif 'Knave' in saying_d:
            for i in range(len(condition)):
                for name in mentioned_name:
                    if i == name and condition[i] == False:
                        temp.append(True)
    #case 2: at most
    if 'most' in saying_d:
        if 'Knight' in saying_d:
            for i in range(len(condition)):
                for name in mentioned_name:
                    if i == name and condition[i] == True:
                        temp.append(name)
            if len(temp) <= 1:
                return True
        elif 'Knave' in saying_d:
            for i in range(len(condition)):
                for name in mentioned_name:
                    if i == name and condition[i] == False:
                        temp.append(name)
            if len(temp) <= 1:
                return True
    #case 3: exactly
    if 'exactly' in saying_d:
        if 'Knight' in saying_d:
            for i in range(len(condition)):
                for name in mentioned_name:
                    if i == name and condition[i] == True:
                        temp.append(name)
            if len(temp) == 1:
                return True
        elif 'Knave' in saying_d:
            for i in range(len(condition)):
                for name in mentioned_name:
                    if i == name and condition[i] == False:
                        temp.append(name)
            if len(temp) == 1:
                return True
    #case 4: all
    if 'all' in saying_d:
        if 'Knights' in saying_d:
            temp = []
            for i in range(len(condition)):
                for name in mentioned_name:
                    if i == name and condition[i] == True:
                        temp.append(name)
            if len(temp) == len(all_sir):
                return True
        elif 'Knaves' in saying_d:
            temp = []
            for i in range(len(condition)):
                for name in mentioned_name:
                    if i == name and condition[i] ==False:
                        temp.append(name)
            if len(temp) == len(all_sir):
                return True
    #case 5: I am
    if 'am' in saying_d:
        if 'Knight' in saying_d:
            for i in range(len(condition)):
                for name in mentioned_name:
                    if i == name and condition[i] == True:
                        return True
        elif 'Knight,' in saying_d:
            for i in range(len(condition)):
                for name in mentioned_name:
                    if i == name and condition[i] == True:
                        return True
        elif 'Knave' in saying_d:
            for i in range(len(condition)):
                for name in mentioned_name:
                    print(f'name:{name}')
                    if i == name and condition[i] == False:
                        return True
        elif 'Knave,' in saying_d:
            knave_count = 0  
            for i in range(len(condition)):
                for name in mentioned_name:
                    if i == name and condition[i] == False:
                        knave_count += 1
            if knave_count > 0:
                return True
    #case 6 sir xxx is xxx
    if saying_d[0] == 'Sir' and saying_d[2] == 'is':
        if 'Knight' in saying_d:
            for i in range(len(condition)):
                for name in mentioned_name:
                    if i == name and condition[i] == True:
                        return True
        if 'Knave' in saying:
            for i in range(len(condition)):
                for name in mentioned_name:
                    if i ==name and condition[i] == False:
                        return True
    #case 7: sir xxx or sir xxx is
    if 'or' in saying_d:
        if 'Knight' in saying_d:
            for i in range(len(condition)):
                for name in mentioned_name:
                    if i == name and condition[i] == True:
                        temp.append(name)
            if len(temp) >= 1:
                return True
        elif 'Knave' in saying_d:
            for i in range(len(condition)):
                for name in mentioned_name:
                    if i == name and condition[i] == False:
                        temp.append(name)
            if len(temp) >= 1:
                return True
    #case 8:all are
    if 'all' not in saying and 'are' in saying_d:
        if 'Knight' in saying_d:
            for i in range(len(condition)):
                for name in mentioned_name:
                    if i == name and condition[i] == True:
                        temp.append(name)
        elif 'Knaves' in saying_d:
            for i in range(len(condition)):
                for name in mentioned_name:
                    if i ==name and condition[i] == False:
                        temp.append(name)
    if len(temp) == len(mentioned_name):
        return True
    return False
sentence = ''
file_name = input('Which text file do you want to use for the puzzle? ')
with open(file_name) as f:
    for line in f:
        sentence += line.replace('!', ' ').replace('?', ' ')
sentence_split_list = sentence.split('\n')
sir_set, sir_name = sir_list(sentence_split_list)
all_sir = ' '.join(sorted(sir_name))
if len(sir_name) > 1:
    print(f'The Sirs are: {all_sir}')
elif len(sir_name) == 1:
    print(f'The Sir is: {all_sir}')
else:
    sys.exit()
sir_dict, saying = generate_saying(sentence)
saying_d = test(sir_dict, sir_set)
sir_all_conditions_list = all_conditions(len(sir_set))
final = []
all_saying_count = 0
for key in saying_d.keys():
    all_saying_count += len(saying_d[key])
for condition in sir_all_conditions_list:
    combined_conditions = []
    for key in saying_d.keys():
        for value in saying_d[key]:
            for i in range(len(condition)):
                if i == key:
                    if condition_judge(sir_set, value, condition) and condition[i]:
                        combined_conditions.append(condition)
                    if not condition_judge(sir_set,value,condition) and not condition[i]:
                        combined_conditions.append(condition)
    if len(combined_conditions) == all_saying_count:
        final.append(condition)
if len(final) > 1:
    print(f'There are {len(final)} solutions.')
elif len(final) == 0:
    print('There is no solution.')
else:
    print('There is a unique solution:')
    sir_names_sorted = sorted(sir_name)
    for solution in final:
        for sir_name, status in zip(sir_names_sorted, solution):
            role = "Knight" if status else "Knave"
            print(f'Sir {sir_name} is a {role}.')
