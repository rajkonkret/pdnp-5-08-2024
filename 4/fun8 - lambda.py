# funkcja lambda
# skrótowy zapis funkcji
# zwraca wynik
# funkcja anonimowa, możliwośc użycia w miejscu deklaracji
def odejmij(a, b):
    return a - b


odejmij2 = lambda a, b: a - b
print(odejmij2(10, 56))  # -46

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))  # 1230.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

# mapowanie danych
lista = [1, 2, 3, 10, 20, 50, 70, 200, 300, 500]
lista_wyn = []
for i in lista:
    lista_wyn.append(i * 2)

print(lista_wyn)  # [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]

print([i * 2 for i in lista])  # [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]


def zmien(x):
    return x * 2


lista_wyn_2 = []
for i in lista:
    lista_wyn_2.append(zmien(i))

print(lista_wyn_2)  # [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]

# funkcje wyższego rzędu
# map() - pobiera element z kolekcji, wykonuje na nim funkcję
print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]
# zastosowanie lambdy jako funkcji anonimowej, użycie w miejscu deklaracji
# anonimowa - nie jest przypisana do żadnej nazwy
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map(): [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 12, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 23, lista))}")
# Zastosowanie map(): [4, 8, 12, 40, 80, 200, 280, 800, 1200, 2000]
# Zastosowanie map(): [12, 24, 36, 120, 240, 600, 840, 2400, 3600, 6000]
# Zastosowanie map(): [23, 46, 69, 230, 460, 1150, 1610, 4600, 6900, 11500]

# filtrowanie danych
print(lista)  # [1, 2, 3, 10, 20, 50, 70, 200, 300, 500]
l3 = []
for i in lista:
    if i < 20:
        l3.append(i)
print(l3)  # [1, 2, 3, 10]

# filter()
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 20, lista))}")
# Zastosowanie filter(): [1, 2, 3, 10]
# wyfiltrowac dane dla x > 100
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 20, lista))}")
# wyfiltrowac dane dla x > 20 i x  < 300
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 20, lista))}")
