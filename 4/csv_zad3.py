import pandas

# pip install pandas

data = pandas.read_csv('records_3.csv', delimiter=";")
print(data)  # wypisanie danych z pliku
#      name branch  year  cgpa
# 0   Radek    Coe     2   9.1
# 1   Radek    Coe     2   9.1
# 2   Radek    Coe     2   9.1
# 3   Radek    Coe     2   9.1
# 4   Radek    Coe     2   9.1
# 5   Radek    Coe     2   9.1
# 6   Radek    Coe     2   9.1
# 7   Radek    Coe     2   9.1
# 8   Radek    Coe     2   9.1
# 9   Radek    Coe     2   9.1
# 10  Radek    Coe     2   9.1
# 11  Radek    Coe     2   9.1
# 12  Radek    Coe     2   9.1
print(
    data.columns)  # Index(['name', 'branch', 'year', 'cgpa'], dtype='object'), wypisanie nazw kolumn jakie mamy w pliku
print(data.values)  # wypisanie wartosci czyli danych z kolumn
# [['Radek' 'Coe' 2 9.1]
#  ['Radek' 'Coe' 2 9.1]
#  ['Radek' 'Coe' 2 9.1]
#  ['Radek' 'Coe' 2 9.1]
#  ['Radek' 'Coe' 2 9.1]
#  ['Radek' 'Coe' 2 9.1]
#  ['Radek' 'Coe' 2 9.1]
#  ['Radek' 'Coe' 2 9.1]
#  ['Radek' 'Coe' 2 9.1]
#  ['Radek' 'Coe' 2 9.1]
#  ['Radek' 'Coe' 2 9.1]
#  ['Radek' 'Coe' 2 9.1]
#  ['Radek' 'Coe' 2 9.1]]
print(data.items)  # wypisanie par
# <bound method DataFrame.items of      name branch  year  cgpa
# 0   Radek    Coe     2   9.1
# 1   Radek    Coe     2   9.1
# 2   Radek    Coe     2   9.1
# 3   Radek    Coe     2   9.1
# 4   Radek    Coe     2   9.1
# 5   Radek    Coe     2   9.1
# 6   Radek    Coe     2   9.1
# 7   Radek    Coe     2   9.1
# 8   Radek    Coe     2   9.1
# 9   Radek    Coe     2   9.1
# 10  Radek    Coe     2   9.1
# 11  Radek    Coe     2   9.1
# 12  Radek    Coe     2   9.1>
