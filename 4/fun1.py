# funkcje - wydzielony fragment kodu, można go wywołąć wielokrotnie w dowolnym momencie
# funkcja musi być najpierw zadeklarowana
# w miejscu deklaracji funkcja się nie wykonuje
# żeby funkcja się wywołała trzeba ją uruchomić

# funkcje nie zwracające wyniku
a = 6
b = 8


# deklaracja funkcji
# słówko def nazwa_funkcji nawiasy ()
# funkcja bez argumentów
# zalecenie PEP8 wymaga by deklaracja funkcji była oddzielona dwoma pustymi liniami od reszty programu
def dodaj():
    print(a + b)


def dodaj2(a, b):  # a,b - dwa obowiązkowe do przekazania argumenty
    print(a + b)


def odejmij(a, b, c=0):  # argument c ma wartośc domyślną
    print(a - b - c)


# wywołąnie funkcji, uruchomienie
# nazwa_funkcji i nawiasy ()
dodaj()  # 14 wypisuje wynik dodawania
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(56, 89)  # 145
dodaj2(a, b)  # 14
# argument c ma wartość domyślną, może być pomijany przy wywołaniu funkcji
# argumenty po pozycji
odejmij(1, 2)  # -1
odejmij(1, 2, 4)  # -5

# argumenty przekazane po nazwie
odejmij(b=8, c=0, a=7)
odejmij(b=9, a=9)  # 0

# argumenty mieszane
odejmij(1, c=90, b=8)
# pozycyjne muszą byc przed nazwanymi
# odejmij(a=1, c=9, 7)  # SyntaxError: positional argument follows keyword argument

# nasza funkcja nic nnie zwraca do głownego programu
print(dodaj())
# 14
# None
# print(dodaj() + dodaj2(8, 90))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
