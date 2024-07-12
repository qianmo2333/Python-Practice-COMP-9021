# Will be tested with letters a string of DISTINCT UPPERCASE letters only.
from itertools import permutations

def f(letters):
    '''
    >>> f('ABCDEFGH')
    There is no solution.
    >>> f('GRIHWSNYP')
    The pairs of words using all (distinct) letters in "GRIHWSNYP" are:
    ('SPRING', 'WHY')
    >>> f('ONESIX')
    The pairs of words using all (distinct) letters in "ONESIX" are:
    ('ION', 'SEX')
    ('ONE', 'SIX')
    >>> f('UTAROFSMN')
    The pairs of words using all (distinct) letters in "UTAROFSMN" are:
    ('AFT', 'MOURNS')
    ('ANT', 'FORUMS')
    ('ANTS', 'FORUM')
    ('ARM', 'FOUNTS')
    ('ARMS', 'FOUNT')
    ('AUNT', 'FORMS')
    ('AUNTS', 'FORM')
    ('AUNTS', 'FROM')
    ('FAN', 'TUMORS')
    ('FANS', 'TUMOR')
    ('FAR', 'MOUNTS')
    ('FARM', 'SNOUT')
    ('FARMS', 'UNTO')
    ('FAST', 'MOURN')
    ('FAT', 'MOURNS')
    ('FATS', 'MOURN')
    ('FAUN', 'STORM')
    ('FAUN', 'STROM')
    ('FAUST', 'MORN')
    ('FAUST', 'NORM')
    ('FOAM', 'TURNS')
    ('FOAMS', 'RUNT')
    ('FOAMS', 'TURN')
    ('FORMAT', 'SUN')
    ('FORUM', 'STAN')
    ('FORUMS', 'NAT')
    ('FORUMS', 'TAN')
    ('FOUNT', 'MARS')
    ('FOUNT', 'RAMS')
    ('FOUNTS', 'RAM')
    ('FUR', 'MATSON')
    ('MASON', 'TURF')
    ('MOANS', 'TURF')
    '''
    dictionary = "C:/Users/24246/Desktop/COMP9021/Sample questions/Final exam sample questions/dictionary.txt"
    solutions = []
    with open(dictionary) as f1:
        for line1 in f1:
            line1 = line1.replace('\n', '')
            status1 = True
            letters1 = letters
            for i in range(len(line1)):
                if line1[i] in letters1:
                    letters1 = letters1.replace(line1[i], '')
                else:
                    status1 = False
                    break
            if status1:
                first_word = line1
                with open(dictionary) as f2:
                    for line2 in f2:
                        line2 = line2.replace('\n', '')
                        status2 = True
                        letters2 =letters1
                        for i in range(len(line2)):
                            if line2[i] in letters2:
                                letters2 = letters2.replace(line2[i], '')
                            else:
                                status2 = False
                                break
                        if status2 and len(letters2) == 0:
                            second_word = line2
                            for items in solutions:
                                if first_word in items[1] and second_word in items[0]:
                                    status2 = False
                                    break
                        if status2 and len(letters2) == 0:
                            second_word = line2
                            solutions.append((first_word, second_word))
    if not solutions:
        print('There is no solution.')
    else:
        print(f'The pairs of words using all (distinct) letters '
              f'in "{letters}" are:'
             )
        for solution in solutions:
            print(solution)
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()