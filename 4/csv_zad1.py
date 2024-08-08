# pliki csv - dane w pliku oddzielone znakiem podziału
# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce

import csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ['Radek', 'Coe', 2, '9.1']

dictionary = dict(zip(fields, row))
print(dictionary)  # {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'}
print(type(dictionary))

filename = 'records.csv'

# newline=""  pomaga ominąc problem pustych lini przy zapisie do pliku na systemach windows
# pojawi sie po każdej linii
with open(filename, 'w', newline="") as csv_f:
    csvwriter = csv.writer(csv_f)  # narzędzie do zapisu pliku csv
    csvwriter.writerow(fields)  # metoda do zapisu wiersza
    csvwriter.writerow(row)  # metoda do zapisu wiersza

filename_2 = 'records_2.csv'
with open(filename_2, 'w', newline='') as f:
    # narzedzie potrafiące zapisać słownik do csv, fieldnames= - nazwy kolumn
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()  # zapisanie nagłowków
    csvwriter.writerow(dictionary)  # zapisujemy słownik do csv

dict_list = [
    {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'},
    {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'},
    {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'},
    {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'},
    {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'},
    {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'},
    {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'},
    {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'},
    {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'},
    {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'},
    {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'},
    {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'},
    {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'},
]
print(dict_list)
filename_3 = 'records_3.csv'
with open(filename_3, 'w', newline='') as file:
    csvwriter = csv.DictWriter(file, fieldnames=fields, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerows(dict_list)
# delimiter=";" - znak podziału
# Radek;Coe;2;9.1
