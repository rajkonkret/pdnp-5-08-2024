# Kolekcje
# lista - przechowuje wiele danych, różnego typu na raz
# zachowuje kolejność przy dodawaniu elementów

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(type(pusta_lista))  # <class 'list'>
print(pusta_lista)  # []

# append() - dodanie elementu (na końcu) do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Marek")
lista.append("Magda")
lista.append('Ania')
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Marek', 'Magda', 'Ania']
#     0        1        2        3        4        5
#    (-6)    (-5)     (-4)     (-3)     (-2)      (-1)
print(lista[0])  # Radek
print(lista[2])  # Zenek
print(lista[4])  # Magda

print(len(lista))  # 6 - długość listy
# print(lista[6])  # IndexError: list index out of range
print(lista[len(lista) - 1])  # Ania
print(lista[-1])  # Ania, ostatni element
print(lista[-4])  # Zenek

# wyświetlenie fragmentu listy (slicowanie)
print(lista[0:3])  # start:stop -> 012  # ['Radek', 'Tomek', 'Zenek'], z prawej zbiór otwarty
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek']
print(lista[2:])  # ['Zenek', 'Marek', 'Magda', 'Ania'], 2345
print(lista[2:5])  # ['Zenek', 'Marek', 'Magda'], 234
print(lista[:])  # ['Radek', 'Tomek', 'Zenek', 'Marek', 'Magda', 'Ania'] - cała lista
print(lista[-2:0])  # [] -> [4:0]
print(lista[0:-2])  # [0:4] -> ['Radek', 'Tomek', 'Zenek', 'Marek']
print(lista[2:3])  # ['Zenek']
print(lista[2:10])  # ['Zenek', 'Marek', 'Magda', 'Ania']
print(lista[10:29])  # []

lista_15 = list(range(15))  # 0..14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_15[0:10:2])  # [start:stop:krok] [0, 2, 4, 6, 8]
print(list(range(0, 15, 2)))  # [0, 2, 4, 6, 8, 10, 12, 14]
print(lista_15[-10])  # 5

# nadpisanie elementu w liście
lista[3] = "Mikołaj"
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Mikołaj', 'Magda', 'Ania']
print(len(lista))  # 6

# dopisanie (rozszerzenie listy) we wskazanym indeksie
lista.insert(1, "Karol")
print(lista)  # ['Radek', 'Karol', 'Tomek', 'Zenek', 'Mikołaj', 'Magda', 'Ania']
print(len(lista))  # 7

# sprawdzenie indeksu dla elementu
print(lista.index("Mikołaj"))  # indeks numer 4

# usunięcie elemntu z listy, pierwsze wystąpienie
lista.remove("Mikołaj")
print(lista)  # ['Radek', 'Karol', 'Tomek', 'Zenek', 'Magda', 'Ania']

# usunięcie elementu z listy po indeksie
# zwraca usunięty element
print(lista.pop(5))  # Ania
print(lista)  # ['Radek', 'Karol', 'Tomek', 'Zenek', 'Magda']
print(lista.pop(-2))  # Zenek
print(lista.pop())  # Magda - usunie ostatni

a = 1
b = 3
a = b
print(a, b)  # 3 3
b = 7
print(a, b)  # 3 7

lista_2 = lista  # a = b, kopiuje referencje (adres w pamięci)
lista_copy = lista.copy()  # kopia elementów listy
print(lista_2, lista)  # ['Radek', 'Karol', 'Tomek'] ['Radek', 'Karol', 'Tomek']
lista.clear()  # b=7, usunięcie elemntów z listy (wszystkich)
print(lista_2, lista)  # [] []
print(lista_copy)
print(id(lista_2))  # 4310567296
print(id(lista))  # 4310567296
print(id(lista_copy))  # 4311170624

liczby = [54, 999, 34, 22, 12.34, 687]
print(liczby)  # [54, 999, 34, 22, 12.34, 687]
print(type(liczby))  # <class 'list'>

print(int("45"))  # 45

liczby.sort()
print(liczby)  # [12.34, 22, 34, 54, 687, 999]

liczby = [54, 999, 34, 22, 12.34, 687, "A"]
print(liczby)  # [54, 999, 34, 22, 12.34, 687, 'A']
# liczby.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'

lista_osob = ['radek', 'ola', 'lena', 'agata']
lista_osob.sort()
print(lista_osob)  # ['agata', 'lena', 'ola', 'radek']

lista_osob.sort(reverse=True)
print(lista_osob)  # ['radek', 'ola', 'lena', 'agata']

lista_osob.reverse()
print(lista_osob)  # ['agata', 'lena', 'ola', 'radek']

liczby[3] = 666
print(liczby[0:3])
print(liczby[-2])
print(liczby)  # [54, 999, 34, 666, 12.34, 687, 'A']

print(liczby.pop(2))  # 34, usunie element o indeksie 2
liczby.remove(54)  # usunie liczbę 54
print(liczby)  # [999, 666, 12.34, 687, 'A']

del liczby  # usnie listę z pamięci
# print(liczby)  # NameError: name 'liczby' is not defined

tekst = "Pyth on."
lista1 = list(tekst)
print(lista1)  # ['P', 'y', 't', 'h', ' ', 'o', 'n', '.'] rozpakowanie sekwencji

lista2 = [tekst]
print(lista2)  # ['Pyth on.']

krotka = tuple(lista_copy)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # ('Radek', 'Karol', 'Tomek')
