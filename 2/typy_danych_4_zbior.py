# zbiór - set - przechowuje unikalne wartośći (elementy)
# nie zachowuje kolejności przy dodawaniu elementów
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # set() rzutowanie na zbiór
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

# utworzenie pustego zbioru (set)
zb2 = set()
print(zb2)  # set() - pusty set wyswietla się jako set()
print(type(zb2))  # <class 'set'>

# dodanie elemntu do zbioru
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}

# usunięcie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22}

# pop() - usunięcie pierwszego elementu
print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 18, 22}
zmienna = zbior.pop()
print(zmienna)  # 66

zbior_copy = zbior.copy()
print(zbior_copy)
print(id(zbior))  # 4304951712
print(id(zbior_copy))  # 4304948800

zbior_2 = {667, 11, 44, 18, 52, 62, 999, 999, 12.34}
print(type(zbior_2))
print(zbior_2)  # {999, 11, 44, 12.34, 18, 52, 667, 62}

# suma zbiorów - zwraca nowy zbiór
print(zbior | zbior_2)  # {999, 777, 11, 44, 12.34, 18, 52, 22, 667, 62}
print(zbior.union(zbior_2))  # {999, 777, 11, 44, 12.34, 18, 52, 22, 667, 62}

# częśc wspólna - zwraca nowy zbiór
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# różnica - zwraca nowy zbiór
print(zbior - zbior_2)  # {777, 22}
print(zbior.difference(zbior_2))  # {777, 22}
print(zbior_2.difference(zbior))  # {999, 12.34, 52, 667, 62}
# {777, 11, 44, 18, 22} - {999, 11, 44, 12.34, 18, 52, 667, 62} = {777,22}

# łączy zbiory, zmienia zbiór bazowy!!! (zbior)
zbior.update(zbior_2)
print(zbior)  # {999, 777, 11, 44, 12.34, 18, 52, 22, 667, 62}

krotka = tuple(zbior)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # (999, 777, 11, 44, 12.34, 18, 52, 22, 667, 62)

lista = list(zbior_2)
print(type(lista))  # <class 'list'>
print(lista)  # [999, 11, 44, 12.34, 18, 52, 667, 62]

# sprawdzenie czy elemnt istnieje w zbiorze
print(999 in zbior_2)  # True
