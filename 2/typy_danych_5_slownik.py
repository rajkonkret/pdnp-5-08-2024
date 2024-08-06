# słownik - para klucz-wartosc
# {'user': "Radek", 'wiek': 78}
# json - {"firstName":"John", "lastName":"Doe"}
# słownik jest odwzorowaniem jsona w pythonie
# nie moga się powtórzyc klucze

# pusty słownik
dictionary = dict()
print(type(dictionary))  # <class 'dict'>
print(dictionary)  # {}

dictionary_1 = {}
print(type(dictionary))  # <class 'dict'>

# dodawanie elementów do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 38
print(dictionary)  # {'imie': 'Radek', 'wiek': 38}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Radek', 38])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 38)])

# nadpisanie elementu
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 38}

# wypisanie elemntu
print(dictionary['imie'])  # Tomek
# print(dictionary['Imie'])  # KeyError: 'Imie'
print(dictionary.get('Imie'))  # None, nie ma klucza w słowniku
print(dictionary.get('Imie', 'Domyślna'))  # Domyślna - zwraca wartość ustawioną jako domyślną, gdy nie ma klucza

dictionary.update({'date': '12-12-2024'})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 38, 'date': '12-12-2024'}

dict_string = {'name': "Radek", 'surname': "Kowalski"}
print(dict_string)  # {'name': 'Radek', 'surname': 'Kowalski'}

dict_small = {'x': 2}
dict_small.update([('y', 3), ('z', 5)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 5}
dict_small.update([("k", 8)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 5, 'k': 8}
# ctrl alt l

# input() - pobiera dane od użytkownika
# tekst = input("Podaj imię")
# print("Masz na imię", tekst)
# print(type(tekst))
# Podaj imięRadek
# Masz na imię Radek
# <class 'str'>
# Podaj imię>? 12
# Masz na imię 12
# <class 'str'>

# aplikacja kalkulator
# pobrać dwie liczby od użytkownika 2 x input
# wyświetlić wynik działania (+) print()
# a = input("Podaj pierwszą liczbę")  # str
# b = float(input("Podaj drugą liczbę"))
# print("Wynik dodawania", int(a) + b)
# Podaj pierwszą liczbę>? 5
# Podaj drugą liczbę>? 6
# Wynik dodawania 11.0

# napisac aplikacje słownik
# pol - ang
# słownik z parami
# wyswietlicz kluzce (słowka, które umiemy prztłumaczyć)
# pobrać słówko do przetłumaczenia (klucz)
# wyświetle wartośc dla tego klucza
# print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
pol_ang = {'kot': 'cat', 'pies': 'dog'}
print("Znane nam słowka", pol_ang.keys())
odp = input("podaj słowko do przetłumaczenia")
print(pol_ang[odp.lower().replace(" ", "")])
print(pol_ang.get(odp.lower().replace(" ", ""), 'nie mo'))
# Znane nam słowka dict_keys(['kot', 'pies'])
# podaj słowko do przetłumaczenia Pi es
# dog
# nie mo
