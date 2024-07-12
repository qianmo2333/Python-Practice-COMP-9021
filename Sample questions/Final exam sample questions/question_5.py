# Will be tested with year between 1913 and 2013.
import csv

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
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',\
             'Sep', 'Oct', 'Nov', 'Dec'
    max_inflation = -float('inf')
    months_with_max_inflation = []

    with open(r'C:\Users\24246\Desktop\COMP9021\Sample questions\Final exam sample questions\cpiai.csv') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            row_year = int(row[0].split('-')[0])
            if row_year == year:
                inflation = float(row[2])
                if inflation > max_inflation:
                    max_inflation = inflation
                    months_with_max_inflation = [row[0].split('-')[1]]
                elif inflation == max_inflation:
                    months_with_max_inflation.append(row[0].split('-')[1])

    months_with_max_inflation = [months[int(m) - 1] for m in months_with_max_inflation]
    print(f'In {year}, maximum inflation was: {max_inflation}')
    print(f'It was achieved in the following months: {", ".join(months_with_max_inflation)}')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
