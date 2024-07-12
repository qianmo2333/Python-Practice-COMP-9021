'''
Tries and find a word in a text file that represents a grid of words, all of the same length.
There is only one word per line in the file.
The letters that make up a word can possibly be separated by an arbitrary number of spaces,
and there can also be spaces at the beginning or at the end of a word,
and there can be lines consisting of nothing but spaces anywhere in the file.
Assume that the file stores data as expected.

A word can be read horizontally from left to right,
or vertically from top to bottom,
or diagonally from top left to bottom right
(this is more limited than the lab exercise).
The locations are represented as a pair (line number, column number),
starting the numbering with 1 (not 0).
'''
def find_word(filename, word):
    '''
    >>> find_word('C:/Users/24246/Desktop/sample/word_search_1.txt', 'PLATINUM')
    PLATINUM was found horizontally (left to right) at position (10, 4)
    >>> find_word('C:/Users/24246/Desktop/sample/word_search_1.txt', 'MANGANESE')
    MANGANESE was found horizontally (left to right) at position (11, 4)
    >>> find_word('C:/Users/24246/Desktop/sample/word_search_1.txt', 'LITHIUM')
    LITHIUM was found vertically (top to bottom) at position (2, 14)
    >>> find_word('C:/Users/24246/Desktop/sample/word_search_1.txt', 'SILVER')
    SILVER was found vertically (top to bottom) at position (2, 13)
    >>> find_word('C:/Users/24246/Desktop/sample/word_search_1.txt', 'SODIUM')
    SODIUM was not found
    >>> find_word('C:/Users/24246/Desktop/sample/word_search_1.txt', 'TITANIUM')
    TITANIUM was not found
    >>> find_word('C:/Users/24246/Desktop/sample/word_search_2.txt', 'PAPAYA')
    PAPAYA was found diagonally (top left to bottom right) at position (1, 9)
    >>> find_word('C:/Users/24246/Desktop/sample/word_search_2.txt', 'RASPBERRY')
    RASPBERRY was found vertically (top to bottom) at position (5, 14)
    >>> find_word('C:/Users/24246/Desktop/sample/word_search_2.txt', 'BLUEBERRY')
    BLUEBERRY was found horizontally (left to right) at position (13, 5)
    >>> find_word('C:/Users/24246/Desktop/sample/word_search_2.txt', 'LEMON')
    LEMON was not found
    '''
    whole_dic = []
    with open(filename) as file:
        for line in file:
            new_line = ''.join(line.strip().split())
            if new_line:
                visited = []
                for element in new_line:
                    visited.append(element)
                whole_dic.append(visited)

        location = find_word_horizontally(whole_dic, word)
        found = False
        if location:
            found = True
            print(word, 'was found horizontally (left to right) at position', location)
        location = find_word_vertically(whole_dic, word)
        if location:
            found = True
            print(word, 'was found vertically (top to bottom) at position', location)
        location = find_word_diagonally(whole_dic, word)
        if location:
            found = True
            print(word, 'was found diagonally (top left to bottom right) at position', location)
        if not found:
            print(word, 'was not found')
      
def find_word_horizontally(whole_dic, word):
    list_word = list(word)
    for i in range(len(whole_dic)):
        count = 0
        for j in range(len(whole_dic)):
            if whole_dic[i][j] == list_word[count]:
                count += 1
                if count == len(list_word):
                    return (i+1,j-len(list_word)+2)

def find_word_vertically(whole_dic, word):
    list_word = list(word)
    for i in range(len(whole_dic)):
        count = 0
        for j in range(len(whole_dic)):
            if whole_dic[j][i] == list_word[count]:
                count += 1
                if count == len(list_word):
                    return (j-len(list_word)+2,i+1)

def find_word_diagonally(whole_dic, word):
    num = 0
    list_word = list(word)
    for _ in range(len(whole_dic)):
        count = 0
        count_2 = 0
        for i in range(len(whole_dic)-num):
            if whole_dic[i+num][i] == list_word[count]:
                count += 1
                if count == len(list_word):
                    return (i-len(list_word)+1,i-len(list_word)+2)
            elif whole_dic[i][i+num] == list_word[count]:
                count_2 += 1
                if count_2 == len(list_word):
                    return (i-len(list_word)+1,i-len(list_word)+2)
        num += 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()   
