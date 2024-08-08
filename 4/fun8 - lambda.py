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

lista = [1, 2, 3, 10, 20, 50, 70, 200, 300, 500]

