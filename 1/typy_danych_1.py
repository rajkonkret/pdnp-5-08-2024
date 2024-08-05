import sys

wiek = 47
rok = 2024
temp = 36.6

print(temp)
print(type(temp))
print(5 * "wiek")  # wiekwiekwiekwiekwiek
print(5 * wiek)  # 235

print(wiek + rok)  # 2071
print(wiek - rok)  # -1977
print(wiek * rok)  # 95128
print(wiek / rok)  # 0.023221343873517788 -> float

print(rok // wiek)  # część całkowita z dzielenia -> 43
print(rok % wiek)  # modulo - reszta z dzielenia -> 3
print(5 % 2)  # 1

print(wiek ** rok)  # potęgowanie

# len() - długość zbioru
print(len(str(wiek ** rok)))  # długość 3385 znaków
# print(len(str(wiek ** rok ** 2)))
# ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
# ctrl alt l

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

# przy liczbach float mamy bład zaokrąglenia
print(0.2 + 0.8)  # float -> 1.0
print(0.2 + 0.7)  # 0.8999999999999999
# The sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345
# 1.3 x 10 ^ 3 -> 1.3 x 2 ^ 4
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308,
#                max_exp=1024,
#                max_10_exp=308,
#                min=2.2250738585072014e-308,
#                min_exp=-1021,
#                min_10_exp=-307,
#                dig=15, mant_dig=53,
#                epsilon=2.220446049250313e-16,
#                radix=2,
#                rounds=1)

print(f"Sprawdzenie zmiennej {temp} {wiek}")  # Sprawdzenie zmiennej 36.6 47
print(f"""
{wiek}
    {temp}""")
# "47
#     36.6"

# typ logiczny
# prawda fałsz
# 1 - prawda, 0 - fałsz
# True False
czy_znasz_python = True
print(czy_znasz_python)  # True
print(type(czy_znasz_python))  # <class 'bool'>

print(int(True))  # 1
print(int(False))  # 0

print(bool(1))  # bool() - rzutowanie na boolean, True
print(bool(100))  # True
print(bool(-10))  # True
print(bool("radek"))  # True
print(bool(6.8))  # True

print(bool(0))  # False
print(bool(""))  # False, zbiór pusty
print(bool(None))  # None - nic, stan nieokreeslony, False, odpowiednik null w innych sytemach

# działania logiczne
# Expression    Evaluates to
# True and True    True
# True and False    False
# False and True    False
# False and False    False
# The or Operator’s Truth Table:
#
# Expression    Evaluates to
# True or True    True
# True or False    True
# False or True    True
# False or False    False
# The not Operator’s Truth Table:
#
# Expression    Evaluates to
# not True    False
# not False

# and -> i -> koniunkcja
print(True and True)  # True
print(True and False)  # False

# or - lub
print(True or False)  # True
print(False or False)  # False

# not - negacja
print(not True)  # False

a = 8
b = 6
# wynik porówanian jest typu bool (typ logiczny)
print(f"Porównanie {a} > {b} = {a > b}")  # Porównanie 8 > 6 = True
print(f"Porównanie {a} < {b} = {a < b}")  # Porównanie 8 < 6 = False
print(f"Porównanie {a <= b=}")  # Porównanie a <= b=False
print(f"Porównanie {a >= b=}")  # Porównanie a >= b=True
print(f"Porównanie {a} == {b} = {a == b}")  # == Porównanie, Porównanie 8 == 6 = False
print(f"Porównanie {a} != {b} = {a != b}")  # != rózna, Porównanie 8 != 6 = True
