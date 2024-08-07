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

for i in range(-10, 0):
    print(i)
    # -10
    # -9
    # -8
    # -7
    # -6
    # -5
    # -4
    # -3
    # -2
    # -1

for c in lista3:
    if c == 2:  # blok gdy warunek spełniony
        c += 1  # c = c + 1
        print("Tylko dla c = 2")
        print(c)
    print("Przy każdym elemencie pętli", c)
# Przy każdym elemencie pętli 0
# Tylko dla c = 2
# Przy każdym elemencie pętli 3
# Przy każdym elemencie pętli 4
# Przy każdym elemencie pętli 6
# Przy każdym elemencie pętli 8
# spam += 1    spam = spam + 1  punkty = punkty + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1
# spam //= 1    spam = spam // 1
# spam **= 1    spam = spam ** 1

imiona = ["Radek", 'Tomek', 'Zenek', "Ania"]
print(imiona)
print(type(imiona))
# ['Radek', 'Tomek', 'Zenek', 'Ania']
# <class 'list'>

for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Ania

# wypisać elementy z listy z indeksem czyli: 0 Radek
for i in range(len(imiona)):  # range(4) 0123
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

# enumerate() - zwraca element kolekcji i jego pozycje
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Ania')
a, b = (0, 'Radek')  # rozpakowanie krotki
print(a, b)  # 0 Radek
# wstawienie rozpakowania krotki od razu w petle zmienne i,o przyjmą kolejne elementy z krotki
for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania
for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

ludzie = ['Radek', 'Tomek', 'Zenek', 'Magda']
wiek = [44, 55, 32, 27]
# wypisac to tak: Radek 44
for i in ludzie:
    print(i, wiek[ludzie.index(i)])
# Radek 44
# Tomek 55
# Zenek 32
# Magda 27
ludzie = ['Radek', 'Tomek', 'Zenek', 'Magda', "Martyna"]
wiek = [44, 55, 32, 27]
# for i in ludzie:
#     print(i, wiek[ludzie.index(i)])
# # Traceback (most recent call last):
# #   File "/Users/radoslawjaniak/PycharmProjects/pdnp-5-08-2024/3/petle_zad1.py", line 179, in <module>
# #     print(i, wiek[ludzie.index(i)])
# #              ~~~~^^^^^^^^^^^^^^^^^
# # IndexError: list index out of range

# zip() - łączy kolekcje w jedną (pary itd), tylko te które mają pełne dane
for i in zip(ludzie, wiek):
    print(i)
    # dostalismy krotki
# ('Radek', 44)
# ('Tomek', 55)
# ('Zenek', 32)
# ('Magda', 27)
# możemy je rozpakowac od razu w pętli
for l, w in zip(ludzie, wiek):
    print(l, w)
# Radek 44
# Tomek 55
# Zenek 32
# Magda 27

# 0 Radek 44
for i in enumerate(zip(ludzie, wiek)):
    print(i)
# (0, ('Radek', 44))
# (1, ('Tomek', 55))
# (2, ('Zenek', 32))
# (3, ('Magda', 27))
a, b = (0, ('Radek', 44))
print(a, b)  # 0 ('Radek', 44)
c, d = ('Radek', 44)
print(a, c, d)
(a, (c, d)) = (0, ('Radek', 44))  # musimy nawiasami wskazać wewnętrzną krotkę
for i, (l, w) in enumerate(zip(ludzie, wiek)):
    print(i, l, w)
# 0 Radek 44
# 1 Tomek 55
# 2 Zenek 32
# 3 Magda 27
