# petle - dają nam możliwość wykonannai wielokrotnie tego samego kodu
# for - pętla iteracyjna
import random

for i in range(5):  # 0 do 4
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(5):  # _ niema zmienna
    print("Test podłoga")
    # print(_)
# Test podłoga
# Test podłoga
# Test podłoga
# Test podłoga
# Test podłoga

for i in range(20):
    print(i * 2)

# na podstawie lotto
# prerobić na petle

lista_kula = list(range(1, 50))  # 1 do 49 generujemy liste kul
lista_wyn = []  # tworzymy pusta listę
for _ in range(6):  # od 0 do 5 ale 6 razy
    wyn = random.choice(lista_kula)  # losujemy liczbę z listy lista_kula i zapamiętujemy w zmiennej wyn
    lista_kula.remove(wyn)  # usuwamy wylosowany element z listy
    print(wyn)  # wypisujemy ten element
    lista_wyn.append(wyn)  # do list_wyn dodjemy wylosowaną liczbę

print(lista_wyn)  # [41, 2, 9, 8, 32, 21], wyswietlamy listę wylosowanych liczb

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# list comprehension
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

print(lista_wyn)  # [40, 39, 12, 6, 46, 43]
for c in lista_wyn:  # weź całą kolekcję
    if c > 10:
        print("Większe od 10", c)
    else:
        print("C mniejsze od 10", c)
# Większe od 10 40
# Większe od 10 39
# Większe od 10 12
# Większe od 10 46
# Większe od 10 43
# C mniejsze od 10 6
# Większe od 10 12
# C mniejsze od 10 4
# Większe od 10 15
# Większe od 10 22
# Większe od 10 26

for i in range(0, 10, 2):  # start, stop, krok
    print(i)
# 0
# 2
# 4
# 6
# 8

for i in range(10, 0, -2):  # krok w tył
    print(i)
# 10
# 8
# 6
# 4
# 2
