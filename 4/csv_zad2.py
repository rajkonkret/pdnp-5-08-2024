import csv

fields = []
rows = []

# filename = 'records_2.csv'
filename = 'records_3.csv'

with open(filename, 'r') as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    print(dialect.delimiter)  # ;
    # StopIteration - pojawi się gdy z iteratora wyciągniemy wszystkie dane
    f.seek(0)  # ponowny odczyt od pierwszego elementu
    csvreader = csv.reader(f, delimiter=dialect.delimiter)
    # csvreader = csv.reader(f, delimiter=";")
    # <_csv.reader object at 0x104eb95b0>, iterator pobierze jeden wiersz i zapamieta który ma dać następnym razem
    print(csvreader)

    fields = next(csvreader)  # next() pobranie pojedynczego elementu, licznik ustawiony na nastepny
    for row in csvreader:  # pobrało drugi wiersz
        print(row)
        rows.append(row)
# ['name', 'branch', 'year', 'cgpa'] - chcemy by trafiło do fields
# ['Radek', 'Coe', '2', '9.1']  - chcemy by trafiło do rows, ['Radek;Coe;2;9.1'] -> ['Radek', 'Coe', '2', '9.1']
print('Fields:', fields)
print(f"Rows: {rows}")

# ['Radek', 'Coe', '2', '9.1']
# Fields: ['name', 'branch', 'year', 'cgpa']
# Rows: [['Radek', 'Coe', '2', '9.1']]
