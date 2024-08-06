# krotka - kolekcja niemutowalna
# pozwala efektywniej zarządzać pamięcią
# krotka jednoelementowa - stała - zmienna

# ('Radek', 'Karol', 'Tomek')
tupla = "Radek"
print(type(tupla))  # <class 'str'>

tupla_2 = ("Radek")
print(type(tupla_2))  # <class 'str'>

tupla_3 = "Radek",
print(type(tupla_3))  # <class 'tuple'>

# PEP8 zaleca przy tuplach jednoelemntowych używać nawias
tupla_4 = ("Radek",)
print(type(tupla_4))  # <class 'tuple'>
print(tupla_4)  # ('Radek',)

# tupla_liczba = 43, 55, 22.34, 11, 200
tupla_liczba = (43, 55, 22.34, 11, 200)
print(tupla_liczba)  # (43, 55, 22.34, 11, 200)
print(type(tupla_liczba))  # <class 'tuple'>

# tupla jest niemutowalna, nie da się dokonać zmiman
# tupla_liczba[2] = 123  # TypeError: 'tuple' object does not support item assignment

# del tupla_liczba
# print(tupla_liczba)  # NameError: name 'tupla_liczba' is not defined

tupla_imiona = "Radek", 'Tomek', "Zenek", "Olek", 'Robert', 'Michał'
print(tupla_imiona)
print(type(tupla_imiona))

print(tupla_imiona.index("Radek"))  # 0
print(tupla_imiona.count("Olek"))  # 1

# rozpakowanie krotki
tup = 1, 2
print(type(tup))  # <class 'tuple'>
# a, b = 1, 2
a, b = tup
print(a, b)  # 1 2
tup_1 = 1, 2, 3
# a, b = tup_1  # ValueError: too many values to unpack (expected 2)
a, *b = tup_1  # * - worek na dane
print(a, b)  # 1 [2, 3]
print(tupla_imiona)
name1, name2, *name3 = tupla_imiona
print(name1, name2, name3)  # Radek Tomek ['Zenek', 'Olek', 'Robert', 'Michał']

name1, *name2, name3 = tupla_imiona
print(name1, name2, name3)  # Radek ['Tomek', 'Zenek', 'Olek', 'Robert'] Michał
print(type(name1))  # <class 'str'>

# sortowanie krotki zwraca nową listę
print(sorted(tupla_imiona))  # ['Michał', 'Olek', 'Radek', 'Robert', 'Tomek', 'Zenek']
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Olek', 'Robert', 'Michał')

lista = list(tupla_imiona)
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Olek', 'Robert', 'Michał']
print(type(lista))  # <class 'list'>
