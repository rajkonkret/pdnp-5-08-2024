# funkcje zwracające wynik
# kończy się słowkiem return
# gdy napotka na return wychodzi z funkcji

def dodaj(a, b):
    return a + b


def odejmij(a=0, b=0, c=0):
    return a - b - c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(78, 34))  # 112
wynik = dodaj(67, 90)
print(wynik)  # 157

print(odejmij(5, 7, 8))  # -10
print(odejmij(5, 8))
print(odejmij(5))
print(odejmij())  # 0
print(odejmij(a=90))  # 90
print(odejmij(b=89, c=78))  # -167
print(odejmij(4, c=90))  # -86

print(oblicz_vat(1000))
print(oblicz_vat(1000, 15))
print(oblicz_vat(vat=8, cena=15000))
# 1230.0
# 1150.0
# 16200.0
print(oblicz_vat(1000) + dodaj(78, 90))  # 1398.0

