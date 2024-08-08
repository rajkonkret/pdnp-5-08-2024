# zmienne o zasięgu globalnym
a = 10
b = 10


def dodaj():
    a = 7  # zasięg lokalny, nie wpływa na globalna zmienna o tej samej nazwie
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)  # pryjmie a i b z przestrzeni globalnej


def dodaj3():
    global a  # uzyj zmiennej globalnej
    a = 9  # nadpisujemy globalne a
    b = 89
    print(a + b)


# f - string format, wartość zmiennej w klamerkach {}
print(f"Wartość a z góry {a=}")  # Wartość a z góry a=10
dodaj()  # 15
print(f"Wartość a z góry {a=}")  # Wartość a z góry a=10
dodaj2()  # 20
print(f"Wartość a z góry {a=}")  # Wartość a z góry a=10
dodaj3()  # 98 zmienilismy wartość a globalnego
# a=9
print(f"Wartość a z góry {a=}")  # Wartość a z góry a=9
dodaj2()  # 19
