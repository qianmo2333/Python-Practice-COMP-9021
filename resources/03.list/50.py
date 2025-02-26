# 2019T1 PRE FINAL exercise_8.py

dictionary_file = 'dictionary.txt'


def number_of_words_in_dictionary(word_1, word_2):
    '''
    "dictionary.txt" is stored in the working directory.

    >>> number_of_words_in_dictionary('company', 'company')
    Could not find company in dictionary.
    >>> number_of_words_in_dictionary('company', 'comparison')
    Could not find at least one of company and comparison in dictionary.
    >>> number_of_words_in_dictionary('COMPANY', 'comparison')
    Could not find at least one of COMPANY and comparison in dictionary.
    >>> number_of_words_in_dictionary('company', 'COMPARISON')
    Could not find at least one of company and COMPARISON in dictionary.
    >>> number_of_words_in_dictionary('COMPANY', 'COMPANY')
    COMPANY is in dictionary.
    >>> number_of_words_in_dictionary('COMPARISON', 'COMPARISON')
    COMPARISON is in dictionary.
    >>> number_of_words_in_dictionary('COMPANY', 'COMPARISON')
    Found 14 words between COMPANY and COMPARISON in dictionary.
    >>> number_of_words_in_dictionary('COMPARISON', 'COMPANY')
    Found 14 words between COMPARISON and COMPANY in dictionary.
    >>> number_of_words_in_dictionary('CONSCIOUS', 'CONSCIOUSLY')
    Found 2 words between CONSCIOUS and CONSCIOUSLY in dictionary.
    >>> number_of_words_in_dictionary('CONSCIOUS', 'CONSCIENTIOUS')
    Found 3 words between CONSCIOUS and CONSCIENTIOUS in dictionary.
    '''
    position_1 = -1
    position_2 = -1
    count = 0
    with open('C:/Users/24246/Desktop/resources/03.list/dictionary.txt') as file:
        for line in file:
            word = line.strip()
            count += 1
            if word == word_1:
                position_1 = count
            if word == word_2:
                position_2 = count
    if position_1 == -1 or position_2 == -1:
        if word_1 == word_2:
            print(f'Could not find {word_1} in dictionary.')
        else:
            print(f'Could not find at least one of {word_1} and {word_2} in dictionary.')
    elif position_1 != -1 and position_2!= -1:
        if word_1 == word_2:
            print(f'{word_1} is in dictionary.')
        else:
            gap = abs(position_1-position_2)+1
            print(f'Found {gap} words between {word_1} and {word_2} in dictionary.')
if __name__ == '__main__':
    import doctest

    doctest.testmod()
