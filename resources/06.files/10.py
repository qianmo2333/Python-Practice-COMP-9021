'''
Will be tested with year between 1913 and 2013.
You might find the reader() function of the csv module useful,
but you can also use the split() method of the str class.
'''
import csv
from collections import defaultdict

def f(year):
    '''
    >>> f(1914)
    In 1914, maximum inflation was: 2.0
    It was achieved in the following months: Aug
    >>> f(1922)
    In 1922, maximum inflation was: 0.6
    It was achieved in the following months: Jul, Oct, Nov, Dec
    >>> f(1995)
    In 1995, maximum inflation was: 0.4
    It was achieved in the following months: Jan, Feb
    >>> f(2013)
    In 2013, maximum inflation was: 0.82
    It was achieved in the following months: Feb
    '''
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    file_cvs = 'C:/Users/24246/Desktop/resources/06.files/cpiai.csv'
    max_inflation = 0
    new_list = []
    month_row = []
    with open(file_cvs) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            year_row = int(row[0].split('-')[0])
            if year_row == year:
                infaltion = float(row[2])
                if infaltion > max_inflation:
                    max_inflation = infaltion
                    month_row = [int(row[0].split('-')[1])]
                elif infaltion == max_inflation:
                    month_row.append(int(row[0].split('-')[1]))
        for char in month_row:
            new_list.append(months[int(char)-1])
        new_str = ', '.join(new_list)
        print(f'In {year}, maximum inflation was: {max_inflation}')
        print(f'It was achieved in the following months: {new_str}')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
